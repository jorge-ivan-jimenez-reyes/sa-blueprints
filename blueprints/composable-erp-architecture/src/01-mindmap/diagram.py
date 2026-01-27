"""
Composable ERP Architecture - Mind Map
======================================
Mapa mental de arquitectura ERP modular, escalable y basada en eventos.

Ejecutar: python diagram.py
Output: output.png
"""

from graphviz import Graph

# Crear grafo no dirigido (mapa mental)
g = Graph(
    'mindmap',
    filename='output',
    format='png',
    engine='neato',  # Layout radial para mapa mental
    graph_attr={
        'bgcolor': 'white',
        'dpi': '150',
        'overlap': 'false',
        'splines': 'true',
        'sep': '+15',
    },
    node_attr={
        'fontname': 'Helvetica',
        'fontsize': '11',
        'style': 'filled,rounded',
        'shape': 'box',
    },
    edge_attr={
        'penwidth': '2',
    }
)

# ===========================================
# NODO CENTRAL
# ===========================================
g.node('center', 'Composable\nERP\nArchitecture', 
       shape='ellipse',
       style='filled,bold',
       fillcolor='#1976D2',
       fontcolor='white',
       fontsize='16',
       width='2',
       height='1.2')

# ===========================================
# RAMA 1: CORE ARCHITECTURE (Azul)
# ===========================================
BLUE = '#E3F2FD'
BLUE_DARK = '#1565C0'

g.node('core', 'Core\nArchitecture', fillcolor=BLUE, fontcolor=BLUE_DARK, fontsize='13')
g.edge('center', 'core', color=BLUE_DARK, penwidth='3')

# Sub-nodos Core
g.node('container', 'Containerization\n• Docker\n• Kubernetes', fillcolor=BLUE, fontcolor=BLUE_DARK)
g.node('serverless', 'Serverless\nComputing\n• No infra mgmt\n• Pay-per-use', fillcolor=BLUE, fontcolor=BLUE_DARK)
g.node('eda', 'Event-Driven\nArchitecture\n• Loose coupling\n• Independent scaling', fillcolor=BLUE, fontcolor=BLUE_DARK)

g.edge('core', 'container', color=BLUE_DARK)
g.edge('core', 'serverless', color=BLUE_DARK)
g.edge('core', 'eda', color=BLUE_DARK)

# ===========================================
# RAMA 2: BENEFITS (Verde)
# ===========================================
GREEN = '#E8F5E9'
GREEN_DARK = '#2E7D32'

g.node('benefits', 'Benefits', fillcolor=GREEN, fontcolor=GREEN_DARK, fontsize='13')
g.edge('center', 'benefits', color=GREEN_DARK, penwidth='3')

# Sub-nodos Benefits
g.node('agility', 'Business\nAgility\n• Rapid adaptation\n• Flexibility', fillcolor=GREEN, fontcolor=GREEN_DARK)
g.node('scalability', 'Scalability &\nPerformance\n• Dynamic scaling\n• Low latency', fillcolor=GREEN, fontcolor=GREEN_DARK)
g.node('innovation', 'Innovation\n• AI integration\n• Faster cycles', fillcolor=GREEN, fontcolor=GREEN_DARK)
g.node('cost', 'Cost\nOptimization\n• Best-of-breed\n• Right-sized', fillcolor=GREEN, fontcolor=GREEN_DARK)
g.node('risk', 'Risk\nMitigation\n• No vendor lock-in\n• Resilience', fillcolor=GREEN, fontcolor=GREEN_DARK)

g.edge('benefits', 'agility', color=GREEN_DARK)
g.edge('benefits', 'scalability', color=GREEN_DARK)
g.edge('benefits', 'innovation', color=GREEN_DARK)
g.edge('benefits', 'cost', color=GREEN_DARK)
g.edge('benefits', 'risk', color=GREEN_DARK)

# ===========================================
# RAMA 3: CHALLENGES (Naranja)
# ===========================================
ORANGE = '#FFF3E0'
ORANGE_DARK = '#E65100'

g.node('challenges', 'Implementation\nChallenges', fillcolor=ORANGE, fontcolor=ORANGE_DARK, fontsize='13')
g.edge('center', 'challenges', color=ORANGE_DARK, penwidth='3')

# Sub-nodos Challenges
g.node('governance', 'Architectural\nGovernance\n• Standards\n• Service registry', fillcolor=ORANGE, fontcolor=ORANGE_DARK)
g.node('security', 'Security &\nCompliance\n• RBAC\n• Unified access', fillcolor=ORANGE, fontcolor=ORANGE_DARK)
g.node('data', 'Data\nManagement\n• MDM\n• Consistency', fillcolor=ORANGE, fontcolor=ORANGE_DARK)

g.edge('challenges', 'governance', color=ORANGE_DARK)
g.edge('challenges', 'security', color=ORANGE_DARK)
g.edge('challenges', 'data', color=ORANGE_DARK)

# ===========================================
# RAMA 4: INDUSTRY APPLICATIONS (Púrpura)
# ===========================================
PURPLE = '#F3E5F5'
PURPLE_DARK = '#7B1FA2'

g.node('industry', 'Industry\nApplications', fillcolor=PURPLE, fontcolor=PURPLE_DARK, fontsize='13')
g.edge('center', 'industry', color=PURPLE_DARK, penwidth='3')

# Sub-nodos Industry
g.node('retail', 'Retail &\nE-Commerce\n• Coca-Cola\n• Adidas\n• TechStyle', fillcolor=PURPLE, fontcolor=PURPLE_DARK)
g.node('healthcare', 'Healthcare\n• 22% cost reduction\n• Better patient care', fillcolor=PURPLE, fontcolor=PURPLE_DARK)

g.edge('industry', 'retail', color=PURPLE_DARK)
g.edge('industry', 'healthcare', color=PURPLE_DARK)

# ===========================================
# RAMA 5: FUTURE TRENDS (Cyan)
# ===========================================
CYAN = '#E0F7FA'
CYAN_DARK = '#00838F'

g.node('future', 'Future\nTrends', fillcolor=CYAN, fontcolor=CYAN_DARK, fontsize='13')
g.edge('center', 'future', color=CYAN_DARK, penwidth='3')

# Sub-nodos Future
g.node('ai', 'AI & ML\n• Process optimization\n• Autonomous decisions', fillcolor=CYAN, fontcolor=CYAN_DARK)
g.node('ecosystem', 'Extended\nEcosystem\n• Marketplaces\n• Partners', fillcolor=CYAN, fontcolor=CYAN_DARK)
g.node('lowcode', 'Low-Code /\nNo-Code\n• Fast customization\n• Citizen developers', fillcolor=CYAN, fontcolor=CYAN_DARK)
g.node('ethics', 'Ethical\nConsiderations\n• Fairness\n• Data privacy', fillcolor=CYAN, fontcolor=CYAN_DARK)

g.edge('future', 'ai', color=CYAN_DARK)
g.edge('future', 'ecosystem', color=CYAN_DARK)
g.edge('future', 'lowcode', color=CYAN_DARK)
g.edge('future', 'ethics', color=CYAN_DARK)

# Renderizar
g.render(cleanup=True)

print("Diagrama generado: output.png")
