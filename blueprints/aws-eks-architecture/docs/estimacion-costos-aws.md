# Estimación de Costos AWS EKS
## IA interactive® - Arquitectura Kubernetes

---

## 📊 Resumen Ejecutivo

| Ambiente | Costo Mensual | Costo Anual |
|----------|---------------|-------------|
| **Development** | ~$150-250 USD | ~$1,800-3,000 USD |
| **Staging** | ~$200-350 USD | ~$2,400-4,200 USD |
| **Production** | ~$400-800 USD | ~$4,800-9,600 USD |
| **TOTAL (3 ambientes)** | **~$750-1,400 USD** | **~$9,000-16,800 USD** |

> **Nota**: Precios basados en región us-east-1. Los costos pueden variar según región, uso real y reservas.

---

## 💰 Desglose por Servicio

### 1. Amazon EKS (Control Plane)

| Item | Costo | Notas |
|------|-------|-------|
| EKS Cluster | **$0.10/hora** = **$73/mes** | Por cluster |
| | | |
| **Dev** | $73/mes | 1 cluster |
| **Stage** | $73/mes | 1 cluster |
| **Prod** | $73/mes | 1 cluster |
| **Total EKS** | **$219/mes** | 3 clusters |

> **Optimización**: Usar 1 cluster con namespaces para dev/stage puede reducir a $73/mes

---

### 2. EC2 Worker Nodes (EKS Data Plane)

#### Instancias Recomendadas

| Tipo | vCPU | RAM | Precio On-Demand | Precio Spot (~70% desc) |
|------|------|-----|------------------|------------------------|
| t3.medium | 2 | 4 GB | $0.0416/hr = ~$30/mes | ~$0.012/hr = ~$9/mes |
| t3.large | 2 | 8 GB | $0.0832/hr = ~$60/mes | ~$0.025/hr = ~$18/mes |
| t3.xlarge | 4 | 16 GB | $0.1664/hr = ~$120/mes | ~$0.05/hr = ~$36/mes |

#### Configuración por Ambiente

| Ambiente | Nodos | Tipo | Modo | Costo/mes |
|----------|-------|------|------|-----------|
| **Dev** | 2 | t3.medium | Spot | ~$18 |
| **Stage** | 2 | t3.medium | Spot | ~$18 |
| **Prod** | 3 | t3.large | On-Demand | ~$180 |
| **Total Nodes** | | | | **~$216/mes** |

> **Nota**: Producción usa On-Demand para estabilidad. Dev/Stage usan Spot para ahorro.

---

### 3. Amazon RDS (PostgreSQL)

| Tipo | vCPU | RAM | Storage | Precio |
|------|------|-----|---------|--------|
| db.t3.micro | 2 | 1 GB | 20 GB | ~$15/mes |
| db.t3.small | 2 | 2 GB | 20 GB | ~$25/mes |
| db.t3.medium | 2 | 4 GB | 50 GB | ~$50/mes |
| db.t3.large | 2 | 8 GB | 100 GB | ~$100/mes |

#### Configuración por Ambiente

| Ambiente | Tipo | Storage | Multi-AZ | Costo/mes |
|----------|------|---------|----------|-----------|
| **Dev** | db.t3.micro | 20 GB | No | ~$15 |
| **Stage** | db.t3.small | 20 GB | No | ~$25 |
| **Prod** | db.t3.medium | 50 GB | Sí | ~$100 |
| **Total RDS** | | | | **~$140/mes** |

> **Incluye**: Storage, IOPS básicos, backups automáticos (7 días)

---

### 4. Amazon CloudFront (CDN)

| Componente | Precio | Estimación |
|------------|--------|------------|
| Transferencia (primeros 10 TB) | $0.085/GB | Variable |
| Requests HTTP | $0.0075/10K | Variable |
| Requests HTTPS | $0.01/10K | Variable |

#### Estimación por Tráfico

| Tráfico Mensual | Transferencia | Requests | Costo/mes |
|-----------------|---------------|----------|-----------|
| Bajo (10K visitas) | ~5 GB | ~100K | ~$5 |
| Medio (50K visitas) | ~25 GB | ~500K | ~$15 |
| Alto (200K visitas) | ~100 GB | ~2M | ~$50 |

