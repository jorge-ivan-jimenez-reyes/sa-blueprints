# Preguntas para el Cliente - Clinical Research Platform

Documento de clarificacion de requerimientos antes de iniciar el desarrollo.

---

## 1. Autenticacion y Seguridad

### 1.1 Metodo de Login
- El documento menciona "correo institucional". Se requiere integracion con Single Sign-On (SSO) de la institucion?
- Se requiere integracion con Google Workspace o Microsoft Azure AD?
- Podemos utilizar servicios de autenticacion de terceros (AWS Cognito, Auth0, Clerk) o se debe desarrollar desde cero?

### 1.2 Biometricos
- Cuando se menciona "biometricos (huella o rostro)" para firma de consentimiento, se refiere a:
  - a) Utilizar Face ID / Touch ID nativos del dispositivo como metodo de autenticacion?
  - b) Capturar y almacenar datos biometricos para validacion de identidad?
- Si es opcion (b), considerar que:
  - El almacenamiento de datos biometricos tiene implicaciones legales adicionales
  - No todos los dispositivos Android tienen hardware biometrico confiable
  - Requiere validaciones adicionales para publicacion en App Store / Play Store
- Cual es el proposito exacto del biometrico: autenticacion o verificacion de identidad?

### 1.3 Autenticacion de Dos Factores (2FA)
- Para investigadores se menciona 2FA. Cual es el metodo preferido?
  - Codigo por correo electronico
  - Codigo por SMS (tiene costo por mensaje)
  - App de autenticacion (Google Authenticator, Microsoft Authenticator)
- El 2FA sera obligatorio o configurable por administrador?
- Se requiere 2FA tambien para participantes en la app movil?

### 1.4 Gestion de Sesiones
- Cual es el tiempo maximo de sesion activa antes de requerir re-autenticacion?
- Se requiere cierre automatico de sesion por inactividad? Despues de cuanto tiempo?
- Cuantos dispositivos simultaneos puede tener un usuario?

---

## 2. Roles y Permisos

### 2.1 Tipos de Usuarios
El documento menciona "investigador" y "participante". Se requieren roles adicionales?
- Administrador del sistema
- Monitor de estudio
- Coordinador de centro
- Solo lectura / Auditor

### 2.2 Permisos por Protocolo
- Los investigadores tienen acceso a todos los protocolos o solo a los asignados?
- Pueden existir investigadores con diferentes niveles de acceso dentro del mismo protocolo?
- Quien puede crear nuevos protocolos?

### 2.3 Administracion
- Quien administra los usuarios del sistema?
- Existe un super-administrador institucional?
- Se requiere aprobacion para nuevos usuarios?

---

## 3. Infraestructura y Disponibilidad

### 3.1 Disponibilidad
- Cual es el nivel de disponibilidad requerido?
  - 99.9% (8.76 horas de downtime al año)
  - 99.95% (4.38 horas de downtime al año)
  - 99.99% (52.6 minutos de downtime al año)
- El sistema debe estar disponible 24/7 o tiene ventanas de mantenimiento?
- Se requiere que sea fault-tolerant (tolerante a fallos)?

### 3.2 Escalabilidad
- Cuantos participantes se estiman por estudio?
- Cuantos estudios activos simultaneos se esperan?
- Cuantos investigadores concurrentes se esperan?
- Se anticipan picos de uso en ciertos horarios o fechas?

### 3.3 Ubicacion de Datos
- Los datos deben residir exclusivamente en Estados Unidos por HIPAA?
- Existe preferencia por alguna region de AWS especifica?

---

## 4. Integraciones

### 4.1 Dominio
- Se utilizara el dominio de la institucion?
- Se delegara un subdominio a AWS para administracion?
- Cual seria el subdominio propuesto? (ej: research.institucion.edu)

### 4.2 Sistemas Externos
- Se requiere integracion con algun sistema existente de la institucion?
- Existe un sistema de expedientes electronicos con el que se deba conectar?
- Se requiere integracion con REDCap u otro sistema de captura de datos?

### 4.3 Notificaciones
- Para notificaciones SMS, quien absorbe el costo por mensaje?
- Se tiene un proveedor de SMS preferido?
- Existe limite de notificaciones por participante?

---

## 5. Funcionalidades Especificas

### 5.1 Formularios y Variables
- El documento menciona "definir limite de variables". Cual es el maximo de variables por formulario?
- Se requiere compatibilidad exacta con tipos de variables de REDCap?
- Cuantos formularios distintos se estiman por protocolo?

### 5.2 Reportes
- Cuantos reportes personalizados se requieren?
- Se requieren graficas en tiempo real o solo exportacion de datos?
- Formatos de exportacion: solo CSV/Excel o tambien PDF, SPSS, SAS?

### 5.3 Documentos
- Cual es el tamaño maximo esperado de documentos (consentimientos, CRFs)?
- Se requiere versionamiento de documentos?
- Los participantes pueden descargar sus documentos firmados?

---

## 6. Presupuesto y Prioridades

### 6.1 Trade-offs
En caso de limitaciones de tiempo o presupuesto, cuales funcionalidades son:
- Criticas (debe tener en v1.0)
- Importantes (deseable en v1.0)
- Futuras (puede esperar a v2.0)

### 6.2 Servicios de Terceros
- Existe flexibilidad para usar servicios de terceros que aceleren el desarrollo?
  - Autenticacion: AWS Cognito, Auth0, Clerk
  - Notificaciones: Twilio, AWS SNS
  - Email: SendGrid, AWS SES
- O se requiere desarrollo propio de todos los componentes?

---

## 7. Compliance y Auditoria

### 7.1 HIPAA
- Se requiere firma de BAA (Business Associate Agreement) con AWS?
- Existe un equipo de compliance que deba revisar la arquitectura?
- Se requiere certificacion HIPAA formal o solo seguir las mejores practicas?

### 7.2 Retencion de Datos
- Cuanto tiempo deben conservarse los datos de un estudio finalizado?
- Cual es la politica de eliminacion de datos de participantes que se retiran?
- Se requiere anonimizacion de datos para ciertos reportes?

---

## Proximos Pasos

1. Agendar reunion para resolver estas preguntas
2. Aprobar diseños de UI/UX antes de desarrollo
3. Definir ambiente de desarrollo y accesos
4. Confirmar subdominio y delegacion DNS
