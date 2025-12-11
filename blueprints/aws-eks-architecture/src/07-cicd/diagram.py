
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.compute import ECR
from diagrams.aws.devtools import Codebuild
from diagrams.onprem.vcs import Github
from diagrams.onprem.gitops import Argocd
from diagrams.onprem.ci import GithubActions
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

with Diagram(
    "IA Interactive - CI/CD Pipeline",
    filename="output",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    # Developer
    dev = Rack("Developer\nPush Code")
    
    # Source Control
    with Cluster("GitHub Repositories"):
        repo_app = Github("App Repo\n(Source Code)")
        repo_infra = Github("Infra Repo\n(Terraform)")
        repo_k8s = Github("K8s Manifests\n(Helm/Kustomize)")
    
    # CI Pipeline
    with Cluster("CI - GitHub Actions"):
        with Cluster("App Pipeline"):
            lint = GithubActions("Lint &\nFormat")
            test = GithubActions("Unit\nTests")
            build = GithubActions("Docker\nBuild")
            push = GithubActions("Push to\nECR")
            update_manifest = GithubActions("Update\nManifests")
        
        with Cluster("Infra Pipeline"):
            tf_init = Rack("terraform\ninit")
            tf_plan = Rack("terraform\nplan")
            tf_apply = Rack("terraform\napply")
    
    # Artifacts
    ecr = ECR("Amazon ECR\nContainer Registry")
    
    # CD Pipeline
    with Cluster("CD - GitOps"):
        argocd = Argocd("Argo CD\nController")
        
        with Cluster("Sync Status"):
            sync = Rack("Auto Sync\nEnabled")
            health = Rack("Health\nChecks")
    
    # Target Environments
    with Cluster("Amazon EKS Environments"):
        with Cluster("Dev"):
            eks_dev = EKS("EKS Dev")
        with Cluster("Stage"):
            eks_stage = EKS("EKS Stage")
        with Cluster("Prod"):
            eks_prod = EKS("EKS Prod")
    
    # Terraform State
    tf_state = Storage("S3\nTerraform State")
    
    # Flow - App Pipeline
    dev >> Edge(color="blue", label="git push") >> repo_app
    repo_app >> Edge(color="green", label="trigger") >> lint
    lint >> test >> build >> push
    push >> Edge(color="green") >> ecr
    push >> Edge(color="purple", label="bump version") >> update_manifest
    update_manifest >> Edge(color="purple") >> repo_k8s
    
    # Flow - Infra Pipeline
    dev >> Edge(color="orange", style="dashed") >> repo_infra
    repo_infra >> tf_init >> tf_plan >> tf_apply
    tf_apply >> Edge(style="dashed") >> tf_state
    
    # Flow - GitOps
    repo_k8s >> Edge(color="red", label="watch") >> argocd
    ecr >> Edge(color="red", style="dashed") >> argocd
    argocd >> sync
    argocd >> health
    
    argocd >> Edge(color="red", label="deploy") >> eks_dev
    argocd >> Edge(color="red") >> eks_stage
    argocd >> Edge(color="red") >> eks_prod



