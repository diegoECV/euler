#!/usr/bin/env python3
"""
Script para verificar e instalar dependencias del proyecto
Grupo de Ciencias Veen Euler - Sistema Web
"""
import subprocess
import sys
import os

def run_command(command):
    """Ejecutar comando y mostrar output"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def check_python_version():
    """Verificar versión de Python"""
    version = sys.version_info
    print(f"🐍 Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 8:
        print("✅ Versión de Python compatible")
        return True
    else:
        print("❌ Se requiere Python 3.8 o superior")
        return False

def check_virtual_env():
    """Verificar si está en un entorno virtual"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Entorno virtual activo")
        return True
    else:
        print("⚠️  No se detectó entorno virtual activo")
        print("   Recomendado: Activar entorno virtual antes de instalar")
        return False

def install_requirements():
    """Instalar dependencias desde requirements.txt"""
    print("\n📦 Instalando dependencias...")
    
    if os.path.exists('requirements.txt'):
        success, output = run_command('pip install -r requirements.txt')
        if success:
            print("✅ Dependencias principales instaladas")
        else:
            print(f"❌ Error al instalar dependencias: {output}")
            return False
    else:
        print("❌ Archivo requirements.txt no encontrado")
        return False
    
    return True

def check_database_connection():
    """Verificar conexión a la base de datos"""
    print("\n🗄️  Verificando conexión a base de datos...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        import pymysql
        
        conn = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USERNAME', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            port=int(os.getenv('DB_PORT', 3306))
        )
        conn.close()
        print("✅ Conexión a MySQL exitosa")
        return True
        
    except Exception as e:
        print(f"❌ Error de conexión a base de datos: {e}")
        print("   Verifica las credenciales en el archivo .env")
        return False

def main():
    """Función principal"""
    print("🚀 Verificando configuración del proyecto Euler PW\n")
    
    # Verificar Python
    if not check_python_version():
        sys.exit(1)
    
    # Verificar entorno virtual
    check_virtual_env()
    
    # Instalar dependencias
    if not install_requirements():
        sys.exit(1)
    
    # Verificar base de datos
    check_database_connection()
    
    print("\n🎉 ¡Configuración completada!")
    print("\n📋 Próximos pasos:")
    print("   1. Verificar archivo .env con credenciales de BD")
    print("   2. Ejecutar: python create_database.py")
    print("   3. Ejecutar: python app.py")
    print("   4. Abrir: http://127.0.0.1:5000")

if __name__ == "__main__":
    main()