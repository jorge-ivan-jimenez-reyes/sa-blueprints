# SA Blueprints

Coleccion de arquitecturas de software y diagramas tecnicos para arquitectos de soluciones y desarrolladores.

---

## Descripcion

**SA Blueprints** es un repositorio open source con arquitecturas de software documentadas. Cada blueprint incluye:

- Diagramas de arquitectura generados con codigo (Python + Diagrams)
- Documentacion tecnica
- Estimaciones de costos cuando aplica
- Decisiones de diseno

---

## Blueprints Disponibles

| Blueprint | Descripcion | Stack |
|-----------|-------------|-------|
| [IA Interactive Website](blueprints/ia-interactive-website/) | Sitio web corporativo para agencia digital | Next.js, Strapi, Vercel |
| [AWS EKS Architecture](blueprints/aws-eks-architecture/) | Arquitectura empresarial en AWS con Kubernetes | AWS, EKS, Terraform, ArgoCD |
| [Library Manager](blueprints/library-manager/) | Sistema con Blue-Green Deployment | SDLC, CI/CD |

---

## Estructura del Repositorio

```
sa-blueprints/
├── blueprints/
│   ├── ia-interactive-website/
│   ├── aws-eks-architecture/
│   └── library-manager/
├── docs/
│   └── guides/
│       ├── que-es-arquitectura-software.md
│       ├── tipos-de-diagramas.md
│       └── como-crear-diagramas.md
├── .cursorrules
├── requirements.txt
└── README.md
```

---

## Guias

| Guia | Descripcion |
|------|-------------|
| [Que es Arquitectura de Software](docs/guides/que-es-arquitectura-software.md) | Conceptos fundamentales |
| [Tipos de Diagramas](docs/guides/tipos-de-diagramas.md) | Diferentes tipos y cuando usarlos |
| [Como Crear Diagramas](docs/guides/como-crear-diagramas.md) | Tutorial con Python Diagrams |

---

## Quick Start

### Requisitos

- Python 3.9+
- Graphviz

### Instalacion

```bash
git clone https://github.com/tu-usuario/sa-blueprints.git
cd sa-blueprints

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Graphviz
brew install graphviz        # macOS
sudo apt install graphviz    # Ubuntu
```

### Generar Diagramas

```bash
source venv/bin/activate
cd blueprints/aws-eks-architecture/src/01-complete-architecture
python diagram.py
```

---

## Tecnologias

| Herramienta | Uso |
|-------------|-----|
| [Diagrams](https://diagrams.mingrammer.com/) | Generacion de diagramas con Python |
| [Graphviz](https://graphviz.org/) | Motor de renderizado |
| Python 3.9+ | Lenguaje |

---

## Licencia

MIT License. Ver [LICENSE](LICENSE).

---

**Autor:** Jorge Ivan Jimenez Reyes 
