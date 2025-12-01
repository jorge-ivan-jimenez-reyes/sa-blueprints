"""
IA Interactive - Kubernetes/EKS Architecture
=============================================
Diagrama simplificado del cluster EKS

Ejecutar: python 05_kubernetes.py
Output: output/05_kubernetes.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS, EC2
from diagrams.aws.network import ALB
from diagrams.aws.compute import ECR
from diagrams.k8s.compute import Pod, Deployment
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.podconfig import ConfigMap, Secret
from diagrams.onprem.gitops import Argocd
from diagrams.onprem.monitoring import Prometheus, Grafana

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

with Diagram(
    "IA Interactive - Amazon EKS Cluster",
    filename="output/05_kubernetes",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    # Container Registry
    ecr = ECR("Amazon ECR")
    
    # ALBs
    alb_public = ALB("ALB Público")
    alb_internal = ALB("ALB Interno")
    
    # EKS Cluster
    with Cluster("Amazon EKS Cluster (t3.small nodes - $0.02/hr)"):
        
        # Worker Node
        with Cluster("Worker Node"):
            node = EC2("t3.small\n2 vCPU / 2GB")
        
        # Namespace: Apps
        with Cluster("Namespace: apps"):
            with Cluster("Front Office"):
                ing_fo = Ingress("Ingress")
                svc_fo = Service("Service")
                pod_fo = Pod("Pod\nNext.js")
            
            with Cluster("Back Office"):
                ing_bo = Ingress("Ingress")
                svc_bo = Service("Service")
                pod_bo = Pod("Pod\nAdmin")
            
            with Cluster("Backend"):
                svc_be = Service("Service")
                pod_be = Pod("Pod\nFastAPI")
                
                cm = ConfigMap("ConfigMap")
                sec = Secret("Secrets")
        
        # Namespace: Platform
        with Cluster("Namespace: platform"):
            prometheus = Prometheus("Prometheus")
            grafana = Grafana("Grafana")
            argocd = Argocd("Argo CD")
    
    # Connections - ECR
    ecr >> Edge(color="green", label="Pull") >> pod_fo
    ecr >> Edge(color="green") >> pod_bo
    ecr >> Edge(color="green") >> pod_be
    
    # Connections - Traffic
    alb_public >> ing_fo >> svc_fo >> pod_fo
    alb_internal >> ing_bo >> svc_bo >> pod_bo
    svc_be >> pod_be
    
    # Config
    cm >> Edge(style="dotted") >> pod_be
    sec >> Edge(style="dotted") >> pod_be
    
    # Observability
    pod_fo >> Edge(color="yellow", style="dashed", label="/metrics") >> prometheus
    pod_be >> Edge(color="yellow", style="dashed") >> prometheus
    prometheus >> grafana
    
    # GitOps
    argocd >> Edge(color="purple", label="Sync") >> pod_fo
    argocd >> Edge(color="purple") >> pod_bo
    argocd >> Edge(color="purple") >> pod_be


print("✅ Diagrama generado: output/05_kubernetes.png")
