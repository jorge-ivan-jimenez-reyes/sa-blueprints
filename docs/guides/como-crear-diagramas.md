# Cómo Crear Diagramas con Python

Esta guía te enseñará a crear diagramas de arquitectura usando la librería **Diagrams** de Python.

---

## Instalación

### 1. Instalar Python
Necesitas Python 3.9 o superior.

```bash
# Verificar versión
python3 --version
```

### 2. Instalar Graphviz
Graphviz es el motor de renderizado.

```bash
# macOS
brew install graphviz

# Ubuntu/Debian
sudo apt install graphviz

# Windows
choco install graphviz
```

### 3. Instalar la librería Diagrams

```bash
# Crear entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac

# Instalar
pip install diagrams
```

---

## Tu Primer Diagrama

### Código básico

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Mi Primer Diagrama", show=False):
    EC2("Servidor Web")
```

### Ejecutar

```bash
python mi_diagrama.py
```

Esto genera `mi_primer_diagrama.png` en el directorio actual.

---

## Estructura de un Diagrama

### Contexto del Diagrama

```python
from diagrams import Diagram

with Diagram(
    name="Nombre del Diagrama",     # Título
    filename="output/mi_diagrama",  # Ruta de salida (sin extensión)
    show=False,                     # No abrir automáticamente
    direction="TB",                 # Dirección del flujo
    outformat="png",                # Formato de salida
):
    # Tu diagrama aquí
    pass
```

### Direcciones disponibles

| Valor | Significado | Uso |
|-------|-------------|-----|
| `TB` | Top to Bottom | Jerarquías, flujos verticales |
| `BT` | Bottom to Top | Dependencias hacia arriba |
| `LR` | Left to Right | Pipelines, flujos horizontales |
| `RL` | Right to Left | Flujos inversos |

---

## Nodos (Componentes)

### Importar nodos

```python
# AWS
from diagrams.aws.compute import EC2, Lambda, ECS
from diagrams.aws.database import RDS, DynamoDB
from diagrams.aws.network import ELB, CloudFront

# Kubernetes
from diagrams.k8s.compute import Pod, Deployment
from diagrams.k8s.network import Service, Ingress

# On-Premise
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL, MySQL
from diagrams.onprem.network import Nginx

# Genéricos
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
```

### Crear nodos

```python
# Nodo simple
web = EC2("Web Server")

# Múltiples nodos
servers = [EC2("Web 1"), EC2("Web 2"), EC2("Web 3")]
```

---

## Conexiones (Edges)

### Operadores básicos

```python
# Conexión izquierda a derecha
node1 >> node2

# Conexión derecha a izquierda
node1 << node2

# Conexión bidireccional
node1 - node2

# Múltiples conexiones
node1 >> [node2, node3, node4]

# Cadena de conexiones
node1 >> node2 >> node3
```

### Edges personalizados

```python
from diagrams import Edge

# Con etiqueta
node1 >> Edge(label="HTTPS") >> node2

# Con color
node1 >> Edge(color="blue") >> node2

# Con estilo
node1 >> Edge(style="dashed") >> node2

# Combinado
node1 >> Edge(
    label="API Call",
    color="green",
    style="bold"
) >> node2
```

### Colores recomendados

| Tipo de conexión | Color |
|------------------|-------|
| Tráfico de usuario | `blue` |
| Deploy/CI-CD | `green` |
| Base de datos | `brown` |
| Cache | `cyan` |
| Monitoring | `purple` |
| Errores/Alertas | `red` |
| Opcional | `gray` |

---

## Clusters (Agrupaciones)

### Cluster básico

```python
from diagrams import Cluster

with Cluster("Web Servers"):
    web1 = Server("Web 1")
    web2 = Server("Web 2")
```

### Clusters anidados

```python
with Cluster("Production"):
    with Cluster("Frontend"):
        web = Server("Web")
    
    with Cluster("Backend"):
        api = Server("API")
        db = PostgreSQL("DB")
```

### Clusters con estilo

```python
with Cluster(
    "Blue Environment",
    graph_attr={
        "bgcolor": "#E3F2FD",    # Fondo azul claro
        "fontcolor": "#1565C0",  # Texto azul
    }
):
    Server("App Blue")
