# LibraryManager - Sistema de Gestión de Biblioteca

## 📚 Descripción

Arquitectura y documentación del sistema de gestión de biblioteca **LibraryManager**, con enfoque en estrategias de despliegue seguras y confiables.

## 🚀 Estrategia de Deployment: Blue-Green

### ¿Qué es Blue-Green Deployment?

Blue-Green es una estrategia de despliegue que **elimina el tiempo de inactividad** manteniendo dos entornos de producción idénticos:

| Aspecto | Blue (Actual) | Green (Nueva) |
|---------|---------------|---------------|
| Estado | PRODUCCIÓN | STAGING |
| Tráfico | 100% | 0% |
| Versión | v1.0 (estable) | v1.1 (nueva) |

### Flujo de Deployment

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Usuarios  │────▶│Load Balancer│────▶│    BLUE     │ ← 100% tráfico
└─────────────┘     └──────┬──────┘     │   (v1.0)    │
                          │            └─────────────┘
                          │
                          │ (switch)    ┌─────────────┐
                          └ ─ ─ ─ ─ ─ ─▶│   GREEN     │ ← 0% tráfico
                                        │   (v1.1)    │   (listo para switch)
                                        └─────────────┘
```

### Ventajas

1. **Zero Downtime**: Los usuarios nunca experimentan interrupciones
2. **Rollback Instantáneo**: Si Green falla, volvemos a Blue en segundos
3. **Testing en Producción Real**: Green puede probarse con tráfico real antes del switch completo
4. **Confianza**: El equipo puede desplegar con tranquilidad

### Proceso de Deployment

1. **Deploy a Green**: Nueva versión se despliega en el entorno Green
2. **Smoke Tests**: Pruebas automáticas verifican que Green funciona
3. **Health Checks**: Monitoreo confirma estabilidad
4. **Switch Traffic**: Load Balancer redirige 100% a Green
5. **Monitoreo**: Si hay problemas → Rollback automático a Blue
6. **Cleanup**: Blue se prepara para el próximo deployment

## 📊 Diagramas

### Generar Diagramas

```bash
# Instalar dependencias
pip install -r ../requirements.txt

# En macOS, instalar graphviz
brew install graphviz

# Generar diagrama
cd diagrams
python blue_green_deployment.py
```

### Diagrama Generado

- `diagrams/output/blue_green_deployment.png` - Arquitectura Blue-Green completa

## 🔐 Seguridad (SSDLC)

La estrategia Blue-Green mejora la seguridad del ciclo de vida:

- **Validación pre-deployment**: Tests de seguridad antes de cada deployment
- **Aislamiento**: Entornos separados previenen contaminación
- **Auditoría**: Cada versión es trazable y reversible
- **Recuperación rápida**: Vulnerabilidades pueden mitigarse con rollback inmediato

## 🛠️ Componentes del Sistema

| Componente | Tecnología | Propósito |
|------------|------------|-----------|
| Load Balancer | HAProxy/Nginx | Distribución de tráfico y switch |
| App Servers | Node.js/Python | Lógica de negocio |
| Database | PostgreSQL | Persistencia (compartida) |
| Cache | Redis | Sesiones y caché |
| Monitoring | Prometheus + Grafana | Observabilidad |
| CI/CD | GitHub Actions | Automatización |

## 📈 Métricas de Deployment

- **Tiempo de deployment**: < 5 minutos
- **Tiempo de rollback**: < 30 segundos
- **Downtime**: 0 segundos
- **Frecuencia sugerida**: Cada 3-4 semanas (o según necesidad)

