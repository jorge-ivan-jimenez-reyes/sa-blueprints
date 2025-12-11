from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS, EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import CloudFront, ELB, ALB, VPC, PrivateSubnet, PublicSubnet
from diagrams.aws.storage import S3
from diagrams.aws.devtools import Codebuild
from diagrams.aws.security import IAM, SecretsManager
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import Eventbridge
from diagrams.onprem.client import Users, Client
from diagrams.onprem.network import Nginx
from diagrams.onprem.vcs import Github
from diagrams.onprem.container import Docker
from diagrams.onprem.gitops import Argocd
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.saas.analytics import Snowflake
from diagrams.generic.compute import Rack
from diagrams.generic.network import VPN

graph_attr = {
    "fontsize": "24",
    "bgcolor": "white",
    "pad": "0.8",
    "splines": "spline",
    "nodesep": "1.0",
    "ranksep": "1.2",
}

with Diagram(
    "IA Interactive - Arquitectura Completa AWS EKS",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    # Usuarios
    with Cluster("Usuarios"):
        visitors = Users("Visitantes\nClientes/Talentos")
        operators = Client("Equipo Interno\n(VPN)")

    # Edge/CDN Layer
    with Cluster("Edge Layer"):
        cdn = CloudFront("Amazon\nCloudFront")

    # VPC Principal
    with Cluster("AWS VPC"):
        
        # Public Subnet
        with Cluster("Public Subnet"):
            alb_public = ALB("ALB Público\n(Front Office)")
        
        # Private Subnet
        with Cluster("Private Subnet"):
            alb_internal = ALB("ALB Interno\n(Back Office)")
            
            # EKS Cluster
            with Cluster("Amazon EKS Cluster"):
                
                with Cluster("Frontend Pods"):
                    front_office = EKS("Front Office\nNext.js")
                    back_office = EKS("Back Office\nMicrofrontends")
                
                with Cluster("Backend Pods"):
                    backend = EKS("Backend\nFastAPI")
                
                with Cluster("Observability Namespace"):
                    prometheus = Prometheus("Prometheus")
                    grafana = Grafana("Grafana")
            
            # VPN Access
            vpn = VPN("Tailscale\nVPN")
        
        # Data Layer
        with Cluster("Data Layer"):
            rds = RDS("Amazon RDS\nPostgreSQL")
            s3 = S3("Amazon S3\nAssets")

    # External Integrations
    with Cluster("Integraciones Externas"):
        hubspot = Rack("HubSpot")
        ga4 = Rack("Google\nAnalytics")
        wordpress = Rack("WordPress\n(Headless)")

    # DevOps
    with Cluster("CI/CD Pipeline"):
        github = Github("GitHub")
        gh_actions = Codebuild("GitHub\nActions")
        argocd = Argocd("Argo CD\nGitOps")
        ecr = Docker("Amazon\nECR")

    # Connections - Users
    visitors >> Edge(color="blue", style="bold") >> cdn
    cdn >> Edge(color="blue") >> alb_public
    alb_public >> Edge(color="blue") >> front_office
    
    operators >> Edge(color="orange", style="bold") >> vpn
    vpn >> Edge(color="orange") >> alb_internal
    alb_internal >> Edge(color="orange") >> back_office
    
    # Frontend to Backend
    front_office >> Edge(color="purple") >> backend
    back_office >> Edge(color="purple") >> backend
    
    # Backend to Data
    backend >> Edge(color="brown") >> rds
    backend >> Edge(color="gray") >> s3
    
    # Backend to External
    backend >> Edge(color="gray", style="dashed") >> hubspot
    backend >> Edge(color="gray", style="dashed") >> wordpress
    
    # Frontend to Analytics (client-side)
    front_office >> Edge(color="gray", style="dotted") >> ga4
    
    # Observability
    backend >> Edge(color="green", style="dashed") >> prometheus
    prometheus >> grafana
    vpn >> Edge(color="yellow", style="dotted") >> grafana
    vpn >> Edge(color="yellow", style="dotted") >> argocd
    
    # CI/CD Flow
    github >> Edge(color="green") >> gh_actions
    gh_actions >> Edge(color="green") >> ecr
    ecr >> Edge(color="green", style="dashed") >> argocd
    argocd >> Edge(color="green") >> front_office
    argocd >> Edge(color="green") >> back_office
    argocd >> Edge(color="green") >> backend