```

---

## Configuración Avanzada

### Atributos del grafo

```python
graph_attr = {
    "fontsize": "14",       # Tamaño de fuente
    "bgcolor": "white",     # Color de fondo
    "pad": "0.3",           # Padding
    "splines": "spline",    # Tipo de líneas
    "nodesep": "0.5",       # Separación horizontal
    "ranksep": "0.5",       # Separación vertical
    "dpi": "150",           # Resolución
}

with Diagram("Mi Diagrama", graph_attr=graph_attr):
    # ...
```

### Formatos de salida

```python
# Un formato
with Diagram("Test", outformat="png"):
    pass

# Múltiples formatos
with Diagram("Test", outformat=["png", "svg", "pdf"]):
    pass
```

---

## Ejemplo Completo

```python
"""
Arquitectura Web Simple
=======================
Ejemplo de diagrama completo.

Ejecutar: python ejemplo.py
Output: output/ejemplo.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis

# Configuración
graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.3",
    "splines": "spline",
}

with Diagram(
    "Arquitectura Web Simple",
    filename="output/ejemplo",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    # Usuarios
    users = Users("Usuarios")
    
    # Load Balancer
    lb = Nginx("Load Balancer")
    
    # Servidores de aplicación
    with Cluster("Application Servers"):
        apps = [
            Server("App 1"),
            Server("App 2"),
        ]
    
    # Base de datos
    with Cluster("Data Layer"):
        db = PostgreSQL("PostgreSQL")
        cache = Redis("Redis Cache")
    
    # Conexiones
    users >> Edge(color="blue", label="HTTPS") >> lb
    lb >> Edge(color="green") >> apps
    
    apps[0] >> Edge(color="brown") >> db
    apps[0] >> Edge(color="cyan") >> cache
    apps[1] >> Edge(color="brown") >> db
    apps[1] >> Edge(color="cyan") >> cache

print("Diagrama generado: output/ejemplo.png")
```

---

## Estructura de Proyecto Recomendada

```
mi-arquitectura/
├── diagrams/
│   ├── 01_arquitectura_general.py
│   ├── 02_deployment.py
│   ├── 03_cicd.py
│   └── output/
│       ├── 01_arquitectura_general.png
│       ├── 02_deployment.png
│       └── 03_cicd.png
├── docs/
│   └── descripcion.md
├── requirements.txt
└── README.md
```

---

## Tips y Mejores Prácticas

### Hacer

1. **Nombrar archivos descriptivamente**
   ```
   01_arquitectura_completa.py
   02_flujo_de_datos.py
   ```

2. **Usar comentarios/docstrings**
   ```python
   """
   Diagrama de CI/CD Pipeline
   Muestra el flujo desde GitHub hasta producción.
   """
   ```

3. **Imprimir confirmación**
   ```python
   print("Diagrama generado: output/mi_diagrama.png")
   ```

4. **Generar en carpeta output/**
   ```python
   filename="output/mi_diagrama"
   ```

### Evitar

1. **Demasiados nodos** (máx 15-20)
2. **Conexiones cruzadas** confusas
3. **Colores sin significado**
4. **Diagramas sin título**

---

## Proveedores Disponibles

La librería soporta muchos proveedores:

| Proveedor | Import |
|-----------|--------|
| AWS | `from diagrams.aws` |
| Azure | `from diagrams.azure` |
| GCP | `from diagrams.gcp` |
| Kubernetes | `from diagrams.k8s` |
| On-Premise | `from diagrams.onprem` |
| SaaS | `from diagrams.saas` |
| Generic | `from diagrams.generic` |
| Programming | `from diagrams.programming` |

Ver lista completa: [Diagrams Nodes](https://diagrams.mingrammer.com/docs/nodes/aws)

---

## Recursos

- [Documentación oficial](https://diagrams.mingrammer.com/)
- [GitHub de Diagrams](https://github.com/mingrammer/diagrams)
- [Graphviz Attributes](https://graphviz.org/doc/info/attrs.html)
- [Ejemplos en este repo](../../blueprints/)

---

## Volver

← [Tipos de Diagramas](tipos-de-diagramas.md) | [Inicio](../../README.md)
