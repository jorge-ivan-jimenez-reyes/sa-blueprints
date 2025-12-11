from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import CloudFront, ALB, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito, IAM, SecretsManager, WAF
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import SNS
from diagrams.aws.engagement import SES
from diagrams.onprem.client import Users, Client
from diagrams.onprem.compute import Server
from diagrams.generic.device import Mobile
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.8",
    "ranksep": "1.0",
}

with Diagram(
    "Clinical Research Platform - Arquitectura Completa",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    with Cluster("Usuarios"):
        participants = Mobile("Participantes\n(iOS/Android)")
        researchers = Client("Investigadores\n(WebApp)")

    with Cluster("Edge Layer"):
        dns = Route53("Route 53\nDNS")
        cdn = CloudFront("CloudFront\nCDN")
        waf = WAF("AWS WAF\nProteccion")

    with Cluster("AWS VPC - HIPAA Compliant"):
        
        with Cluster("Public Subnet"):
            alb = ALB("Application\nLoad Balancer")
        
        with Cluster("Private Subnet"):
            
            with Cluster("Application Layer"):
                api = Server("API Backend\n(Node.js/Python)")
                webapp = Server("WebApp\n(React)")
            
            with Cluster("Authentication"):
                cognito = Cognito("AWS Cognito\n2FA/MFA")
                secrets = SecretsManager("Secrets\nManager")
            
            with Cluster("Notifications"):
                sns = SNS("SNS\nPush Notifications")
                ses = SES("SES\nEmail Service")
        
        with Cluster("Data Layer - Encrypted"):
            rds = RDS("RDS PostgreSQL\nHIPAA Compliant")
            s3_docs = S3("S3 Documents\nConsentimientos")
            s3_backup = S3("S3 Backups\nEncrypted")

    with Cluster("Monitoring"):
        cloudwatch = Cloudwatch("CloudWatch\nLogs & Metrics")
        audit = Rack("Audit Trail\nCompliance")

    participants >> Edge(color="blue", style="bold") >> dns
    researchers >> Edge(color="orange", style="bold") >> dns
    
    dns >> waf >> cdn >> alb
    
    alb >> Edge(color="green") >> api
    alb >> Edge(color="green") >> webapp
    
    api >> Edge(color="purple") >> cognito
    webapp >> Edge(color="purple") >> cognito
    cognito >> secrets
    
    api >> Edge(color="brown") >> rds
    api >> Edge(color="gray") >> s3_docs
    
    api >> Edge(color="cyan") >> sns
    api >> Edge(color="cyan") >> ses
    
    rds >> Edge(style="dashed") >> s3_backup
    
    api >> Edge(color="yellow", style="dashed") >> cloudwatch
    cloudwatch >> audit
