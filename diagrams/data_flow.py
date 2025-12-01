"""
IA Interactive - Diagrama de Flujo de Datos
============================================
Muestra cómo fluye la información entre los componentes

Ejecutar: python data_flow.py
Output: output/ia_interactive_data_flow.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users, Client
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.saas.cdn import Cloudflare

graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",
    "pad": "0.5",
}

with Diagram(
    "IA Interactive - Flujo de Datos",
    filename="output/ia_interactive_data_flow",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    
    # === FLUJO 1: Visitante consulta contenido ===
    with Cluster("1. Consulta de Contenido (Cache Hit)"):
        user1 = Users("Visitante")
        cf1 = Cloudflare("CDN Cache")
        
        user1 >> Edge(label="1. Request", color="blue") >> cf1
        cf1 >> Edge(label="2. Cached Response", color="green", style="bold") >> user1

    # === FLUJO 2: Contenido dinámico ===
    with Cluster("2. Contenido Dinámico (Cache Miss)"):
        user2 = Users("Visitante")
        cf2 = Cloudflare("CDN")
        next2 = Server("Next.js ISR")
        cache2 = Redis("Redis")
        db2 = PostgreSQL("PostgreSQL")
        
        user2 >> Edge(label="1", color="blue") >> cf2
        cf2 >> Edge(label="2", color="orange") >> next2
        next2 >> Edge(label="3", color="purple") >> cache2
        cache2 >> Edge(label="4 (miss)", color="red", style="dashed") >> next2
        next2 >> Edge(label="5", color="brown") >> db2
        db2 >> Edge(label="6", color="green") >> next2

    # === FLUJO 3: Envío de formulario ===
    with Cluster("3. Formulario de Contacto"):
        user3 = Users("Lead")
        form3 = Server("API Route")
        db3 = PostgreSQL("PostgreSQL")
        email3 = Rack("Resend API")
        
        user3 >> Edge(label="1. Submit", color="blue") >> form3
        form3 >> Edge(label="2. Save", color="brown") >> db3
        form3 >> Edge(label="3. Notify", color="orange") >> email3

    # === FLUJO 4: Administrador edita contenido ===
    with Cluster("4. Gestión de Contenido (Admin)"):
        admin4 = Client("Admin")
        cms4 = Server("Strapi CMS")
        db4 = PostgreSQL("PostgreSQL")
        blob4 = Storage("Blob Storage")
        cache4 = Redis("Invalidate")
        
        admin4 >> Edge(label="1. Edit", color="orange") >> cms4
        cms4 >> Edge(label="2. Save", color="brown") >> db4
        cms4 >> Edge(label="3. Upload", color="purple") >> blob4
        cms4 >> Edge(label="4. Invalidate", color="red") >> cache4


print("✅ Diagrama generado: output/ia_interactive_data_flow.png")

