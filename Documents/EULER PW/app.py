from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import datetime
from dotenv import load_dotenv
import pymysql

# Cargar variables de entorno
load_dotenv()

# Instalar PyMySQL como MySQLdb
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Configuración de la base de datos
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key_change_in_production')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelos de Base de Datos
class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True)
    telefono = db.Column(db.String(20))
    whatsapp = db.Column(db.String(20))
    fecha_nacimiento = db.Column(db.Date)
    grado_estudio = db.Column(db.String(50))
    institucion_educativa = db.Column(db.String(200))
    direccion = db.Column(db.Text)
    distrito = db.Column(db.String(100))
    provincia = db.Column(db.String(100))
    departamento = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    activo = db.Column(db.Boolean, default=True)

class Programa(db.Model):
    __tablename__ = 'programas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio_mensual = db.Column(db.Numeric(8, 2))
    duracion_meses = db.Column(db.Integer)
    modalidad = db.Column(db.Enum('virtual', 'presencial', 'hibrida', name='modalidad_enum'), default='virtual')
    nivel_academico = db.Column(db.Enum('primaria', 'secundaria', 'preuniversitario', 'universitario', name='nivel_enum'), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

class Contacto(db.Model):
    __tablename__ = 'contactos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    programa_interes = db.Column(db.String(100))
    mensaje = db.Column(db.Text)
    origen = db.Column(db.Enum('formulario_web', 'whatsapp', 'facebook', 'instagram', 'referido', name='origen_enum'), default='formulario_web')
    estado = db.Column(db.Enum('nuevo', 'contactado', 'interesado', 'inscrito', 'no_interesado', name='estado_enum'), default='nuevo')
    fecha_contacto = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_seguimiento = db.Column(db.DateTime)
    observaciones = db.Column(db.Text)

class Profesor(db.Model):
    __tablename__ = 'profesores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True)
    telefono = db.Column(db.String(20))
    especialidad = db.Column(db.String(200))
    experiencia_anos = db.Column(db.Integer)
    grado_academico = db.Column(db.String(150))
    biografia = db.Column(db.Text)
    foto_url = db.Column(db.String(500))
    activo = db.Column(db.Boolean, default=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

def get_base_context():
    """Contexto base para todos los templates"""
    return {
        'vite_dev': os.environ.get('VITE_DEV', '0') in ('1', 'true', 'True'),
        'current_year': datetime.now().year
    }

@app.route('/')
def index():
    return render_template('index.html', **get_base_context())

@app.route('/programas/beca18')
def beca18():
    return render_template('programas/beca18.html', **get_base_context())

@app.route('/programas/preuniversitario')
def preuniversitario():
    return render_template('programas/preuniversitario.html', **get_base_context())

@app.route('/programas/matematicas')
def matematicas():
    return render_template('programas/matematicas.html', **get_base_context())

@app.route('/programas/ciencias')
def ciencias():
    return render_template('programas/ciencias.html', **get_base_context())

@app.route('/horarios')
def horarios():
    return render_template('pages/horarios.html', **get_base_context())

@app.route('/inscripciones')
def inscripciones():
    return render_template('pages/inscripciones.html', **get_base_context())

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombres = request.form.get('nombres')
            telefono = request.form.get('telefono')
            programa_interes = request.form.get('programa_interes')
            mensaje = request.form.get('mensaje')
            
            # Crear nuevo contacto
            nuevo_contacto = Contacto(
                nombres=nombres,
                telefono=telefono,
                programa_interes=programa_interes,
                mensaje=mensaje,
                origen='formulario_web'
            )
            
            # Guardar en la base de datos
            db.session.add(nuevo_contacto)
            db.session.commit()
            
            flash('¡Gracias por contactarnos! Te responderemos pronto por WhatsApp.', 'success')
            return redirect(url_for('contacto'))
            
        except Exception as e:
            db.session.rollback()
            flash('Hubo un error al enviar tu mensaje. Por favor intenta de nuevo.', 'error')
            print(f"Error: {e}")
    
    return render_template('pages/contacto.html', **get_base_context())

@app.route('/nosotros')
def nosotros():
    return render_template('pages/nosotros.html', **get_base_context())

# API endpoints
@app.route('/api/programas')
def api_programas():
    """Obtener lista de programas activos"""
    try:
        programas = Programa.query.filter_by(activo=True).all()
        return jsonify([{
            'id': p.id,
            'nombre': p.nombre,
            'descripcion': p.descripcion,
            'precio_mensual': float(p.precio_mensual) if p.precio_mensual else None,
            'duracion_meses': p.duracion_meses,
            'modalidad': p.modalidad,
            'nivel_academico': p.nivel_academico
        } for p in programas])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contactos')
def api_contactos():
    """Obtener lista de contactos (solo para admin)"""
    try:
        contactos = Contacto.query.order_by(Contacto.fecha_contacto.desc()).limit(50).all()
        return jsonify([{
            'id': c.id,
            'nombres': c.nombres,
            'telefono': c.telefono,
            'programa_interes': c.programa_interes,
            'mensaje': c.mensaje,
            'estado': c.estado,
            'fecha_contacto': c.fecha_contacto.isoformat() if c.fecha_contacto else None
        } for c in contactos])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Función para inicializar la base de datos
def init_db():
    """Inicializar la base de datos y crear tablas"""
    try:
        with app.app_context():
            db.create_all()
            print("✅ Base de datos inicializada correctamente")
            
            # Verificar si ya hay programas, si no, crear los datos iniciales
            if Programa.query.count() == 0:
                programas_iniciales = [
                    Programa(nombre='MATECERO (Primaria)', descripcion='Programa de matemáticas para estudiantes de primaria', precio_mensual=80.00, duracion_meses=12, nivel_academico='primaria'),
                    Programa(nombre='BÁSICO (1° - 2° Secundaria)', descripcion='Programa integral para estudiantes de 1° y 2° de secundaria', precio_mensual=100.00, duracion_meses=12, nivel_academico='secundaria'),
                    Programa(nombre='INTERMEDIO (3° - 4° Secundaria)', descripcion='Programa avanzado para estudiantes de 3° y 4° de secundaria', precio_mensual=120.00, duracion_meses=12, nivel_academico='secundaria'),
                    Programa(nombre='PREUNIVERSITARIO', descripcion='Preparación intensiva para el ingreso a universidades', precio_mensual=150.00, duracion_meses=10, nivel_academico='preuniversitario'),
                    Programa(nombre='BECA 18', descripcion='Programa especializado para postular a la Beca 18', precio_mensual=130.00, duracion_meses=8, nivel_academico='preuniversitario'),
                    Programa(nombre='MATEMÁTICAS', descripcion='Curso especializado en matemáticas para todos los niveles', precio_mensual=90.00, duracion_meses=6, nivel_academico='secundaria'),
                    Programa(nombre='CIENCIAS', descripcion='Programa integral de ciencias: física, química y biología', precio_mensual=110.00, duracion_meses=12, nivel_academico='secundaria')
                ]
                
                for programa in programas_iniciales:
                    db.session.add(programa)
                
                db.session.commit()
                print("✅ Datos iniciales de programas creados")
                
    except Exception as e:
        print(f"❌ Error al inicializar la base de datos: {e}")

if __name__ == '__main__':
    # Inicializar la base de datos
    init_db()
    
    # Ejecutar la aplicación
    app.run(debug=True) 