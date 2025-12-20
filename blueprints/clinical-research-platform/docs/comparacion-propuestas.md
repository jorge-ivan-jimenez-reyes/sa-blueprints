# Comparacion de Propuestas

Clinical Research Platform - Dos opciones con Fargate

---

| Aspecto | Propuesta A (Basica) | Propuesta B (+ Seguridad) |
|---------|----------------------|---------------------------|
| Costo mensual | $200-350 USD | $400-600 USD |
| Base de datos | RDS Single-AZ | RDS Multi-AZ |
| Cache | No | Redis |
| WAF | No | Si |
| Audit Trail | No | CloudTrail |
| Secrets Manager | No | Si |

---

## Propuesta A - Fargate Basico

Arquitectura minima funcional. Economica y escalable.

### Diagrama

![Propuesta A](../src/06-propuesta-simple/output.png)

### Componentes

| Servicio | Configuracion |
|----------|---------------|
| Fargate | 2 tareas (0.25 vCPU, 0.5GB) |
| RDS PostgreSQL | db.t3.micro Single-AZ |
| S3 | Standard |
| CloudFront | Basico |
| Cognito | User Pool |
| SNS/SES | Pay-per-use |

### Costo Estimado

| Servicio | USD/mes |
|----------|---------|
| Fargate | $30-50 |
| RDS db.t3.micro | $15-25 |
| ALB | $20-30 |
| S3 + CloudFront | $10-20 |
| Route 53 | $5 |
| Cognito (500 users) | $0-25 |
| SNS/SES | $5-15 |
| CloudWatch | $10-20 |
| **Total** | **$200-350** |

### Ventajas
- Muy economico
- Simple de mantener
- Suficiente para estudios pequenos
- Escala si se necesita

### Desventajas
- Sin alta disponibilidad (Single-AZ)
- Sin WAF (menor proteccion)
- Sin cache (mas carga en DB)
- Recovery manual si falla

### Ideal para
- MVP o piloto
- Estudios con < 100 participantes
- Presupuesto limitado

---

## Propuesta B - Fargate + Seguridad

Arquitectura robusta con alta disponibilidad y seguridad.

### Diagrama

![Propuesta B](../src/07-propuesta-estandar/output.png)

### Componentes

| Servicio | Configuracion |
|----------|---------------|
| Fargate | 2 tareas (0.5 vCPU, 1GB) con auto-scaling |
| RDS PostgreSQL | db.t3.small Multi-AZ |
| ElastiCache | cache.t3.micro |
| S3 | Standard |
| CloudFront + WAF | Con proteccion |
| Cognito | User Pool + 2FA |
| Secrets Manager | Credenciales |
| CloudTrail | Auditoria |

### Costo Estimado

| Servicio | USD/mes |
|----------|---------|
| Fargate | $50-80 |
| RDS db.t3.small Multi-AZ | $50-70 |
| ElastiCache | $15-25 |
| ALB | $20-30 |
| S3 + CloudFront | $15-25 |
| WAF | $10-20 |
| Route 53 | $5 |
| Cognito (1000 users) | $0-50 |
| Secrets Manager | $5 |
| SNS/SES | $10-20 |
| CloudWatch + CloudTrail | $20-35 |
| **Total** | **$400-600** |

### Ventajas
- Alta disponibilidad (Multi-AZ)
- Failover automatico de DB
- WAF protege contra ataques
- Cache reduce carga en DB
- Audit trail para HIPAA
- Secrets seguros

### Desventajas
- Mayor costo
- Mas componentes

### Ideal para
- Produccion
- Estudios con > 100 participantes
- Requerimiento de compliance HIPAA

---

## Comparativa de Costos

| Escenario | Propuesta A | Propuesta B |
|-----------|-------------|-------------|
| Minimo | $200/mes | $400/mes |
| Tipico | $275/mes | $500/mes |
| Pico | $350/mes | $600/mes |
| **Anual tipico** | **$3,300** | **$6,000** |

---

## Escalabilidad

Ambas propuestas usan Fargate que escala automaticamente:

| Usuarios concurrentes | Fargate tasks | Costo adicional |
|----------------------|---------------|-----------------|
| 1-50 | 2 | Base |
| 50-200 | 4 | +$30-50/mes |
| 200-500 | 6-8 | +$60-100/mes |
| 500+ | Auto-scale | Variable |

---

## Recomendacion

**Para empezar: Propuesta A**
- Iniciar con lo basico
- Validar que funciona
- Bajo riesgo financiero

**Migrar a Propuesta B cuando:**
- El estudio tenga > 50 participantes activos
- Se requiera compliance formal HIPAA
- Se detecten ataques o necesidad de WAF

La migracion de A a B toma ~1 semana y no requiere downtime significativo.

---

## Que NO incluyen estas propuestas

Costos adicionales a considerar:
- Dominio (~$12/año)
- Certificado SSL (gratis con ACM)
- SMS via SNS ($0.00645/mensaje)
- Transferencia de datos (primeros 100GB gratis)
