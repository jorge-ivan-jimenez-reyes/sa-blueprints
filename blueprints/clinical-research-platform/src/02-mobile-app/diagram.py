from diagrams import Diagram, Cluster, Edge
from diagrams.aws.security import Cognito
from diagrams.aws.integration import SNS
from diagrams.aws.storage import S3
from diagrams.onprem.compute import Server
from diagrams.generic.device import Mobile
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
    "Clinical Research - Mobile App (Participantes)",
    filename="output",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    participant = Mobile("Participante\niOS/Android")
    
    with Cluster("React Native App"):
        
        with Cluster("Seguridad"):
            login = Rack("Login\nEmail + Password")
            biometric = Rack("Biometricos\nHuella/Face ID")
            token_auth = Rack("Token\nActivacion")
        
        with Cluster("Funciones Principales"):
            dashboard = Rack("Dashboard\nEstado del Estudio")
            calendar = Rack("Calendario\nVisitas")
            consent = Rack("Consentimiento\nFirma Digital")
            surveys = Rack("Encuestas\nFormularios")
            messages = Rack("Mensajes\nChat Seguro")
            docs = Rack("Documentos\nPersonales")
            profile = Rack("Perfil\nConfiguracion")
    
    with Cluster("Backend Services"):
        api = Server("API\nBackend")
        cognito = Cognito("Cognito\nAuth")
        push = SNS("Push\nNotifications")
        storage = S3("S3\nDocumentos")
    
    participant >> Edge(color="blue", style="bold") >> login
    login >> biometric
    login >> token_auth
    
    login >> Edge(color="purple") >> cognito
    
    token_auth >> dashboard
    dashboard >> calendar
    dashboard >> consent
    dashboard >> surveys
    dashboard >> messages
    dashboard >> docs
    dashboard >> profile
    
    calendar >> Edge(color="green") >> api
    consent >> Edge(color="green") >> api
    surveys >> Edge(color="green") >> api
    messages >> Edge(color="green") >> api
    
    api >> push
    consent >> Edge(color="gray") >> storage
    docs >> Edge(color="gray") >> storage
