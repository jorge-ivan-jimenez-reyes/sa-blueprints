
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.network import CloudFront, ALB, Route53
from diagrams.aws.storage import S3
from diagrams.onprem.client import Users
from diagrams.programming.framework import React
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

with Diagram(
    "IA Interactive - Front Office (Sitio Público)",
    filename="output",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    # Users
    users = Users("Visitantes\n(Clientes/Talentos)")
    
    # DNS
    dns = Route53("Route 53\nDNS")
    
    # CDN
    cdn = CloudFront("CloudFront\nCDN + Cache")
    
    # Load Balancer
    alb = ALB("ALB Público\n(Ingress)")
    
    # EKS Pod (single, low cost)
    with Cluster("Amazon EKS - Front Office"):
        with Cluster("Next.js (t3.small - $0.02/hr)"):
            pod1 = EKS("Pod Next.js\nSSR/SSG")
    
    # Static Assets
    s3 = S3("S3 Bucket\nStatic Assets")
    
    # Next.js Features
    with Cluster("Características Next.js"):
        ssr = Rack("SSR/SSG\nISR")
        i18n = Rack("i18n\n(ES/EN)")
        seo = Rack("SEO\nMeta Tags")
    
    # Analytics (Client-side)
    with Cluster("Analytics"):
        ga4 = Rack("Google\nAnalytics 4")
    
    # Flow
    users >> Edge(color="blue", style="bold", label="HTTPS") >> dns
    dns >> cdn
    cdn >> Edge(label="Cache Miss") >> alb
    cdn >> Edge(color="green", style="dashed", label="Cache Hit") >> users
    
    alb >> pod1
    
    pod1 >> Edge(style="dotted") >> s3
    
    pod1 >> Edge(color="purple", style="dashed") >> ssr
    pod1 >> Edge(color="purple", style="dashed") >> i18n
    pod1 >> Edge(color="purple", style="dashed") >> seo
    
    # Analytics connection (client-side)
    pod1 >> Edge(color="gray", style="dotted") >> ga4



