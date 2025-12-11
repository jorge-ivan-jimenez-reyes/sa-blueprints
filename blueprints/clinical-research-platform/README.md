# Clinical Research Platform

Plataforma para gestion de estudios clinicos con aplicacion movil para participantes y webapp para investigadores.

---

## Objetivos

- Herramienta de apoyo a investigadores para mejorar adherencia a protocolos
- Mejorar retencion de pacientes en estudios clinicos
- Seguimiento seguro de participantes cumpliendo HIPAA

---

## Stack Tecnologico

| Componente | Tecnologia |
|------------|------------|
| Mobile App | React Native (iOS/Android) |
| WebApp | React + AWS Amplify |
| Backend | Node.js / Python |
| Database | PostgreSQL (RDS) |
| Cloud | AWS (HIPAA Compliant) |
| Auth | AWS Cognito (2FA/MFA) |
| Storage | S3 (Encrypted) |
| Notifications | SNS / SES |

---

## Estructura

```
clinical-research-platform/
├── src/
│   ├── 01-complete-architecture/
│   ├── 02-mobile-app/
│   ├── 03-webapp/
│   ├── 04-backend-infrastructure/
│   ├── 05-security-layers/
│   ├── 06-propuesta-simple/      # Fargate (Serverless)
│   └── 07-propuesta-estandar/    # EC2 (Autoadministrado)
└── docs/
    ├── preguntas-cliente.md
    └── comparacion-propuestas.md
```

---

## Diagramas

### 01 - Arquitectura Completa

Vista general de toda la plataforma. Muestra como se conectan los usuarios (participantes y investigadores) con la infraestructura AWS.

Flujo:
1. Participantes acceden via Mobile App (React Native)
2. Investigadores acceden via WebApp (React + Amplify)
3. Route 53 resuelve DNS
4. CloudFront distribuye contenido estatico
5. ALB balancea trafico al backend
6. Backend en contenedores procesa requests
7. Datos en RDS PostgreSQL y S3
8. Cognito maneja autenticacion
9. SNS/SES envian notificaciones

![Complete Architecture](src/01-complete-architecture/output.png)

---

### 02 - Mobile App (Participantes)

Arquitectura de la aplicacion movil React Native para iOS y Android.

Componentes:
- React Native con navegacion y estado local
- Cognito para login con biometricos opcionales
- API Gateway o ALB para comunicacion con backend
- S3 para documentos y consentimientos
- Push notifications via SNS

Funcionalidades:
- Login seguro con opcion biometrica
- Dashboard de estado del estudio
- Calendario de visitas con confirmacion
- Consentimiento informado digital con firma
- Encuestas y formularios de seguimiento
- Chat seguro con el equipo de investigacion
- Notificaciones push de recordatorios

![Mobile App](src/02-mobile-app/output.png)

---

### 03 - WebApp (Investigadores)

Panel de administracion web para el equipo de investigacion.

Componentes:
- React SPA hosteado en Amplify
- Cognito con 2FA obligatorio
- Conexion a API backend
- Reportes exportables

Funcionalidades:
- Dashboard con KPIs (estudios activos, pacientes, visitas)
- Gestion de protocolos y CRFs
- Enrolamiento y seguimiento de participantes
- Cronograma de visitas con colores
- Recoleccion de datos con validaciones
- Registro de eventos adversos
- Reportes exportables (CSV/Excel)
- Auditoria completa de acciones

![WebApp](src/03-webapp/output.png)

---

### 04 - Backend Infrastructure

Infraestructura de backend en AWS cumpliendo lineamientos HIPAA.

Componentes:
- VPC con subnets publicas (ALB) y privadas (compute, DB)
- ECS/Fargate o EC2 para contenedores
- RDS PostgreSQL para datos relacionales
- ElastiCache Redis para cache de sesiones
- S3 encriptado para documentos PHI
- CloudWatch para metricas y logs
- CloudTrail para auditoria

Seguridad:
- Todo el trafico interno en subnets privadas
- Base de datos sin acceso publico
- Encryption at rest y in transit
- Backups automaticos

![Backend Infrastructure](src/04-backend-infrastructure/output.png)

---

### 05 - Capas de Seguridad

Stack de seguridad en capas para cumplimiento HIPAA.

| Capa | Componentes | Funcion |
|------|-------------|---------|
| 1. Edge | Shield, WAF, CloudFront | Proteccion DDoS y filtrado |
| 2. Auth | Cognito, IAM, RBAC | Autenticacion y autorizacion |
| 3. Network | VPC, Security Groups | Aislamiento de red |
| 4. Application | Validation, Sessions | Seguridad en codigo |
| 5. Data | KMS, Encryption | Proteccion de datos |
| 6. Audit | CloudTrail, Logs | Trazabilidad completa |

