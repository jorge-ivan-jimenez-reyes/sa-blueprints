"""
IA Interactive - Backend Architecture
=====================================
Diagrama del backend monolítico FastAPI

Ejecutar: python 04_backend.py
Output: output/04_backend.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.security import SecretsManager
from diagrams.aws.network import ALB
from diagrams.programming.language import Python
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

with Diagram(
    "IA Interactive - Backend (FastAPI Monolith)",
    filename="output/04_backend",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    # Consumers
    with Cluster("Consumidores"):
        front = Rack("Front Office\n(Next.js)")
        back = Rack("Back Office\n(Microfrontends)")
    
    # Load Balancer
    alb = ALB("ALB\n(Internal Service)")
    
    # EKS Backend
    with Cluster("Amazon EKS - Backend"):
        with Cluster("FastAPI Pods (HPA)"):
            pod1 = EKS("Pod 1\nFastAPI")
            pod2 = EKS("Pod 2\nFastAPI")
    
    # API Structure
    with Cluster("API v1 - Routers"):
        with Cluster("Routers"):
            r_clientes = Python("/clientes")
            r_servicios = Python("/servicios")
            r_contenido = Python("/contenido")
            r_carreras = Python("/carreras")
            r_metricas = Python("/metricas")
            r_health = Python("/health")
    
    # Services Layer
    with Cluster("Services Layer"):
        svc = Rack("Business Logic\nServices")
    
    # Integrations
    with Cluster("Integraciones Externas"):
        hubspot = Rack("HubSpot\nClient")
        wordpress = Rack("WordPress\nClient")
        email = Rack("Email\nClient")
    
    # Data Layer
    with Cluster("Data Layer"):
        rds = RDS("Amazon RDS\nPostgreSQL")
        s3 = S3("Amazon S3\nMedia Files")
        secrets = SecretsManager("Secrets\nManager")
    
    # Connections
    front >> Edge(color="blue", label="REST API") >> alb
    back >> Edge(color="orange", label="REST API") >> alb
    
    alb >> pod1
    alb >> pod2
    
    pod1 >> Edge(color="purple", style="dashed") >> r_clientes
    pod1 >> Edge(color="purple", style="dashed") >> r_servicios
    pod1 >> Edge(color="purple", style="dashed") >> r_contenido
    pod1 >> Edge(color="purple", style="dashed") >> r_carreras
    pod1 >> Edge(color="purple", style="dashed") >> r_metricas
    pod1 >> Edge(color="purple", style="dashed") >> r_health
    
    r_clientes >> svc
    r_servicios >> svc
    r_contenido >> svc
    r_carreras >> svc
    r_metricas >> svc
    
    svc >> Edge(color="brown") >> rds
    svc >> Edge(color="gray") >> s3
    svc >> Edge(color="red") >> secrets
    
    svc >> Edge(color="green", style="dashed") >> hubspot
    svc >> Edge(color="green", style="dashed") >> wordpress
    svc >> Edge(color="green", style="dashed") >> email


print("✅ Diagrama generado: output/04_backend.png")

