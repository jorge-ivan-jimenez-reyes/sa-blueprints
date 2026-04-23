"""
Axis AI - Arquitectura de la Aplicacion
=======================================
Generador automatizado de BIA, DLP y DRP con IA.
Stack: Next.js 15 + TypeScript, Tailwind + shadcn/ui, React Context + localStorage, OpenAI GPT-4o.

Ejecutar: python diagram.py
Output: output.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.programming.language import Typescript
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.saas.cdn import Cloudflare

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.6",
    "ranksep": "1.2",
}

with Diagram(
    "Axis AI - Arquitectura de la Aplicacion",
    filename="output",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):

    # === USUARIO ===
    with Cluster("Usuario"):
        consultor = Users("Consultor\n(Navegador)")

    # === EDGE ===
    with Cluster("Edge / Hosting"):
        edge = Cloudflare("Vercel Edge\nHTTPS / SSL")

    # === CLIENTE (BROWSER) ===
    with Cluster("Cliente - Navegador Web"):

        with Cluster("UI (Tailwind + shadcn/ui)"):
            forms = Server("Next.js 15\nForms / SSR\n5 Modulos")

        with Cluster("Flujo Secuencial de Modulos"):
            m1 = Rack("1. Organizacion")
            m2 = Rack("2. BIA")
            m3 = Rack("3. DLP")
            m4 = Rack("4. DRP")
            m5 = Rack("5. Resumen\n& Validacion")
            m1 >> Edge(color="gray", style="dashed") >> m2
            m2 >> Edge(color="gray", style="dashed") >> m3
            m3 >> Edge(color="gray", style="dashed") >> m4
            m4 >> Edge(color="gray", style="dashed") >> m5

        with Cluster("Estado Global"):
            ctx = Typescript("useProjectStore\n(React Context)")
            ls = Storage("localStorage\n(Persistencia)")

        with Cluster("Motor Logico de Consistencia"):
            motor = Rack("Validacion Cruzada\nBIA <-> DLP <-> DRP")

    # === SERVIDOR NEXT.JS 15 ===
    with Cluster("Servidor - Next.js 15 (TypeScript)"):
        with Cluster("API Route /api/generate"):
            api = Server("Endpoint Unificado\n{ module, data }")

        with Cluster("Prompt Engineering"):
            sys_prompt = Rack("System Prompt\nRol Consultor Senior\n+ Restricciones")
            user_prompt = Rack("User Prompt\nJSON del estado\n+ Contexto real")

        with Cluster("Seguridad"):
            secrets = Rack("API Keys ocultas\n(.env / Server only)")

    # === IA EXTERNA ===
    with Cluster("Servicio de IA"):
        gpt = Rack("OpenAI API\nGPT-4o / GPT-5")

    # === OUTPUT ===
    with Cluster("Documentos Generados (Markdown)"):
        md_bia = Storage("BIA.md")
        md_dlp = Storage("DLP.md")
        md_drp = Storage("DRP.md")

    # === CONEXIONES ===

    # Usuario -> Edge -> Cliente
    consultor >> Edge(color="blue", style="bold", label="HTTPS") >> edge
    edge >> Edge(color="blue") >> forms

    # Forms <-> Modulos
    forms >> Edge(color="gray", style="dotted", label="guia al usuario") >> m1

    # Forms <-> Estado Global
    forms >> Edge(color="purple", label="captura datos") >> ctx
    ctx >> Edge(color="cyan", style="dashed", label="persist") >> ls

    # Resumen -> Motor -> Forms
    m5 >> Edge(color="red", label="audita") >> motor
    motor >> Edge(color="red", style="dashed", label="warnings") >> forms

    # Cliente -> Servidor
    ctx >> Edge(color="orange", style="bold", label="POST /api/generate") >> api

    # Servidor construye prompt
    api >> Edge(color="purple") >> sys_prompt
    api >> Edge(color="purple") >> user_prompt
    api >> Edge(color="gray", style="dashed") >> secrets

    # Servidor -> OpenAI
    sys_prompt >> Edge(color="green", style="bold", label="prompt maestro") >> gpt
    user_prompt >> Edge(color="green", style="bold") >> gpt

    # OpenAI -> Servidor -> Cliente
    gpt >> Edge(color="brown", style="bold", label="Markdown") >> api
    api >> Edge(color="brown", label="render") >> forms

    # Forms -> Documentos finales
    forms >> Edge(color="black", style="dashed") >> md_bia
    forms >> Edge(color="black", style="dashed") >> md_dlp
    forms >> Edge(color="black", style="dashed") >> md_drp
