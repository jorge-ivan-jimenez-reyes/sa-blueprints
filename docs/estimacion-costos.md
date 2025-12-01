# Estimación de Costos de Infraestructura
## IA interactive® - Sitio Web Corporativo

---

## 📊 Resumen Ejecutivo

| Escenario | Costo Mensual | Costo Anual |
|-----------|---------------|-------------|
| **MVP / Inicial** | $45-65 USD | $540-780 USD |
| **Crecimiento** | $100-150 USD | $1,200-1,800 USD |
| **Escala / Enterprise** | $250-400 USD | $3,000-4,800 USD |

> **Nota**: Los costos no incluyen desarrollo, solo infraestructura, plataformas y herramientas.

---

## 📋 Desglose Detallado por Servicio

### 1. Hosting Frontend - Vercel

| Plan | Costo | Incluye | Recomendación |
|------|-------|---------|---------------|
| **Hobby** | $0/mes | 100GB bandwidth, SSL, previews | ❌ Solo desarrollo |
| **Pro** | $20/mes | 1TB bandwidth, analytics, team | ✅ Producción |
| **Enterprise** | Custom | SLA, soporte, features avanzados | Para escala |

**Selección: Pro Plan - $20/mes**

Costos adicionales Vercel:
- Bandwidth extra: $40/100GB
- Edge Functions: $2/millón de invocaciones
- Analytics: Incluido en Pro

---

### 2. CMS - Strapi (Self-hosted)

Strapi es open source, el costo es solo del hosting:

| Proveedor | Plan | Costo | Specs |
|-----------|------|-------|-------|
| **Railway** | Starter | $5/mes + uso | 512MB RAM, auto-scale |
| **Render** | Starter | $7/mes | 512MB RAM |
| **DigitalOcean** | Basic | $12/mes | 1GB RAM, 25GB SSD |
| **AWS ECS** | Fargate | $15-30/mes | Variable |

**Selección: Railway Starter - ~$5-10/mes**

---

### 3. Base de Datos - PostgreSQL

| Proveedor | Plan | Costo | Specs |
|-----------|------|-------|-------|
| **Supabase** | Free | $0/mes | 500MB, 2 proyectos |
| **Supabase** | Pro | $25/mes | 8GB, backups, no pause |
| **Railway** | Incluido | ~$5/mes | 1GB, auto-scale |
| **Neon** | Free | $0/mes | 512MB, branching |
| **PlanetScale** | Free | $0/mes | 5GB, MySQL |

**Selección: Supabase Pro - $25/mes** (para producción con backups)

---

### 4. CDN y Seguridad - Cloudflare

| Plan | Costo | Incluye |
|------|-------|---------|
| **Free** | $0/mes | CDN, SSL, DDoS básico |
| **Pro** | $20/mes | WAF, Image optimization, Analytics |
| **Business** | $200/mes | WAF avanzado, SLA 100% |

**Selección: Free para MVP, Pro para producción - $0-20/mes**

---

### 5. Cache - Redis

| Proveedor | Plan | Costo | Specs |
|-----------|------|-------|-------|
| **Upstash** | Free | $0/mes | 10K commands/día |
| **Upstash** | Pay-as-you-go | ~$5/mes | $0.2/100K commands |
| **Redis Cloud** | Free | $0/mes | 30MB |
| **Railway** | - | ~$3/mes | Incluido en plan |

**Selección: Upstash Free/Pay-as-you-go - $0-5/mes**

---

### 6. Object Storage (Imágenes/Assets)

| Proveedor | Plan | Costo | Egress |
|-----------|------|-------|--------|
| **Cloudflare R2** | Pay-as-you-go | $0.015/GB/mes | $0 (gratis) |
| **AWS S3** | Standard | $0.023/GB/mes | $0.09/GB |
| **Supabase Storage** | Incluido | $0-25/mes | Incluido |
| **Vercel Blob** | - | $0.15/GB/mes | $0.15/GB |

**Selección: Cloudflare R2 - ~$1-5/mes** (sin egress fees)

---

### 7. Email Transaccional

| Proveedor | Plan | Costo | Límite |
|-----------|------|-------|--------|
| **Resend** | Free | $0/mes | 3K emails/mes |
| **Resend** | Pro | $20/mes | 50K emails/mes |
| **SendGrid** | Free | $0/mes | 100 emails/día |
| **AWS SES** | Pay-as-you-go | $0.10/1K emails | Sin límite |

**Selección: Resend Free → Pro según volumen - $0-20/mes**

---

### 8. Scheduling (Agendar Citas)

| Proveedor | Plan | Costo | Features |
|-----------|------|-------|----------|
| **Cal.com** | Free | $0/mes | 1 calendario, básico |
| **Cal.com** | Team | $12/usuario/mes | Team features |
| **Calendly** | Free | $0/mes | 1 tipo de evento |
| **Calendly** | Pro | $10/mes | Unlimited |

**Selección: Cal.com Free (open source) - $0/mes**

---

### 9. Analytics y Monitoreo

| Servicio | Plan | Costo | Uso |
|----------|------|-------|-----|
| **Google Analytics 4** | Free | $0/mes | Métricas web |
| **Hotjar** | Basic | $0/mes | 35 sessions/día |
| **Hotjar** | Plus | $32/mes | 100 sessions/día |
| **Vercel Analytics** | Incluido Pro | $0 | Web Vitals |
| **Sentry** | Team | $26/mes | Error tracking |
| **Sentry** | Developer | $0/mes | 5K errors/mes |

