from diagrams import Diagram, Cluster, Edge
from diagrams.aws.security import Cognito
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.6",
    "ranksep": "0.8",
}

with Diagram(
    "Clinical Research - WebApp (Investigadores)",
    filename="output",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    researcher = Client("Investigador\nBrowser")
    
    with Cluster("WebApp React"):
        
        with Cluster("Seguridad"):
            login = Rack("Login\nEmail Institucional")
            mfa = Rack("2FA/MFA\nAutenticacion")
            roles = Rack("Gestion\nRoles")
        
        with Cluster("Dashboard"):
            kpis = Rack("KPIs\nMetricas")
            alerts = Rack("Alertas\nEventos")
        
        with Cluster("Gestion"):
            protocols = Rack("Protocolos\nCRFs")
            participants = Rack("Participantes\nEnrolamiento")
            visits = Rack("Visitas\nCronograma")
            forms = Rack("Formularios\nRecoleccion")
        
        with Cluster("Compliance"):
            adverse = Rack("Eventos\nAdversos")
            audit = Rack("Auditoria\nHistorial")
            reports = Rack("Reportes\nExport")
    
    with Cluster("Backend"):
        api = Server("API\nBackend")
        cognito = Cognito("Cognito\n2FA")
        db = RDS("PostgreSQL\nHIPAA")
        storage = S3("S3\nDocumentos")
    
    researcher >> Edge(color="orange", style="bold") >> login
    login >> mfa >> roles
    
    mfa >> Edge(color="purple") >> cognito
    
    roles >> kpis
    roles >> alerts
    
    kpis >> protocols
    protocols >> participants
    participants >> visits
    visits >> forms
    
    forms >> adverse
    adverse >> audit
    audit >> reports
    
    protocols >> Edge(color="green") >> api
    participants >> Edge(color="green") >> api
    visits >> Edge(color="green") >> api
    forms >> Edge(color="green") >> api
    adverse >> Edge(color="green") >> api
    
    api >> Edge(color="brown") >> db
    api >> Edge(color="gray") >> storage
    
    reports >> Edge(color="cyan", label="CSV/Excel") >> storage
