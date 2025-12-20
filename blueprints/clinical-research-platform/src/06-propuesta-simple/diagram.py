from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate, ECR
from diagrams.aws.database import RDS
from diagrams.aws.network import CloudFront, ALB, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito
from diagrams.aws.management import Cloudwatch
from diagrams.aws.engagement import SES
from diagrams.aws.integration import SNS
from diagrams.generic.device import Mobile
from diagrams.onprem.client import Client

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.6",
    "ranksep": "0.7",
}

with Diagram(
    "Propuesta A - Fargate Basico",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    with Cluster("Usuarios"):
        mobile = Mobile("App Movil")
        web = Client("WebApp")

    dns = Route53("Route 53")
    cdn = CloudFront("CloudFront")

    with Cluster("AWS"):
        alb = ALB("ALB")
        
        with Cluster("Fargate"):
            api = Fargate("API")
            webapp = Fargate("WebApp")
        
        ecr = ECR("ECR")
        cognito = Cognito("Cognito")
        
        with Cluster("Data"):
            rds = RDS("RDS PostgreSQL\nSingle-AZ")
            s3 = S3("S3")
        
        sns = SNS("SNS")
        ses = SES("SES")

    cloudwatch = Cloudwatch("CloudWatch")

    mobile >> Edge(color="blue") >> dns
    web >> Edge(color="orange") >> dns
    
    dns >> cdn >> alb
    
    alb >> api
    alb >> webapp
    ecr >> Edge(style="dashed") >> api
    
    api >> Edge(color="purple") >> cognito
    
    api >> Edge(color="brown") >> rds
    api >> Edge(color="gray") >> s3
    
    api >> sns
    api >> ses
    
    api >> Edge(style="dashed") >> cloudwatch
