# Glosario de Términos
## Documentación de Arquitectura - IA interactive®

---

> Este glosario define los términos técnicos utilizados en la documentación para asegurar claridad y evitar ambigüedades.

---

## A

### API (Application Programming Interface)
Interfaz que permite la comunicación entre diferentes sistemas de software. En esta arquitectura, las API Routes de Next.js manejan las solicitudes del frontend.

### API REST
Estilo de arquitectura para diseñar servicios web que utilizan HTTP para comunicarse. Strapi expone una API REST para acceder al contenido.

---

## B

### Backend
La parte del sistema que procesa la lógica de negocio, accede a bases de datos y maneja la seguridad. No es visible para los usuarios finales.

### Blob Storage
Almacenamiento de objetos binarios grandes como imágenes, videos y archivos. Cloudflare R2 sirve este propósito.

### Bounce Rate (Tasa de Rebote)
Porcentaje de visitantes que abandonan el sitio después de ver solo una página.

---

## C

### Cache
Almacenamiento temporal de datos para acceso rápido. Reduce la carga en servidores y mejora tiempos de respuesta.

### CDN (Content Delivery Network)
Red de servidores distribuidos globalmente que entregan contenido al usuario desde la ubicación más cercana. Cloudflare es el CDN propuesto.

### CI/CD (Continuous Integration/Continuous Deployment)
Prácticas de desarrollo que automatizan la integración y despliegue de código. GitHub Actions implementa esto.

### CMS (Content Management System)
Sistema para crear, editar y gestionar contenido digital. Strapi es el CMS headless propuesto.

### Core Web Vitals
Métricas de Google que miden la experiencia del usuario: LCP, FID, CLS.

### CORS (Cross-Origin Resource Sharing)
Mecanismo de seguridad que controla qué dominios pueden acceder a recursos de una API.

### CSRF (Cross-Site Request Forgery)
Tipo de ataque donde un sitio malicioso engaña al navegador para realizar acciones no autorizadas.

---

## D

### DDoS (Distributed Denial of Service)
Ataque que intenta hacer un servicio inaccesible inundándolo con tráfico malicioso.

### Deploy
Proceso de publicar una nueva versión del software en producción.

---

## E

### Edge Computing
Procesamiento de datos cerca del usuario final en lugar de un servidor centralizado. Vercel Edge y Cloudflare operan en el edge.

### Edge Functions
Funciones que se ejecutan en servidores edge, cerca del usuario, para menor latencia.

### Egress
Tráfico de datos que sale de un servicio cloud. Cloudflare R2 no cobra por egress.

---

## F

### FCP (First Contentful Paint)
Tiempo hasta que el navegador renderiza el primer contenido visible.

### FID (First Input Delay)
Tiempo desde que el usuario interactúa hasta que el navegador responde.

### Frontend
La parte del sistema que el usuario ve e interactúa directamente. Next.js construye el frontend.

---

## G

### GraphQL
Lenguaje de consulta para APIs que permite solicitar exactamente los datos necesarios. Strapi soporta GraphQL.

---

## H

### Headless CMS
CMS que solo gestiona contenido sin frontend propio, entregando datos via API. Strapi es headless.

### Heatmap
Visualización que muestra dónde hacen clic los usuarios en una página. Hotjar genera heatmaps.

### HSTS (HTTP Strict Transport Security)
Header de seguridad que fuerza conexiones HTTPS.

---

## I

### i18n (Internationalization)
Proceso de diseñar software para soportar múltiples idiomas. next-intl maneja i18n.

### ISR (Incremental Static Regeneration)
Técnica de Next.js que regenera páginas estáticas bajo demanda sin rebuild completo.

---

## J

### JAMstack
Arquitectura moderna: JavaScript, APIs, Markup. Genera sitios estáticos con contenido dinámico vía APIs.

### JWT (JSON Web Token)
Estándar para tokens de autenticación seguros y auto-contenidos.

---

## L

### LCP (Largest Contentful Paint)
Tiempo hasta que el elemento más grande de la página es visible. Objetivo: < 2.5 segundos.

### Lazy Loading
Técnica que carga recursos (imágenes, componentes) solo cuando son necesarios.

---

## M

### Middleware
Software que actúa entre el cliente y el servidor, procesando requests/responses.

---

## N

### Next.js
Framework de React para construir aplicaciones web con SSR, SSG e ISR.

---

## O

### OAuth 2.0
Protocolo estándar de autorización que permite acceso seguro a recursos.

### OIDC (OpenID Connect)
Capa de identidad sobre OAuth 2.0 para autenticación.

---

## P

### PostgreSQL
Base de datos relacional open source, robusta y escalable.

### Preview Deployment
Versión temporal del sitio para revisar cambios antes de producción.

---

## R

### Rate Limiting
Técnica que limita el número de requests por usuario/IP para prevenir abuso.

### RBAC (Role-Based Access Control)
Control de acceso basado en roles de usuario (Admin, Editor, etc.).

### Redis
Base de datos en memoria usada principalmente para cache. Upstash ofrece Redis serverless.

### REST
Ver API REST.

### RLS (Row Level Security)
Políticas de seguridad a nivel de fila en bases de datos.

---

## S

### S3 (Simple Storage Service)
Servicio de almacenamiento de objetos de AWS. Cloudflare R2 es compatible con S3.

### Serverless
Modelo donde el proveedor cloud gestiona la infraestructura. Pagas solo por uso.

### SLA (Service Level Agreement)
Acuerdo de nivel de servicio que garantiza disponibilidad (ej: 99.9%).

### SSG (Static Site Generation)
Generación de páginas HTML en tiempo de build, no en cada request.

### SSR (Server-Side Rendering)
Renderizado de páginas en el servidor para cada request.

### SSL/TLS
Protocolos de encriptación para comunicaciones seguras (HTTPS).

### Stale-While-Revalidate
Estrategia de cache que sirve contenido antiguo mientras actualiza en segundo plano.

### Strapi
CMS headless open source basado en Node.js.

---

## T

### TypeScript
Superset de JavaScript con tipado estático. Mejora la calidad del código.

---

## U

### Upstash
Proveedor de Redis serverless con pricing por request.

---

## V

### Vercel
Plataforma de hosting optimizada para Next.js con edge network global.

---

## W

### WAF (Web Application Firewall)
Firewall que protege aplicaciones web filtrando tráfico malicioso.

### Webhook
Notificación HTTP automática cuando ocurre un evento en un sistema.

### WYSIWYG (What You See Is What You Get)
Editor donde el contenido se ve igual que el resultado final.

---

## X

### XSS (Cross-Site Scripting)
Ataque que inyecta scripts maliciosos en páginas web.

---

## Z

### Zod
Librería de validación de esquemas para TypeScript.

---

*Última actualización: Noviembre 2025*