**Selección para MVP:**
- GA4 Free: $0
- Hotjar Basic: $0
- Sentry Developer: $0
- **Total: $0/mes**

**Selección para Producción:**
- GA4 Free: $0
- Hotjar Plus: $32/mes
- Sentry Team: $26/mes
- **Total: $58/mes**

---

### 10. Dominio y SSL

| Item | Costo | Frecuencia |
|------|-------|------------|
| Dominio .com | $12-15 | Anual |
| Dominio .mx (opcional) | $15-25 | Anual |
| SSL | $0 | Incluido (Cloudflare/Vercel) |

**Total: ~$15-40/año**

---

### 11. CI/CD y Versionamiento

| Servicio | Plan | Costo |
|----------|------|-------|
| **GitHub** | Free | $0/mes (repos públicos/privados) |
| **GitHub Actions** | Free | 2,000 min/mes |

**Selección: GitHub Free - $0/mes**

---

## 💰 Escenarios de Costo Consolidados

### Escenario 1: MVP / Lanzamiento Inicial

Para sitio con bajo tráfico inicial (~1,000-5,000 visitas/mes):

| Servicio | Costo Mensual |
|----------|---------------|
| Vercel Pro | $20 |
| Railway (Strapi) | $5 |
| Supabase Free | $0 |
| Cloudflare Free | $0 |
| Upstash Free | $0 |
| Cloudflare R2 | $1 |
| Resend Free | $0 |
| Cal.com Free | $0 |
| Analytics (Free tier) | $0 |
| GitHub Free | $0 |
| **TOTAL** | **~$26/mes** |
| Dominio (anual) | $15/año |

**Costo Anual MVP: ~$327 USD**

---

### Escenario 2: Producción / Crecimiento

Para sitio con tráfico medio (~10,000-50,000 visitas/mes):

| Servicio | Costo Mensual |
|----------|---------------|
| Vercel Pro | $20 |
| Railway (Strapi) | $10 |
| Supabase Pro | $25 |
| Cloudflare Pro | $20 |
| Upstash | $5 |
| Cloudflare R2 | $5 |
| Resend Pro | $20 |
| Cal.com Free | $0 |
| Hotjar Plus | $32 |
| Sentry Team | $26 |
| GitHub Free | $0 |
| **TOTAL** | **~$163/mes** |
| Dominio (anual) | $15/año |

**Costo Anual Producción: ~$1,971 USD**

---

### Escenario 3: Escala / Alto Tráfico

Para sitio con alto tráfico (>100,000 visitas/mes):

| Servicio | Costo Mensual |
|----------|---------------|
| Vercel Pro + bandwidth | $50 |
| Railway (Strapi scaled) | $30 |
| Supabase Pro + compute | $75 |
| Cloudflare Pro | $20 |
| Upstash Pro | $20 |
| Cloudflare R2 | $15 |
| Resend Pro | $20 |
| Cal.com Team | $24 |
| Hotjar Business | $80 |
| Sentry Team | $26 |
| GitHub Team | $0 |
| **TOTAL** | **~$360/mes** |

**Costo Anual Escala: ~$4,320 USD**

---

## 📈 Comparativa con Alternativas

### vs. WordPress Hosting Tradicional

| Aspecto | Propuesta (JAMstack) | WordPress Managed |
|---------|---------------------|-------------------|
| Hosting | $20-50/mes | $30-100/mes |
| Seguridad | Cloudflare incluido | Plugin extra $5-20/mes |
| Performance | SSG + CDN nativo | Requiere plugins |
| Escalabilidad | Automática | Manual/costosa |
| **Total típico** | **$50-150/mes** | **$80-200/mes** |

### vs. Enterprise CMS (Contentful, Sanity)

| CMS | Costo Mensual | Límites |
|-----|---------------|---------|
| **Strapi (propuesto)** | $5-30 (hosting) | Ilimitado |
| Contentful | $300+ | Enterprise features |
| Sanity | $99+ | Team features |

**Ahorro con Strapi: $70-270/mes**

---

## 🔮 Proyección a 12 Meses

| Mes | Escenario | Costo Acumulado |
|-----|-----------|-----------------|
| 1-3 | MVP | $78 |
| 4-6 | Crecimiento | $489 |
| 7-12 | Producción | $978 |
| **Total Año 1** | | **~$1,545 USD** |

---

## ✅ Recomendaciones de Optimización

1. **Empezar con tiers gratuitos** y escalar según métricas reales
2. **Monitorear bandwidth** de Vercel para evitar sorpresas
3. **Usar Cloudflare R2** en lugar de S3 para eliminar egress costs
4. **Cachear agresivamente** para reducir requests al origin
5. **Revisar analytics** mensualmente para ajustar servicios

---

## 📝 Notas Importantes

1. **Precios en USD** y sujetos a cambios por los proveedores
2. **No incluye** costos de desarrollo, diseño o contenido
3. **No incluye** licencias de software adicional (todo es open source)
4. **IVA/impuestos** pueden aplicar según ubicación
5. **Precios de noviembre 2025** - verificar actualizaciones

---

**Documento preparado para:** IA interactive®  
**Fecha:** Noviembre 2025  
**Versión:** 1.0