**Estimación Prod**: **~$20-50/mes**

---

### 5. Application Load Balancer (ALB)

| Componente | Precio |
|------------|--------|
| ALB por hora | $0.0225/hr = ~$16/mes |
| LCU (capacidad) | $0.008/LCU-hour |

#### Por Ambiente

| Ambiente | ALBs | Costo/mes |
|----------|------|-----------|
| **Dev** | 1 (público) | ~$20 |
| **Stage** | 1 (público) | ~$20 |
| **Prod** | 2 (público + interno) | ~$45 |
| **Total ALB** | | **~$85/mes** |

---

### 6. Amazon S3 (Storage)

| Componente | Precio |
|------------|--------|
| Storage (Standard) | $0.023/GB/mes |
| PUT/POST requests | $0.005/1K |
| GET requests | $0.0004/1K |
| Transferencia | $0.09/GB (fuera de AWS) |

#### Estimación

| Ambiente | Storage | Costo/mes |
|----------|---------|-----------|
| **Dev** | 5 GB | ~$1 |
| **Stage** | 5 GB | ~$1 |
| **Prod** | 50 GB | ~$5 |
| **Total S3** | | **~$7/mes** |

---

### 7. Amazon ECR (Container Registry)

| Componente | Precio |
|------------|--------|
| Storage | $0.10/GB/mes |
| Transferencia (dentro de región) | Gratis |

**Estimación**: 10 GB de imágenes = **~$1/mes**

---

### 8. Networking (VPC, NAT, etc.)

| Componente | Precio |
|------------|--------|
| NAT Gateway | $0.045/hr = ~$32/mes |
| NAT Gateway Data | $0.045/GB |
| VPC | Gratis |
| Subnets | Gratis |

#### Por Ambiente

| Ambiente | NAT Gateways | Costo/mes |
|----------|--------------|-----------|
| **Dev** | 1 | ~$35 |
| **Stage** | 1 | ~$35 |
| **Prod** | 2 (HA) | ~$70 |
| **Total NAT** | | **~$140/mes** |

> **Optimización**: Dev/Stage pueden compartir NAT o usar NAT Instance (~$5/mes)

---

### 9. Secrets Manager

| Componente | Precio |
|------------|--------|
| Por secreto | $0.40/mes |
| API calls | $0.05/10K |

**Estimación**: 10 secretos = **~$5/mes**

---

### 10. CloudWatch (Logging & Metrics)

| Componente | Precio |
|------------|--------|
| Logs Ingestion | $0.50/GB |
| Logs Storage | $0.03/GB/mes |
| Metrics | $0.30/metric/mes (después de free tier) |
| Dashboards | $3/dashboard/mes |

**Estimación Total**: **~$30-50/mes**

---

### 11. Route 53 (DNS)

| Componente | Precio |
|------------|--------|
| Hosted Zone | $0.50/mes |
| Queries (primeros 1B) | $0.40/millón |
| Health Checks | $0.50/mes por endpoint |

**Estimación**: **~$5/mes**

---

### 12. Herramientas DevOps

| Herramienta | Precio | Notas |
|-------------|--------|-------|
| **GitHub Actions** | $0-$4/usuario | Free tier generoso |
| **Argo CD** | Gratis | Open source, self-hosted |
| **Prometheus** | Gratis | Open source, self-hosted |
| **Grafana** | Gratis | Open source, self-hosted |
| **Tailscale** | $0-$6/usuario | Free tier hasta 3 usuarios |

**Total DevOps**: **~$0-20/mes**

---

## 📋 Consolidado por Ambiente

### Development (~$150-250/mes)

| Servicio | Configuración | Costo |
|----------|---------------|-------|
| EKS Control Plane | 1 cluster | $73 |
| EC2 Nodes | 2x t3.medium Spot | $18 |
| RDS | db.t3.micro | $15 |
| ALB | 1 público | $20 |
| NAT Gateway | 1 | $35 |
| S3 + ECR | ~6 GB | $2 |
| CloudWatch | Básico | $10 |
| Misc | DNS, Secrets | $5 |
| **Total Dev** | | **~$178/mes** |

### Staging (~$200-350/mes)

