
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.security import Vault
from diagrams.saas.cdn import Cloudflare
from diagrams.generic.network import Firewall

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
}

with Diagram(
    "IA Interactive - Capas de Seguridad",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    
    users = Users("Internet Users")
    
    with Cluster("Capa 1: Edge Security"):
        with Cluster("Cloudflare"):
            ddos = Firewall("DDoS Protection")
            waf = Firewall("WAF Rules")
            ssl = Vault("SSL/TLS\nEncryption")
            bot = Firewall("Bot Protection")
    
    with Cluster("Capa 2: Application Security"):
        with Cluster("Vercel"):
            headers = Server("Security Headers\nCSP, HSTS, X-Frame")
            rate = Firewall("Rate Limiting")
            auth = Vault("Auth0/NextAuth\nOAuth 2.0 + OIDC")
    
    with Cluster("Capa 3: API Security"):
        with Cluster("Backend"):
            validation = Server("Input Validation\nZod/Yup")
            sanitize = Server("Data Sanitization\nXSS Prevention")
            cors = Firewall("CORS Policy")
    
    with Cluster("Capa 4: Data Security"):
        with Cluster("Database"):
            encrypt = Vault("Encryption at Rest\nAES-256")
            backup = Vault("Automated Backups")
            access = Firewall("Row Level Security\nRLS")
    
    # Conexiones
    users >> Edge(color="red") >> ddos
    ddos >> waf >> ssl >> bot
    bot >> Edge(color="orange") >> headers
    headers >> rate >> auth
    auth >> Edge(color="yellow") >> validation
    validation >> sanitize >> cors
    cors >> Edge(color="green") >> encrypt
    encrypt >> backup >> access



