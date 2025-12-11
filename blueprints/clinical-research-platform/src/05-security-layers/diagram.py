from diagrams import Diagram, Cluster, Edge
from diagrams.aws.security import WAF, Cognito, IAM, SecretsManager, KMS, Shield
from diagrams.aws.network import VPC
from diagrams.aws.management import Cloudtrail
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.generic.compute import Rack
from diagrams.onprem.client import Users

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "0.6",
}

with Diagram(
    "Clinical Research - Security Layers (HIPAA Compliance)",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    users = Users("Usuarios")
    
    with Cluster("Layer 1: Edge Security"):
        shield = Shield("AWS Shield\nDDoS Protection")
        waf = WAF("AWS WAF\nWeb Firewall")
        ssl = Rack("SSL/TLS\nEncryption")
    
    with Cluster("Layer 2: Authentication & Authorization"):
        cognito = Cognito("AWS Cognito\nMFA/2FA")
        iam = IAM("IAM\nRole-Based Access")
        rbac = Rack("RBAC\nPermisos por Rol")
    
    with Cluster("Layer 3: Network Security"):
        vpc = VPC("VPC\nIsolation")
        private = Rack("Private Subnets\nNo Public Access")
        sg = Rack("Security Groups\nFirewall Rules")
    
    with Cluster("Layer 4: Application Security"):
        validation = Rack("Input Validation\nSanitization")
        session = Rack("Session Management\nToken Expiry")
        secrets = SecretsManager("Secrets Manager\nCredentials")
    
    with Cluster("Layer 5: Data Security"):
        kms = KMS("KMS\nEncryption Keys")
        rds = RDS("RDS Encrypted\nAt Rest")
        s3 = S3("S3 Encrypted\nAt Rest")
    
    with Cluster("Layer 6: Audit & Compliance"):
        cloudtrail = Cloudtrail("CloudTrail\nAudit Logs")
        audit = Rack("Audit Trail\nChange History")
        hipaa = Rack("HIPAA\nCompliance")
    
    users >> Edge(color="blue", style="bold") >> shield
    shield >> waf >> ssl
    
    ssl >> Edge(color="purple") >> cognito
    cognito >> iam >> rbac
    
    rbac >> Edge(color="green") >> vpc
    vpc >> private >> sg
    
    sg >> Edge(color="orange") >> validation
    validation >> session >> secrets
    
    secrets >> Edge(color="red") >> kms
    kms >> rds
    kms >> s3
    
    rds >> Edge(color="gray", style="dashed") >> cloudtrail
    s3 >> Edge(color="gray", style="dashed") >> cloudtrail
    cloudtrail >> audit >> hipaa
