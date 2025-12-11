from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, ECS, ECR
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import VPC, PrivateSubnet, PublicSubnet, ALB, NATGateway, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito, IAM, SecretsManager, WAF, KMS
from diagrams.aws.management import Cloudwatch, Cloudtrail
from diagrams.aws.integration import SNS, SQS
from diagrams.aws.engagement import SES

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.6",
    "ranksep": "0.8",
}

with Diagram(
    "Clinical Research - AWS Infrastructure (HIPAA)",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    dns = Route53("Route 53")
    waf = WAF("WAF")
    
    with Cluster("AWS VPC - HIPAA Compliant"):
        
        with Cluster("Public Subnets"):
            alb = ALB("ALB")
            nat = NATGateway("NAT Gateway")
        
        with Cluster("Private Subnets - App Tier"):
            with Cluster("ECS Cluster"):
                api_service = ECS("API Service")
                webapp_service = ECS("WebApp Service")
            ecr = ECR("ECR Registry")
        
        with Cluster("Private Subnets - Data Tier"):
            with Cluster("Database"):
                rds_primary = RDS("RDS Primary\nPostgreSQL")
                rds_replica = RDS("RDS Replica\nRead Only")
            cache = ElastiCache("ElastiCache\nRedis")
    
    with Cluster("Security Services"):
        cognito = Cognito("Cognito")
        secrets = SecretsManager("Secrets Manager")
        kms = KMS("KMS\nEncryption Keys")
        iam = IAM("IAM Roles")
    
    with Cluster("Storage - Encrypted"):
        s3_docs = S3("Documents")
        s3_backup = S3("Backups")
        s3_logs = S3("Logs")
    
    with Cluster("Messaging"):
        sns = SNS("SNS")
        ses = SES("SES")
        sqs = SQS("SQS")
    
    with Cluster("Monitoring & Audit"):
        cloudwatch = Cloudwatch("CloudWatch")
        cloudtrail = Cloudtrail("CloudTrail\nAudit")
    
    dns >> waf >> alb
    
    alb >> api_service
    alb >> webapp_service
    
    api_service >> nat
    ecr >> api_service
    ecr >> webapp_service
    
    api_service >> Edge(color="purple") >> cognito
    api_service >> Edge(color="purple") >> secrets
    
    api_service >> Edge(color="brown") >> rds_primary
    rds_primary >> Edge(style="dashed") >> rds_replica
    api_service >> Edge(color="cyan") >> cache
    
    api_service >> Edge(color="gray") >> s3_docs
    rds_primary >> Edge(style="dashed") >> s3_backup
    
    api_service >> sns
    api_service >> ses
    api_service >> sqs
    
    kms >> rds_primary
    kms >> s3_docs
    kms >> s3_backup
    
    api_service >> Edge(color="yellow", style="dashed") >> cloudwatch
    cloudwatch >> s3_logs
    cloudtrail >> s3_logs
