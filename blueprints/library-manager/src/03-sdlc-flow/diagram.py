
from diagrams import Diagram, Cluster, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.generic.blank import Blank

# Configuración para LaTeX - horizontal y compacto
graph_attr = {
    "fontsize": "12",
    "bgcolor": "white",
    "pad": "0.3",
    "splines": "ortho",
    "nodesep": "0.6",
    "ranksep": "0.8",
    "dpi": "120",
}

with Diagram(
    "LibraryManager - Flujo SDLC",
    filename="output",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    # TESTING
    with Cluster("TESTING", graph_attr={"bgcolor": "#E3F2FD", "fontcolor": "#1565C0"}):
        t1 = Rack("Unit\nTesting")
        t2 = Rack("Integration\nTesting")
        t3 = Rack("UAT")
    
    # DEPLOYMENT
    with Cluster("DEPLOYMENT", graph_attr={"bgcolor": "#E8F5E9", "fontcolor": "#2E7D32"}):
        d1 = Rack("Blue-Green\nStrategy")
        d2 = Rack("Zero\nDowntime")
        d3 = Rack("Rollback\nReady")
    
    # MAINTENANCE
    with Cluster("MAINTENANCE", graph_attr={"bgcolor": "#FFF3E0", "fontcolor": "#E65100"}):
        m1 = Rack("Correctivo")
        m2 = Rack("Perfectivo")
        m3 = Rack("Preventivo")
    
    # SSDLC (Security)
    with Cluster("SSDLC", graph_attr={"bgcolor": "#FCE4EC", "fontcolor": "#C2185B"}):
        s1 = Rack("Confidentiality")
        s2 = Rack("Integrity")
        s3 = Rack("Availability")
    
    # Flujo principal entre fases
    t3 >> Edge(color="blue", style="bold", label="validado") >> d1
    d3 >> Edge(color="green", style="bold", label="desplegado") >> m1
    m3 >> Edge(color="orange", style="bold", label="actualizado") >> s1
    
    # Conexión interna de cada fase
    t1 >> t2 >> t3
    d1 >> d2 >> d3
    m1 >> m2 >> m3
    s1 >> s2 >> s3




