"""
LibraryManager - Blue-Green Deployment (Versión Compacta)
=========================================================
Diagrama simplificado para documentos LaTeX.

Ejecutar: python blue_green_simple.py
Output: output/blue_green_simple.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.network import Haproxy
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.vcs import Github
from diagrams.generic.compute import Rack

# Configuración compacta - dimensiones pequeñas para LaTeX
graph_attr = {
    "fontsize": "11",
    "bgcolor": "white",
    "pad": "0.2",
    "splines": "spline",
    "nodesep": "0.5",
    "ranksep": "0.5",
    "dpi": "100",
    "size": "8,6!",  # ~800x600 px aprox
}

with Diagram(
    "LibraryManager - Blue-Green Deployment",
    filename="output/blue_green_simple",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    # Usuarios y CI/CD en la parte superior
    users = Users("Usuarios")
    
    with Cluster("CI/CD"):
        github = Github("GitHub\nActions")
    
    # Load Balancer central
    lb = Haproxy("Load Balancer\n(Switch)")
    
    # Entornos Blue y Green lado a lado
    with Cluster("BLUE (v1.0) - PRODUCCIÓN", graph_attr={"bgcolor": "#BBDEFB", "fontcolor": "#1565C0"}):
        blue_app = Server("App Blue")
        blue_svc = Rack("Services")
    
    with Cluster("GREEN (v1.1) - STAGING", graph_attr={"bgcolor": "#C8E6C9", "fontcolor": "#2E7D32"}):
        green_app = Server("App Green")
        green_svc = Rack("Services")
    
    # Base de datos compartida
    with Cluster("Shared Database"):
        db = PostgreSQL("PostgreSQL")
    
    # Conexiones
    users >> Edge(color="blue", style="bold", label="HTTPS") >> lb
    
    # Blue recibe tráfico (activo)
    lb >> Edge(color="blue", style="bold", label="100%") >> blue_app
    blue_app >> blue_svc
    blue_svc >> Edge(color="brown") >> db
    
    # Green en standby (dashed)
    lb >> Edge(color="green", style="dashed", label="0%") >> green_app
    green_app >> green_svc
    green_svc >> Edge(color="brown", style="dashed") >> db
    
    # CI/CD despliega a Green
    github >> Edge(color="gray", style="dashed", label="deploy") >> green_app


print("✅ Diagrama compacto generado: output/blue_green_simple.png")
