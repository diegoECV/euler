-- Esquema de base de datos para Grupo de Ciencias Veen Euler

-- Tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    whatsapp VARCHAR(20),
    fecha_nacimiento DATE,
    grado_estudio VARCHAR(50),
    institucion_educativa VARCHAR(200),
    direccion TEXT,
    distrito VARCHAR(100),
    provincia VARCHAR(100),
    departamento VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_email (email),
    INDEX idx_telefono (telefono),
    INDEX idx_whatsapp (whatsapp)
);

-- Tabla de programas educativos
CREATE TABLE IF NOT EXISTS programas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio_mensual DECIMAL(8,2),
    duracion_meses INT,
    modalidad ENUM('virtual', 'presencial', 'hibrida') DEFAULT 'virtual',
    nivel_academico ENUM('primaria', 'secundaria', 'preuniversitario', 'universitario') NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de inscripciones
CREATE TABLE IF NOT EXISTS inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT NOT NULL,
    programa_id INT NOT NULL,
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('pendiente', 'activo', 'pausado', 'completado', 'cancelado') DEFAULT 'pendiente',
    fecha_inicio DATE,
    fecha_fin DATE,
    precio_acordado DECIMAL(8,2),
    descuento_aplicado DECIMAL(5,2) DEFAULT 0,
    observaciones TEXT,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id) ON DELETE CASCADE,
    FOREIGN KEY (programa_id) REFERENCES programas(id) ON DELETE RESTRICT,
    INDEX idx_estudiante (estudiante_id),
    INDEX idx_programa (programa_id),
    INDEX idx_estado (estado)
);

-- Tabla de contactos/leads
CREATE TABLE IF NOT EXISTS contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    programa_interes VARCHAR(100),
    mensaje TEXT,
    origen ENUM('formulario_web', 'whatsapp', 'facebook', 'instagram', 'referido') DEFAULT 'formulario_web',
    estado ENUM('nuevo', 'contactado', 'interesado', 'inscrito', 'no_interesado') DEFAULT 'nuevo',
    fecha_contacto TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_seguimiento TIMESTAMP NULL,
    observaciones TEXT,
    INDEX idx_telefono (telefono),
    INDEX idx_estado (estado),
    INDEX idx_fecha_contacto (fecha_contacto)
);

-- Tabla de profesores
CREATE TABLE IF NOT EXISTS profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    especialidad VARCHAR(200),
    experiencia_anos INT,
    grado_academico VARCHAR(150),
    biografia TEXT,
    foto_url VARCHAR(500),
    activo BOOLEAN DEFAULT TRUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de horarios
CREATE TABLE IF NOT EXISTS horarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    programa_id INT NOT NULL,
    profesor_id INT NOT NULL,
    dia_semana ENUM('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo') NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    aula_virtual VARCHAR(200),
    link_clase TEXT,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (programa_id) REFERENCES programas(id) ON DELETE CASCADE,
    FOREIGN KEY (profesor_id) REFERENCES profesores(id) ON DELETE RESTRICT,
    INDEX idx_programa (programa_id),
    INDEX idx_profesor (profesor_id),
    INDEX idx_dia (dia_semana)
);

-- Tabla de pagos
CREATE TABLE IF NOT EXISTS pagos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    inscripcion_id INT NOT NULL,
    monto DECIMAL(8,2) NOT NULL,
    fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metodo_pago ENUM('efectivo', 'transferencia', 'yape', 'plin', 'tarjeta') NOT NULL,
    numero_transaccion VARCHAR(100),
    estado ENUM('pendiente', 'confirmado', 'rechazado') DEFAULT 'pendiente',
    mes_correspondiente DATE,
    observaciones TEXT,
    FOREIGN KEY (inscripcion_id) REFERENCES inscripciones(id) ON DELETE CASCADE,
    INDEX idx_inscripcion (inscripcion_id),
    INDEX idx_fecha_pago (fecha_pago),
    INDEX idx_estado (estado)
);

-- Insertar datos iniciales de programas
INSERT INTO programas (nombre, descripcion, precio_mensual, duracion_meses, modalidad, nivel_academico) VALUES
('MATECERO (Primaria)', 'Programa de matemáticas para estudiantes de primaria, enfocado en fortalecer las bases matemáticas de forma divertida y didáctica.', 80.00, 12, 'virtual', 'primaria'),
('BÁSICO (1° - 2° Secundaria)', 'Programa integral para estudiantes de 1° y 2° de secundaria, cubriendo matemáticas y ciencias básicas.', 100.00, 12, 'virtual', 'secundaria'),
('INTERMEDIO (3° - 4° Secundaria)', 'Programa avanzado para estudiantes de 3° y 4° de secundaria, preparándolos para el nivel preuniversitario.', 120.00, 12, 'virtual', 'secundaria'),
('PREUNIVERSITARIO', 'Preparación intensiva para el ingreso a universidades nacionales y particulares. Incluye todas las materias del examen de admisión.', 150.00, 10, 'virtual', 'preuniversitario'),
('BECA 18', 'Programa especializado para postular a la Beca 18, con preparación específica para el examen de admisión y orientación vocacional.', 130.00, 8, 'virtual', 'preuniversitario'),
('MATEMÁTICAS', 'Curso especializado en matemáticas para todos los niveles, desde básico hasta avanzado.', 90.00, 6, 'virtual', 'secundaria'),
('CIENCIAS', 'Programa integral de ciencias que incluye física, química y biología para estudiantes de secundaria.', 110.00, 12, 'virtual', 'secundaria');

-- Insertar datos de ejemplo de profesores
INSERT INTO profesores (nombres, apellidos, email, telefono, especialidad, experiencia_anos, grado_academico, biografia) VALUES
('Carlos Alberto', 'Ramírez Vega', 'carlos.ramirez@gcveeneuler.edu.pe', '964266259', 'Matemáticas y Física', 8, 'Ingeniero Matemático - UNMSM', 'Especialista en matemáticas con amplia experiencia en preparación preuniversitaria y olimpiadas matemáticas.'),
('María Elena', 'Gonzales Torres', 'maria.gonzales@gcveeneuler.edu.pe', '964266260', 'Química y Biología', 6, 'Química Farmacéutica - UNMSM', 'Experta en ciencias naturales con metodología innovadora para la enseñanza virtual.'),
('José Luis', 'Mendoza Silva', 'jose.mendoza@gcveeneuler.edu.pe', '964266261', 'Física y Matemáticas', 10, 'Físico - UNI', 'Docente especializado en física y matemáticas aplicadas, con experiencia en preparación para ingreso a universidades de ingeniería.'),
('Ana Patricia', 'Flores Huamán', 'ana.flores@gcveeneuler.edu.pe', '964266262', 'Matemáticas Primaria', 5, 'Educación Primaria - PUCP', 'Especialista en educación primaria con enfoque en matemáticas lúdicas y metodologías activas.');
