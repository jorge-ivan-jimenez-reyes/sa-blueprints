"""
IA Interactive - Back Office Architecture
==========================================
Diagrama del panel de administración

Ejecutar: python 03_back_office.py
Output: output/03_back_office.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.network import ALB
from diagrams.onprem.client import Client
from diagrams.generic.network import VPN
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

with Diagram(
    "IA Interactive - Back Office (Panel Admin)",
    filename="output/03_back_office",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    # Internal Users
    operators = Client("Equipo Interno\n(Marketing, Contenido, HR)")
    
    # VPN Access
    vpn = VPN("Tailscale VPN\n(Zero Trust)")
    
    # Internal VPC
    with Cluster("AWS VPC (Private)"):
        # Internal Load Balancer
        alb = ALB("ALB Interno\n(No público)")
        
        # EKS - Single Pod (low cost)
        with Cluster("Amazon EKS - Back Office"):
            with Cluster("Admin Dashboard (t3.small - $0.02/hr)"):
                admin_pod = EKS("Pod Admin\nNext.js")
    
    # Modules/Features
    with Cluster("Módulos del Admin"):
        mod_clientes = Rack("Clientes\ny Leads")
        mod_contenido = Rack("Contenido\ny Servicios")
        mod_carreras = Rack("Carreras\ny Vacantes")
        mod_metricas = Rack("Métricas\ny Reportes")
    
    # Flow
    operators >> Edge(color="orange", style="bold", label="VPN Tunnel") >> vpn
    vpn >> Edge(color="orange", label="Private Access") >> alb
    
    alb >> admin_pod
    
    admin_pod >> Edge(color="purple", style="dashed") >> mod_clientes
    admin_pod >> Edge(color="purple", style="dashed") >> mod_contenido
    admin_pod >> Edge(color="purple", style="dashed") >> mod_carreras
    admin_pod >> Edge(color="purple", style="dashed") >> mod_metricas


print("✅ Diagrama generado: output/03_back_office.png")
