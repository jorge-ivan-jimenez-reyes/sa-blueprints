from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate, ECR
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import CloudFront, ALB, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito, WAF, SecretsManager
from diagrams.aws.management import Cloudwatch, Cloudtrail
from diagrams.aws.engagement import SES
from diagrams.aws.integration import SNS
from diagrams.aws.mobile import Amplify
from diagrams.generic.device import Mobile
from diagrams.onprem.client import Client
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.5",
    "ranksep": "0.5",
}

with Diagram(
    "Propuesta A - Fargate Serverless",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    with Cluster("Usuarios"):
        mobile_user = Mobile("Participantes")
        web_user = Client("Investigadores")

    with Cluster("Frontend"):
        with Cluster("Mobile App"):
            react_native = Rack("React Native\niOS / Android")
        
        with Cluster("WebApp"):
            amplify = Amplify("AWS Amplify")
            react = Rack("React")

    with Cluster("Edge"):
        dns = Route53("Route 53")
        waf = WAF("WAF")
        cdn = CloudFront("CloudFront")

    with Cluster("AWS Backend"):
        alb = ALB("ALB")
        
        with Cluster("Fargate (Serverless)"):
            api = Fargate("API Backend")
            worker = Fargate("Worker")
        
        ecr = ECR("ECR")
        
        with Cluster("Security"):
            cognito = Cognito("Cognito 2FA")
            secrets = SecretsManager("Secrets")
        
        with Cluster("Data"):
            rds = RDS("RDS PostgreSQL\nSingle-AZ")
            cache = ElastiCache("Redis")
            s3 = S3("S3")

        sns = SNS("SNS")
        ses = SES("SES")

    with Cluster("Monitoring"):
        cloudwatch = Cloudwatch("CloudWatch")
        cloudtrail = Cloudtrail("CloudTrail")

    mobile_user >> react_native
    web_user >> amplify
    amplify >> react
    
    react_native >> Edge(color="blue") >> dns
    react >> Edge(color="orange") >> dns
    
    dns >> waf >> cdn >> alb
    
    alb >> api
    alb >> worker
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
