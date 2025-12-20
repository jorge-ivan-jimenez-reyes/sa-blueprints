from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate, ECR
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import CloudFront, ALB, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito, WAF, SecretsManager
from diagrams.aws.management import Cloudwatch, Cloudtrail
from diagrams.aws.engagement import SES
from diagrams.aws.integration import SNS
from diagrams.generic.device import Mobile
from diagrams.onprem.client import Client

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.5",
    "ranksep": "0.6",
}

with Diagram(
    "Propuesta B - Fargate + Seguridad",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    with Cluster("Usuarios"):
        mobile = Mobile("App Movil")
        web = Client("WebApp")

    with Cluster("Edge"):
        dns = Route53("Route 53")
        waf = WAF("WAF")
        cdn = CloudFront("CloudFront")

    with Cluster("AWS VPC"):
        alb = ALB("ALB")
        
        with Cluster("Fargate"):
            api = Fargate("API")
            webapp = Fargate("WebApp")
        
        ecr = ECR("ECR")
        
        with Cluster("Security"):
            cognito = Cognito("Cognito 2FA")
            secrets = SecretsManager("Secrets")
        
        with Cluster("Data"):
            rds = RDS("RDS PostgreSQL\nMulti-AZ")
            cache = ElastiCache("Redis")
            s3 = S3("S3")

        sns = SNS("SNS")
        ses = SES("SES")

    with Cluster("Monitoring"):
        cloudwatch = Cloudwatch("CloudWatch")
        cloudtrail = Cloudtrail("CloudTrail")

    mobile >> Edge(color="blue") >> dns
    web >> Edge(color="orange") >> dns
    
    dns >> waf >> cdn >> alb
    
    alb >> api
    alb >> webapp
    ecr >> Edge(style="dashed") >> api
    
    api >> Edge(color="purple") >> cognito
    cognito >> secrets
    
    api >> Edge(color="brown") >> rds
    api >> Edge(color="cyan") >> cache
    api >> Edge(color="gray") >> s3
    
    api >> sns
    api >> ses
    
    api >> Edge(style="dashed") >> cloudwatch
    cloudwatch >> cloudtrail
