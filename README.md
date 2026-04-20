# LCA_PRO - Sistema de Gestión de Casos y Reportes

Sistema completo de gestión de casos LCA (Life Cycle Assessment) con interfaz web moderna, controles de acceso basados en roles, y generación profesional de reportes.

## Características Principales

- ✅ **Interfaz Web Moderna**: Basada en Streamlit con diseño responsive para móviles
- ✅ **Control de Acceso**: Sistema de roles (Administrador, Usuario, Técnico)
- ✅ **Aislamiento por Empresa**: Cada empresa ve solo sus propios datos
- ✅ **Gestión de Casos**: Creación, edición y seguimiento de casos LCA
- ✅ **Motor Experto**: Análisis inteligente con IA (opcional)
- ✅ **Reportes Profesionales**: Exportación a PDF y Excel con branding
- ✅ **Base de Datos**: SQLite integrada para persistencia de datos
- ✅ **Procesamiento Multimedia**: Soporte para imágenes y audio (opcional)

## Requisitos del Sistema

- **Python 3.8+**
- **Windows/Linux/macOS**
- **4GB RAM mínimo** (8GB recomendado)
- **Espacio en disco**: 500MB mínimo

## Instalación Rápida (Windows)

1. **Descarga los archivos**:
   - `LCA_PRO (1).py` (aplicación principal)
   - `requirements.txt` (dependencias)
   - `install.bat` (instalador)
   - `start.bat` (iniciador)

2. **Ejecuta la instalación**:
   ```bash
   # Doble clic en install.bat
   # O desde línea de comandos:
   install.bat
   ```

3. **Inicia la aplicación**:
   ```bash
   # Doble clic en start.bat
   # O desde línea de comandos:
   start.bat
   ```

## Instalación Manual

### 1. Instalar Python
Descarga e instala Python 3.8+ desde: https://www.python.org/downloads/

### 2. Crear entorno virtual
```bash
python -m venv lca_pro_env
```

### 3. Activar entorno virtual
**Windows:**
```bash
lca_pro_env\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source lca_pro_env/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar aplicación
```bash
streamlit run "LCA_PRO (1).py"
```

## Uso de la Aplicación

### Acceso Inicial
- **Usuario por defecto**: admin
- **Contraseña por defecto**: admin123
- **URL**: http://localhost:8501

### Roles de Usuario

1. **Administrador**:
   - Gestión completa del sistema
   - Creación de empresas y usuarios
   - Acceso a todos los reportes

2. **Usuario**:
   - Creación y gestión de casos
   - Visualización de reportes de su empresa
   - Acceso al motor experto

3. **Técnico**:
   - Solo entrada de datos
   - No puede ver reportes
   - Acceso limitado al motor experto

### Funcionalidades Principales

#### Dashboard
- Vista general del sistema
- Estadísticas por empresa
- Navegación por módulos

#### Gestión de Casos
- Crear nuevos casos LCA
- Editar información de casos
- Subir documentos y multimedia
- Seguimiento de estado

#### Motor Experto
- Análisis inteligente con IA
- Generación de recomendaciones
- Procesamiento de datos multimedia

#### Reportes
- Reportes individuales por caso
- Reportes globales por empresa
- Exportación profesional (PDF/Excel)
- Branding personalizado

#### Administración
- Gestión de empresas
- Control de usuarios
- Configuración del sistema

## Configuración Avanzada

### Variables de Entorno
```bash
# Puerto del servidor (por defecto: 8501)
STREAMLIT_SERVER_PORT=8501

# Dirección del servidor (por defecto: localhost)
STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Modo desarrollador
STREAMLIT_DEVELOPMENT_MODE=true
```

### Base de Datos
La aplicación utiliza SQLite automáticamente. Los archivos de base de datos se crean en el directorio de trabajo.

### Personalización
- Logos y branding en `assets/` (crear directorio)
- Configuración de colores en el código CSS
- Personalización de reportes en las funciones de exportación

## Solución de Problemas

### Error de dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Problemas con Google AI
Si no tienes clave API de Google, la funcionalidad de IA estará deshabilitada automáticamente.

### Error de puerto ocupado
```bash
# Cambiar puerto
streamlit run "LCA_PRO (1).py" --server.port 8502
```

### Problemas de memoria
- Cierra otras aplicaciones
- Aumenta la RAM del sistema
- Deshabilita procesamiento multimedia si no es necesario

## Desarrollo

### Estructura del Código
```
LCA_PRO (1).py          # Aplicación principal
requirements.txt         # Dependencias Python
run.py                   # Script de inicio alternativo
install.bat             # Instalador Windows
start.bat               # Iniciador rápido
README.md               # Esta documentación
```

### Extensiones
- El código está modularizado por funciones
- Cada sección principal tiene su propia función
- Los estilos CSS están centralizados en `inject_css()`

## Soporte

Para soporte técnico o reportes de bugs, revisa:
1. Los logs de la consola
2. Los mensajes de error de Streamlit
3. La documentación de las librerías utilizadas

## Licencia

Este proyecto es de uso interno. No distribuir sin autorización.

---

**Versión**: 1.0.0
**Fecha**: Abril 2026
**Desarrollado para**: Gestión profesional de LCA