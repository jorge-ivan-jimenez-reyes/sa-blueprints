# Tipos de Diagramas de Arquitectura

Existen diferentes tipos de diagramas de arquitectura, cada uno con un propósito específico. Esta guía te ayudará a entender cuándo usar cada uno.

---

## Vista General

| Tipo | Propósito | Audiencia | Nivel de Detalle |
|------|-----------|-----------|------------------|
| Aplicación | Estructura del software | Desarrolladores | Alto |
| Integración | Cómo interactúan componentes | Arquitectos | Medio |
| Deployment | Dónde se ejecuta | DevOps/SRE | Alto |
| DevOps/CI-CD | Flujos de implementación | DevOps | Medio |
| Datos | Flujo de información | Data Engineers | Alto |
| Seguridad | Capas de protección | Security | Medio |

---

## Diagrama de Arquitectura de Aplicación

### ¿Qué es?
Muestra la **estructura básica del software**: componentes, módulos y sus relaciones.

### ¿Cuándo usarlo?
- Explicar la estructura de una aplicación
- Evaluar impacto de cambios
- Onboarding de nuevos desarrolladores

### Elementos típicos
- Frontend, Backend, APIs
- Bases de datos
- Servicios externos
- Usuarios

### Ejemplo
```
┌─────────────────────────────────────────────────────┐
│                    Usuarios                          │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                 CDN (Cloudflare)                     │
└─────────────────────┬───────────────────────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│    Frontend     │     │   Admin Panel   │
│   (Next.js)     │     │   (React)       │
└────────┬────────┘     └────────┬────────┘
         │                       │
         └───────────┬───────────┘
                     ▼
         ┌─────────────────────┐
         │    Backend API      │
         │    (Node.js)        │
         └──────────┬──────────┘
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
┌─────────────────┐   ┌─────────────────┐
│   PostgreSQL    │   │     Redis       │
│   (Database)    │   │    (Cache)      │
└─────────────────┘   └─────────────────┘
```

---

## Diagrama de Arquitectura de Integración

### ¿Qué es?
Se enfoca en **cómo se comunican** los diferentes sistemas y servicios.

### ¿Cuándo usarlo?
- Planificar integraciones con terceros
- Documentar APIs y protocolos
- Analizar dependencias externas

### Elementos típicos
- APIs (REST, GraphQL, gRPC)
- Message queues
- Webhooks
- Servicios externos

### Ejemplo
```
┌─────────────┐         ┌─────────────┐
│  Sistema A  │◄──REST──►│  Sistema B  │
└──────┬──────┘         └──────┬──────┘
       │                       │
       │ Webhook               │ gRPC
       ▼                       ▼
┌─────────────┐         ┌─────────────┐
│  Stripe     │         │  Auth0      │
│  (Pagos)    │         │  (Auth)     │
└─────────────┘         └─────────────┘
```

---

## Diagrama de Arquitectura de Deployment

### ¿Qué es?
Muestra **dónde y cómo** se despliega el sistema físicamente.

### ¿Cuándo usarlo?
- Planificar infraestructura
- Documentar ambientes (dev, staging, prod)
- Estrategias de deployment (Blue-Green, Canary)

### Elementos típicos
- Servidores/Instancias
- Contenedores (Docker, K8s)
- Load Balancers
- Redes y zonas

### Ejemplo: Blue-Green Deployment
```
                    ┌─────────────────┐
                    │  Load Balancer  │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
     ┌─────────────────┐           ┌─────────────────┐
     │  BLUE (v1.0)    │           │  GREEN (v1.1)   │
     │  ████████████   │           │  ░░░░░░░░░░░░   │
     │  100% traffic   │           │  0% traffic     │
     └─────────────────┘           └─────────────────┘
```

---

## Diagrama de DevOps / CI-CD

### ¿Qué es?
Visualiza los **flujos de integración y despliegue** continuo.

### ¿Cuándo usarlo?
- Documentar pipelines
- Mejorar procesos de deployment
- Onboarding de DevOps

### Elementos típicos
- Repositorios (GitHub, GitLab)
- CI tools (GitHub Actions, Jenkins)
- Container registries
- Ambientes de deployment

### Ejemplo
```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  GitHub  │────▶│   CI     │────▶│  Docker  │────▶│   K8s    │
│  (Code)  │     │ (Build)  │     │ Registry │     │ (Deploy) │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
     │               │                                   │
     │               ▼                                   │
     │        ┌──────────┐                              │
     │        │  Tests   │                              │
     │        │  Lint    │                              │
     │        └──────────┘                              │
     │                                                   │
     └───────────────── GitOps ─────────────────────────┘
```

---

## Diagrama de Arquitectura de Datos

### ¿Qué es?
Muestra **cómo fluyen y se almacenan los datos** en el sistema.

### ¿Cuándo usarlo?
- Diseñar data pipelines
- Optimizar almacenamiento
- Cumplimiento y auditoría (GDPR, etc.)

### Elementos típicos
- Fuentes de datos
- ETL/ELT processes
- Data warehouses
- Analytics tools

### Ejemplo
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Sources   │     │    ETL      │     │  Warehouse  │
│  ─────────  │────▶│  ─────────  │────▶│  ─────────  │
│  - App DB   │     │  - Extract  │     │  - Snowflake│
│  - Logs     │     │  - Transform│     │  - BigQuery │
│  - APIs     │     │  - Load     │     │             │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │  Analytics  │
                                        │  - Metabase │
                                        │  - Looker   │
                                        └─────────────┘
```

---

## Diagrama de Arquitectura de Seguridad

### ¿Qué es?
Documenta las **capas de seguridad** y protección del sistema.

### ¿Cuándo usarlo?
- Auditorías de seguridad
- Cumplimiento regulatorio
- Análisis de riesgos

### Elementos típicos
- Firewalls / WAF
- Authentication (OAuth, JWT)
- Encryption
- Access control

### Ejemplo
```
┌─────────────────────────────────────────────────────┐
│                    INTERNET                          │
└─────────────────────────┬───────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│              WAF + DDoS Protection                   │
│                   (Cloudflare)                       │
└─────────────────────────┬───────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                   SSL/TLS                            │
│               (HTTPS Encryption)                     │
└─────────────────────────┬───────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│              Authentication Layer                    │
│              (OAuth 2.0 / JWT)                       │
└─────────────────────────┬───────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│              Application Layer                       │
│           (Input Validation, RBAC)                   │
└─────────────────────────┬───────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                Data Layer                            │
│         (Encryption at Rest, Backups)               │
└─────────────────────────────────────────────────────┘
```

---

## ¿Qué Diagrama Necesito?

| Si necesitas... | Usa este diagrama |
|-----------------|-------------------|
| Explicar cómo está construida la app | Aplicación |
| Mostrar comunicación entre sistemas | Integración |
| Documentar infraestructura y servidores | Deployment |
| Visualizar el pipeline de CI/CD | DevOps |
| Entender el flujo de información | Datos |
| Auditar seguridad del sistema | Seguridad |

---

## Mejores Prácticas

### Hacer
- Mantener los diagramas simples (máx 15-20 elementos)
- Usar colores consistentes
- Incluir leyenda si es necesario
- Actualizar cuando cambie la arquitectura
- Versionar los diagramas

### Evitar
- Demasiado detalle en un solo diagrama
- Mezclar diferentes niveles de abstracción
- Colores sin significado
- Diagramas desactualizados
- Información sensible (IPs, passwords)

---

## Siguiente Paso

Aprende [Cómo Crear Diagramas con Python](como-crear-diagramas.md) →