| Servicio | Configuración | Costo |
|----------|---------------|-------|
| EKS Control Plane | 1 cluster | $73 |
| EC2 Nodes | 2x t3.medium Spot | $18 |
| RDS | db.t3.small | $25 |
| ALB | 1 público | $20 |
| NAT Gateway | 1 | $35 |
| S3 + ECR | ~6 GB | $2 |
| CloudWatch | Básico | $15 |
| Misc | DNS, Secrets | $5 |
| **Total Stage** | | **~$193/mes** |

### Production (~$400-800/mes)

| Servicio | Configuración | Costo |
|----------|---------------|-------|
| EKS Control Plane | 1 cluster | $73 |
| EC2 Nodes | 3x t3.large On-Demand | $180 |
| RDS | db.t3.medium Multi-AZ | $100 |
| CloudFront | CDN | $30 |
| ALB | 2 (público + interno) | $45 |
| NAT Gateway | 2 (HA) | $70 |
| S3 + ECR | ~60 GB | $6 |
| CloudWatch | Completo | $30 |
| Misc | DNS, Secrets | $10 |
| **Total Prod** | | **~$544/mes** |

---

## 🔧 Estrategias de Optimización

### 1. Compartir Recursos (Ahorro: 30-40%)

| Estrategia | Ahorro |
|------------|--------|
| 1 cluster EKS con namespaces | ~$146/mes |
| NAT Instance en lugar de NAT Gateway (dev/stage) | ~$60/mes |
| ALB compartido con path-based routing | ~$40/mes |

### 2. Instancias Reservadas (Ahorro: 30-50%)

| Tipo | Commitment | Ahorro |
|------|------------|--------|
| EC2 Reserved | 1 año | ~30% |
| EC2 Reserved | 3 años | ~50% |
| RDS Reserved | 1 año | ~30% |

### 3. Spot Instances (Ahorro: 60-70%)

| Ambiente | Recomendación |
|----------|---------------|
| Dev/Stage | 100% Spot |
| Prod | Spot para workloads tolerantes a interrupciones |

### 4. Right-Sizing

- Monitorear uso real de CPU/RAM
- Ajustar instancias según métricas
- Usar HPA agresivamente

---

## 📈 Proyección Anual

### Escenario Optimizado

| Ambiente | Mensual | Anual |
|----------|---------|-------|
| Dev (compartido) | $100 | $1,200 |
| Stage (compartido) | $120 | $1,440 |
| Prod (reservas 1yr) | $380 | $4,560 |
| **Total Optimizado** | **$600/mes** | **$7,200/año** |

### Escenario Estándar

| Ambiente | Mensual | Anual |
|----------|---------|-------|
| Dev | $180 | $2,160 |
| Stage | $195 | $2,340 |
| Prod | $545 | $6,540 |
| **Total Estándar** | **$920/mes** | **$11,040/año** |

---

## ⚠️ Costos Variables (No incluidos)

| Item | Descripción |
|------|-------------|
| Transferencia de datos | Depende del tráfico |
| Picos de carga | Autoescalado puede aumentar costos |
| Backups adicionales | RDS snapshots, S3 versioning |
| WAF (opcional) | ~$20/mes + requests |
| Shield Advanced | ~$3,000/mes (solo si es crítico) |

---

## 📝 Notas Importantes

1. **Precios en USD** región us-east-1 (Nov 2024)
2. **Free Tier AWS** puede reducir costos primeros 12 meses
3. **Calculadora AWS**: https://calculator.aws/
4. **Precios Spot**: Varían según demanda, verificar en tiempo real
5. **Multi-AZ**: Solo recomendado para producción
6. **Terraform/IaC**: Automatizar destrucción de recursos no usados

---

## ✅ Recomendación Final

### Para Inicio (MVP)

```
1 cluster EKS compartido (Dev + Stage):     $150/mes
1 cluster EKS producción:                   $400/mes
─────────────────────────────────────────────────────
Total Inicial:                              $550/mes (~$6,600/año)
```

### A Medida que Escala

- Separar clusters Dev/Stage
- Implementar reservas
- Agregar redundancia (Multi-AZ)
- Escalar nodos horizontalmente

---

**Documento preparado para:** IA interactive®  
**Fecha:** Noviembre 2025  
**Versión:** 1.0  
**Fuentes:** AWS Pricing Calculator, AWS Documentation

