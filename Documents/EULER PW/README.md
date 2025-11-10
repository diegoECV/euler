# Grupo de Ciencias Veen Euler - Sistema Web

Sistema web completo para la academia Grupo de Ciencias Veen Euler con gestión de estudiantes, programas educativos y base de datos MySQL.

## 🚀 Tecnologías

- **Frontend**: Vite + Tailwind CSS + Material Icons
- **Backend**: Flask + SQLAlchemy + MySQL
- **Base de Datos**: MySQL (AWS RDS)
- **Deployment**: Python Virtual Environment

## 📋 Requisitos del Sistema

- Python 3.8 o superior
- Node.js 16+ y npm
- MySQL (local o AWS RDS)
- Entorno virtual Python (venv o virtualenv)

## ⚡ Instalación Rápida

### 1. Clonar y configurar el proyecto

```bash
cd "c:\Users\dieog\Documents\EULER PW"
```

### 2. Configurar entorno virtual Python

```bash
# Activar tu entorno virtual existente
venv\Scripts\activate

# Instalar dependencias automáticamente
python setup.py
```

### 3. Configurar variables de entorno

Crear archivo `.env` con:

```env
DB_HOST=database-1.ctusauicknm6.us-east-1.rds.amazonaws.com
DB_USERNAME=root
DB_PASSWORD=diego1416
DB_NAME=euler_db
DB_PORT=3306
SECRET_KEY=tu_clave_secreta_muy_segura_aqui
```

### 4. Inicializar base de datos

```bash
python create_database.py
```

### 5. Construir assets frontend

```bash
npm install
npm run build
```

### 6. Ejecutar aplicación

```bash
python app.py
```

La aplicación estará disponible en: http://127.0.0.1:5000

## 📁 Estructura del Proyecto
```
EULER PW/
├── app.py                 # Flask app principal
├── package.json           # Configuración de npm y scripts
├── vite.config.js         # Configuración de Vite
├── tailwind.config.js     # Configuración de Tailwind v4
├── postcss.config.cjs     # Configuración de PostCSS
├── src/
│   ├── main.js           # Entry point de JavaScript
│   └── index.css         # Entry point de CSS con Tailwind
├── templates/
│   └── index.html        # Template Flask con carga condicional
└── static/dist/          # Assets compilados (generado por build)
```

### 2. Comandos de Instalación
```bash
# Instalar dependencias (ya ejecutado)
npm install -D vite@7.2.2 tailwindcss@4.1.17 postcss autoprefixer @tailwindcss/postcss
```

### 3. Comandos de Desarrollo

#### Modo Desarrollo (Hot Reload)
```bash
# Terminal 1: Servidor Vite (hot reload de CSS/JS)
npm run dev

# Terminal 2: Servidor Flask con VITE_DEV activado
$env:VITE_DEV="1"; python app.py
```
Abre http://localhost:5000 (Flask sirve HTML, Vite sirve CSS/JS con hot reload)

#### Modo Producción
```bash
# 1. Compilar assets
npm run build

# 2. Ejecutar Flask (sin VITE_DEV)
python app.py
```

### 4. Cómo Funciona la Integración

**En desarrollo** (`VITE_DEV=1`):
- Flask sirve HTML desde `templates/index.html`
- Vite dev server sirve CSS/JS desde http://localhost:5173
- Hot reload automático

**En producción** (sin `VITE_DEV`):  
- `npm run build` genera archivos en `static/dist/assets/`
- Flask sirve HTML + assets estáticos compilados
- CSS/JS optimizados para producción

### 5. Verificación
✅ **Instalación exitosa** - Dependencias instaladas sin vulnerabilidades  
✅ **Build exitoso** - Assets generados en `static/dist/assets/`  
✅ **Flask funcionando** - Servidor ejecutándose en http://127.0.0.1:5000  
✅ **Tailwind configurado** - Estilos aplicados al template

### 6. Problemas Resueltos
- ❌ **Inicial**: Tailwind v4 requiere configuración diferente a v3
- ✅ **Solucionado**: Usar `@import "tailwindcss"` en lugar de `@tailwind`  
- ✅ **Solucionado**: Configurar `@tailwindcss/postcss` plugin
- ✅ **Solucionado**: Corregir rutas de configuración en CSS
- ✅ **Solucionado**: Agregar `"type": "module"` en package.json

## Comandos Rápidos

```bash
# Desarrollo
npm run dev & $env:VITE_DEV="1"; python app.py

# Producción  
npm run build && python app.py

# Preview de build
npm run preview
```