Cada capa agrega proteccion independiente. Un atacante tendria que vulnerar todas las capas para acceder a datos PHI.

![Security Layers](src/05-security-layers/output.png)

---

## Propuestas de Arquitectura

Dos opciones con diferentes niveles de costo y complejidad.

### 06 - Propuesta A: Fargate (Serverless)

AWS administra los servidores. Solo subes contenedores y AWS escala automaticamente.

| Aspecto | Valor |
|---------|-------|
| Compute | Fargate (2 tareas) |
| Database | RDS PostgreSQL Single-AZ |
| Cache | No |
| WAF | No |
| Costo | $200-350 USD/mes |

Ventajas:
- Sin administracion de servidores
- AWS parcha el OS automaticamente
- Escala automatico segun demanda
- Pay-per-use (pagas solo lo que usas)

Desventajas:
- Menos control sobre infraestructura
- Sin WAF (proteccion basica)
- Sin cache (puede ser mas lento)
- Sin audit trail avanzado

Ideal para: Equipos pequenos sin DevOps dedicado.

![Propuesta A - Fargate](src/06-propuesta-simple/output.png)

---

### 07 - Propuesta B: EC2 (Autoadministrado)

Ustedes administran los servidores EC2. Control total con SSH y configuracion personalizada.

| Aspecto | Valor |
|---------|-------|
| Compute | EC2 (2x t3.small) |
| Database | RDS PostgreSQL Single-AZ |
| Cache | ElastiCache Redis |
| WAF | Si |
| CloudTrail | Si |
| Secrets Manager | Si |
| Costo | $300-450 USD/mes |

Ventajas:
- Control total (SSH, logs, configuracion)
- WAF protege contra ataques web
- Cache Redis mejora performance
- Audit trail completo para HIPAA
- Secrets Manager para credenciales
- Pueden optimizar instancias segun necesidad

Desventajas:
- Ustedes parchean el sistema operativo
- Ustedes escalan manualmente (o configuran Auto Scaling)
- Pagan 24/7 aunque no haya trafico

Ideal para: Equipos con experiencia en administracion de servidores.

![Propuesta B - EC2](src/07-propuesta-estandar/output.png)

---

## Comparativa de Propuestas

| | Propuesta A (Fargate) | Propuesta B (EC2) |
|-|----------------------|-------------------|
| Quien administra | AWS | Ustedes |
| Parches de OS | Automatico | Manual |
| SSH a servidor | No | Si |
| WAF | No | Si |
| Cache Redis | No | Si |
| CloudTrail | No | Si |
| Costo minimo | $200/mes | $300/mes |
| Costo tipico | $275/mes | $375/mes |
| Anual estimado | $3,300 | $4,500 |

Ver comparacion detallada: [docs/comparacion-propuestas.md](docs/comparacion-propuestas.md)

---

## Requisitos HIPAA

| Requisito | Implementacion |
|-----------|----------------|
| Encryption at Rest | KMS + RDS Encrypted + S3 Encrypted |
| Encryption in Transit | SSL/TLS en todo el trafico |
| Access Control | Cognito + IAM + RBAC por roles |
| Audit Logs | CloudTrail + Audit Trail en app |
| Data Backup | RDS Automated Backups + S3 Versioning |
| Network Isolation | VPC + Private Subnets + Security Groups |

---

## Equipo

| Rol | Nombre |
|-----|--------|
| Coordinador | Mtro. Alfredo Pedroza Diaz |
| Lider | Jonathan Arroyo Pilatowsky |
| Programador Sr | Dr. David Escobar Castillejos |
| Programador Sr | Ing. Inaki Siguenza Noriega |
| Programador Jr | Luis Cedillo Maldonado |
| Programador Jr | Mauricio Chavarria |
| Programador Jr | Esteban Mayoral |
| Programador Jr | Daniel Pelaez |
| Programador Jr | Jorge Jimenez |

---

## Timeline

- Duracion: 9 meses
- Metodologia: Agile con sprints semanales
- Entregas iterativas con demos al cliente

---

## Documentacion

| Documento | Descripcion |
|-----------|-------------|
| [Preguntas para Cliente](docs/preguntas-cliente.md) | Clarificaciones pendientes sobre requerimientos |
| [Comparacion Propuestas](docs/comparacion-propuestas.md) | Fargate vs EC2 con costos detallados |

---

## Generar Diagramas

```bash
cd sa-blueprints
source venv/bin/activate

# Generar un diagrama especifico
cd blueprints/clinical-research-platform/src/01-complete-architecture
python diagram.py

# Generar todos los diagramas
for dir in blueprints/clinical-research-platform/src/*/; do
  (cd "$dir" && python diagram.py)
done
```
