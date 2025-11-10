#!/usr/bin/env python3
"""
Script para crear la base de datos euler_db en MySQL RDS
"""
import pymysql
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

def crear_base_de_datos():
    try:
        # Conectar a MySQL sin especificar base de datos
        conn = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            port=int(os.getenv('DB_PORT', 3306))
        )
        
        cursor = conn.cursor()
        
        # Crear la base de datos
        cursor.execute('CREATE DATABASE IF NOT EXISTS euler_db;')
        print("✅ Base de datos 'euler_db' creada exitosamente")
        
        # Verificar que se creó
        cursor.execute('SHOW DATABASES;')
        databases = cursor.fetchall()
        print("📋 Bases de datos disponibles:")
        for db in databases:
            print(f"   - {db[0]}")
        
        conn.commit()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Error al crear la base de datos: {e}")
        return False

if __name__ == "__main__":
    print("🔄 Creando base de datos MySQL...")
    if crear_base_de_datos():
        print("🎉 ¡Listo! Ahora puedes ejecutar 'python app.py'")
    else:
        print("💥 Hubo un problema. Verifica tus credenciales de MySQL.")