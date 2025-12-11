
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.management import Cloudwatch, CloudwatchAlarm
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.logging import Loki
from diagrams.onprem.tracing import Jaeger
from diagrams.generic.network import VPN
from diagrams.onprem.client import Client
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

with Diagram(
    "IA Interactive - Observability Stack",
    filename="output",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    # Operators
    ops = Client("Equipo DevOps\n/ SRE")
    vpn = VPN("Tailscale\nVPN")
    
    # Sources
    with Cluster("Fuentes de Datos"):
        with Cluster("Application Pods"):
            front = EKS("Front Office")
            back = EKS("Back Office")
            backend = EKS("Backend API")
    
    # EKS Observability Namespace
    with Cluster("Amazon EKS - Namespace: observability"):
        
        with Cluster("Metrics"):
            prometheus = Prometheus("Prometheus\nMetrics Collection")
            alertmanager = Rack("Alertmanager\nAlert Routing")
        
        with Cluster("Visualization"):
            grafana = Grafana("Grafana\nDashboards")
        
        with Cluster("Logging (Optional)"):
            loki = Loki("Loki\nLog Aggregation")
    
    # AWS Native
    with Cluster("AWS Native Observability"):
        cloudwatch = Cloudwatch("CloudWatch\nLogs & Metrics")
        alarms = CloudwatchAlarm("CloudWatch\nAlarms")
    
    # Dashboards
    with Cluster("Dashboards Disponibles"):
        dash_infra = Rack("Infraestructura\nCPU/Memory/Network")
        dash_app = Rack("Aplicación\nLatency/Errors/Throughput")
        dash_biz = Rack("Negocio\nLeads/Conversiones/Visitas")
        dash_k8s = Rack("Kubernetes\nPods/Nodes/HPA")
    
    # Alerts
    with Cluster("Alertas Configuradas"):
        alert_cpu = Rack("High CPU\n> 80%")
        alert_mem = Rack("High Memory\n> 80%")
        alert_error = Rack("Error Rate\n> 1%")
        alert_latency = Rack("High Latency\n> 500ms")
        alert_pod = Rack("Pod Restart\n/ Crash")
    
    # Notification Channels
    with Cluster("Canales de Notificación"):
        slack = Rack("Slack")
        email = Rack("Email")
        pagerduty = Rack("PagerDuty\n(Optional)")
    
    # Connections
    ops >> Edge(color="orange", style="bold") >> vpn
    vpn >> Edge(color="orange") >> grafana
    
    front >> Edge(color="yellow", label="/metrics") >> prometheus
    back >> Edge(color="yellow") >> prometheus
    backend >> Edge(color="yellow") >> prometheus
    
    front >> Edge(color="blue", style="dashed") >> cloudwatch
    back >> Edge(color="blue", style="dashed") >> cloudwatch
    backend >> Edge(color="blue", style="dashed") >> cloudwatch
    
    prometheus >> Edge(color="green") >> grafana
    prometheus >> Edge(color="red") >> alertmanager
    cloudwatch >> Edge(color="red") >> alarms
    
    loki >> Edge(color="purple") >> grafana
    
    grafana >> Edge(style="dotted") >> dash_infra
    grafana >> Edge(style="dotted") >> dash_app
    grafana >> Edge(style="dotted") >> dash_biz
    grafana >> Edge(style="dotted") >> dash_k8s
    
    alertmanager >> Edge(color="red") >> alert_cpu
    alertmanager >> Edge(color="red") >> alert_mem
    alertmanager >> Edge(color="red") >> alert_error
    alertmanager >> Edge(color="red") >> alert_latency
    alertmanager >> Edge(color="red") >> alert_pod
    
    alertmanager >> Edge(color="red", style="bold") >> slack
    alertmanager >> Edge(color="red", style="bold") >> email
    alarms >> Edge(color="red", style="bold") >> pagerduty



