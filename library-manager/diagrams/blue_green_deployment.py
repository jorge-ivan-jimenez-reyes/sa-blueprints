"""
LibraryManager - Blue-Green Deployment Strategy
================================================
Diagrama de estrategia de despliegue Blue-Green para el sistema
de gestión de biblioteca.

Ejecutar: python blue_green_deployment.py
Output: output/blue_green_deployment.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.network import Nginx, Haproxy
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.vcs import Github
from diagrams.onprem.ci import GithubActions
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.generic.network import Switch

# Configuración del diagrama - Versión compacta
graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.3",
    "splines": "spline",
    "rankdir": "LR",  # Left to Right para más compacto
    "nodesep": "0.3",
    "ranksep": "0.4",
    "dpi": "150",
}

cluster_attr = {
    "fontsize": "11",
    "bgcolor": "lightgray",
}

with Diagram(
    "LibraryManager - Blue-Green Deployment",
    filename="output/blue_green_deployment",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    # Usuarios
    users = Users("Bibliotecarios\n& Usuarios")
    
    # CI/CD Pipeline
    with Cluster("CI/CD Pipeline"):
        repo = Github("GitHub\nRepository")
        ci = GithubActions("GitHub Actions\nBuild & Test")
        artifacts = Storage("Docker\nArtifacts")
    
    # Load Balancer / Router
    with Cluster("Traffic Management"):
        dns = Rack("DNS\nlibrarymanager.edu")
        lb = Haproxy("Load Balancer\n(HAProxy/Nginx)")
        health = Rack("Health\nChecks")
    
    # Blue Environment (Production)
    with Cluster("BLUE Environment (v1.0 - LIVE)", graph_attr={"bgcolor": "#E3F2FD", "fontcolor": "#1565C0"}):
        with Cluster("Application Servers"):
            blue_app1 = Server("App Server 1\n(Blue)")
            blue_app2 = Server("App Server 2\n(Blue)")
        
        with Cluster("Services"):
            blue_catalog = Rack("Catálogo\nService")
            blue_loans = Rack("Préstamos\nService")
            blue_users = Rack("Usuarios\nService")
    
    # Green Environment (Staging/New Version)
    with Cluster("GREEN Environment (v1.1 - IDLE)", graph_attr={"bgcolor": "#E8F5E9", "fontcolor": "#2E7D32"}):
        with Cluster("Application Servers"):
            green_app1 = Server("App Server 1\n(Green)")
            green_app2 = Server("App Server 2\n(Green)")
        
        with Cluster("Services"):
            green_catalog = Rack("Catálogo\nService")
            green_loans = Rack("Préstamos\nService")
            green_users = Rack("Usuarios\nService")
    
    # Shared Infrastructure
    with Cluster("Shared Infrastructure", graph_attr={"bgcolor": "#FFF3E0"}):
        with Cluster("Database Layer"):
            db_primary = PostgreSQL("PostgreSQL\nPrimary")
            db_replica = PostgreSQL("PostgreSQL\nReplica")
        
        with Cluster("Cache Layer"):
            cache = Redis("Redis\nSession Cache")
        
        with Cluster("File Storage"):
            storage = Storage("Libros Digitales\n& Archivos")
    
    # Monitoring
    with Cluster("Observability"):
        prometheus = Prometheus("Prometheus\nMetrics")
        grafana = Grafana("Grafana\nDashboards")
        alerts = Rack("Alertas\n& Rollback")
    
    # === CONEXIONES ===
    
    # CI/CD Flow
    repo >> Edge(color="gray", label="push") >> ci
    ci >> Edge(color="gray", label="build") >> artifacts
    artifacts >> Edge(color="green", style="dashed", label="deploy v1.1") >> green_app1
    artifacts >> Edge(color="green", style="dashed") >> green_app2
    
    # User Traffic Flow
    users >> Edge(color="blue", style="bold", label="HTTPS") >> dns
    dns >> Edge(color="blue", style="bold") >> lb
    
    # Load Balancer to Blue (ACTIVE)
    lb >> Edge(color="blue", style="bold", label="100% traffic") >> blue_app1
    lb >> Edge(color="blue", style="bold") >> blue_app2
    
    # Load Balancer to Green (STANDBY - dashed)
    lb >> Edge(color="green", style="dashed", label="0% traffic\n(ready to switch)") >> green_app1
    lb >> Edge(color="green", style="dashed") >> green_app2
    
    # Health Checks
    lb >> Edge(color="orange", style="dotted") >> health
    health >> Edge(color="orange", style="dotted") >> blue_app1
    health >> Edge(color="orange", style="dotted") >> green_app1
    
    # Blue Services
    blue_app1 >> Edge(color="blue") >> blue_catalog
    blue_app1 >> Edge(color="blue") >> blue_loans
    blue_app1 >> Edge(color="blue") >> blue_users
    
    # Green Services
    green_app1 >> Edge(color="green") >> green_catalog
    green_app1 >> Edge(color="green") >> green_loans
    green_app1 >> Edge(color="green") >> green_users
    
    # Database connections
    blue_catalog >> Edge(color="brown") >> db_primary
    blue_loans >> Edge(color="brown") >> db_primary
    blue_users >> Edge(color="brown") >> db_primary
    
    green_catalog >> Edge(color="brown", style="dashed") >> db_primary
    green_loans >> Edge(color="brown", style="dashed") >> db_primary
    green_users >> Edge(color="brown", style="dashed") >> db_primary
    
    # Database replication
    db_primary >> Edge(color="red", style="dotted", label="replication") >> db_replica
    
    # Cache connections
    blue_users >> Edge(color="cyan") >> cache
    green_users >> Edge(color="cyan", style="dashed") >> cache
    
    # Storage connections
    blue_catalog >> Edge(color="gray") >> storage
    green_catalog >> Edge(color="gray", style="dashed") >> storage
    
    # Monitoring
    prometheus >> Edge(color="purple", style="dotted") >> blue_app1
    prometheus >> Edge(color="purple", style="dotted") >> green_app1
    prometheus >> Edge(color="purple", style="dotted") >> db_primary
    prometheus >> Edge(color="yellow") >> grafana
    grafana >> Edge(color="red", style="bold", label="trigger") >> alerts
    alerts >> Edge(color="red", style="dashed", label="auto-rollback") >> lb


print("✅ Diagrama generado: output/blue_green_deployment.png")
print("")
print("📋 Estrategia Blue-Green:")
print("   1. Blue (v1.0) recibe 100% del tráfico (PRODUCCIÓN)")
print("   2. Green (v1.1) está listo pero sin tráfico (STAGING)")
print("   3. Después de validar Green, el Load Balancer hace el SWITCH")
print("   4. Si hay problemas, rollback instantáneo a Blue")
