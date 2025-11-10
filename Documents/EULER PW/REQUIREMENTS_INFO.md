# 📋 ARCHIVOS DE REQUERIMIENTOS CREADOS

## 📦 Dependencias Python

### `requirements.txt` (Producción)
Contiene todas las dependencias necesarias para ejecutar la aplicación:

- **Flask 3.0.0** - Framework web principal
- **Flask-SQLAlchemy 3.1.1** - ORM para base de datos  
- **Flask-Migrate 4.0.5** - Migraciones de BD
- **PyMySQL 1.1.0** - Conector MySQL
- **mysql-connector-python 8.2.0** - Driver MySQL oficial
- **python-dotenv 1.0.0** - Variables de entorno
- **psycopg2-binary 2.9.9** - PostgreSQL (opcional)

### `requirements-dev.txt` (Desarrollo)
Incluye dependencias adicionales para desarrollo:

- **pytest** - Testing framework
- **black** - Formateo de código
- **flake8** - Linting
- **flask-debugtoolbar** - Herramientas de debug

### `setup.py` (Script de configuración)
Script automatizado que:

1. ✅ Verifica versión de Python (3.8+)
2. ✅ Detecta entorno virtual activo  
3. ✅ Instala dependencias desde requirements.txt
4. ✅ Verifica conexión a base de datos MySQL
5. ✅ Proporciona instrucciones de uso

## 🚀 Instalación

### Opción 1: Automática (Recomendada)
```bash
# Activar entorno virtual
venv\Scripts\activate

# Ejecutar script de configuración
python setup.py
```

### Opción 2: Manual
```bash
# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias de producción
pip install -r requirements.txt

# Instalar dependencias de desarrollo (opcional)
pip install -r requirements-dev.txt
```

### Opción 3: Dependencias específicas
```bash
# Solo las esenciales para Flask + MySQL
pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv

# Solo para desarrollo local
pip install Flask mysql-connector-python
```

## 🔧 Verificación de instalación

```bash
# Verificar que Flask está instalado
python -c "import flask; print(f'Flask {flask.__version__}')"

# Verificar conexión MySQL  
python -c "import pymysql; print('PyMySQL OK')"

# Ejecutar script de verificación completa
python setup.py
```

## 📊 Compatibilidad

- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12
- **MySQL**: 5.7+, 8.0+ (AWS RDS compatible)
- **PostgreSQL**: 12+ (opcional)
- **Windows**: ✅ Completamente compatible
- **macOS/Linux**: ✅ Compatible (ajustar rutas en scripts)

## 🚨 Solución de problemas comunes

### Error: "No module named 'pymysql'"
```bash
pip install pymysql mysql-connector-python
```

### Error: "Access denied for user"
- Verificar credenciales en archivo `.env`
- Comprobar conectividad a AWS RDS

### Error: "Unknown database 'euler_db'"
```bash
python create_database.py
```

### Error: "Flask command not found"  
- Verificar que el entorno virtual esté activo
- Reinstalar Flask: `pip install Flask`

## 📧 Soporte

Si tienes problemas con la instalación:

1. Verificar que Python 3.8+ esté instalado
2. Activar entorno virtual (`venv\Scripts\activate`)
3. Ejecutar `python setup.py` para diagnóstico automático
4. Revisar logs de error en la terminal

---

**Nota**: Todos los archivos de requerimientos están optimizados para el proyecto Grupo de Ciencias Veen Euler y han sido probados en el entorno de desarrollo actual.