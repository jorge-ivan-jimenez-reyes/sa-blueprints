
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users, Client
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.onprem.monitoring import Grafana
from diagrams.saas.cdn import Cloudflare
from diagrams.saas.analytics import Snowflake
from diagrams.programming.framework import React
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.custom import Custom

# Configuración del diagrama
graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

with Diagram(
    "IA Interactive - Arquitectura de Solución",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    
    # Usuarios finales
    with Cluster("Usuarios"):
        visitantes = Users("Visitantes\n(Clientes/Talentos)")
        admin = Client("Administradores")

    # Capa de Edge/CDN
    with Cluster("Edge Layer - Cloudflare"):
        cdn = Cloudflare("CDN + WAF\nDDoS Protection\nSSL/TLS")

    # Frontend - Sitio Público
    with Cluster("Frontend Layer - Vercel Edge"):
        with Cluster("Sitio Público"):
            nextjs = Server("Next.js 14\nSSG + ISR")
            static = Storage("Static Assets\n(Images, CSS, JS)")
        
        with Cluster("Panel Admin"):
            admin_app = Server("Admin Dashboard\n(Next.js)")

    # Backend / API Layer
    with Cluster("Backend Layer"):
        with Cluster("API Gateway"):
            api = Server("API Routes\n(Serverless)")
        
        with Cluster("CMS Headless"):
            cms = Server("Strapi CMS\n(Self-hosted)")
    
    # Servicios externos
    with Cluster("Servicios Externos"):
        with Cluster("Analytics"):
            ga4 = Rack("Google Analytics 4")
            hotjar = Rack("Hotjar\nHeatmaps")
        
        with Cluster("Comunicación"):
            email = Rack("Resend\n(Email API)")
            calendar = Rack("Cal.com\n(Scheduling)")
        
        with Cluster("Integraciones"):
            linkedin = Rack("LinkedIn API")
            social = Rack("Social Media")

    # Base de datos
    with Cluster("Data Layer"):
        with Cluster("Database"):
            db = PostgreSQL("PostgreSQL\n(Supabase/Railway)")
        
        with Cluster("Cache"):
            cache = Redis("Redis Cache\n(Upstash)")
        
        with Cluster("Storage"):
            blob = Storage("Blob Storage\n(Cloudflare R2)")

    # CI/CD y Monitoreo
    with Cluster("DevOps"):
        with Cluster("CI/CD"):
            github = Github("GitHub\nActions")
        
        with Cluster("Monitoring"):
            monitoring = Grafana("Vercel Analytics\n+ Sentry")

    # Conexiones principales
    # Usuarios -> CDN
    visitantes >> Edge(color="blue", style="bold") >> cdn
    admin >> Edge(color="orange", style="bold") >> cdn
    
    # CDN -> Frontend
    cdn >> Edge(color="green") >> nextjs
    cdn >> Edge(color="green") >> admin_app
    
    # Frontend -> Backend
    nextjs >> Edge(color="purple") >> api
    admin_app >> Edge(color="purple") >> api
    nextjs >> Edge(color="gray", style="dashed") >> static
    
    # API -> CMS
    api >> Edge(color="red") >> cms
    
    # Backend -> Data
    cms >> Edge(color="brown") >> db
    api >> Edge(color="brown") >> db
    api >> Edge(color="cyan") >> cache
    cms >> Edge(color="gray") >> blob
    
    # Servicios externos
    api >> Edge(color="gray", style="dashed") >> email
    api >> Edge(color="gray", style="dashed") >> calendar
    api >> Edge(color="gray", style="dashed") >> linkedin
    
    # Analytics (client-side)
    nextjs >> Edge(color="gray", style="dotted") >> ga4
    nextjs >> Edge(color="gray", style="dotted") >> hotjar
    
    # DevOps
    github >> Edge(color="green", style="dashed") >> nextjs
    github >> Edge(color="green", style="dashed") >> cms
    monitoring >> Edge(color="yellow", style="dotted") >> nextjs
    monitoring >> Edge(color="yellow", style="dotted") >> api



