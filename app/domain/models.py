from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.infrastructure.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # ID único y autogenerado
    nombre = Column(String, nullable=False)
    cedula = Column(String, unique=True, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    celular = Column(String, nullable=False)
    contraseña = Column(String, nullable=False)

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_empresa = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    nit = Column(String, unique=True, index=True)
    numero_contacto = Column(String)
    sede = Column(Boolean)

class Departamento(Base):
    __tablename__ = "departamentos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_departamento = Column(String, index=True)

class Ciudad(Base):
    __tablename__ = "ciudades"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_ciudad = Column(String, index=True)
    departamento_id = Column(UUID(as_uuid=True), ForeignKey('departamentos.id'))  # Relación con departamento

class Sede(Base):
    __tablename__ = "sedes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_sede = Column(String, index=True)
    email = Column(String)
    empresa_id = Column(UUID(as_uuid=True), ForeignKey('empresas.id'))  # Cambiado de nit a empresa_id
    numero_contacto = Column(String)
    departamento_id = Column(UUID(as_uuid=True), ForeignKey('departamentos.id'))  # Relación con departamento
    ciudad_id = Column(UUID(as_uuid=True), ForeignKey('ciudades.id'))  # Relación con ciudad

class Impresora(Base):
    __tablename__ = "impresoras"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    marca = Column(String)
    modelo = Column(String)
    serial = Column(String)
    estado = Column(String)  # Puede ser 'asignada', 'disponible', 'en reparación'
    empresa_id = Column(UUID(as_uuid=True), ForeignKey('empresas.id'))  # Relación con empresa
    sede_id = Column(UUID(as_uuid=True), ForeignKey('sedes.id'))  # Relación con sede

class Toner(Base):
    __tablename__ = "toners"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    referencia = Column(String, index=True)
    estado = Column(String)  # Puede ser 'asignada', 'disponible', 'en recarga'
    empresa_id = Column(UUID(as_uuid=True), ForeignKey('empresas.id'))  # Relación con empresa
    sede_id = Column(UUID(as_uuid=True), ForeignKey('sedes.id'))  # Relación con sede