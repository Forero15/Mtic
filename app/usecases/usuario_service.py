from sqlalchemy.orm import Session
from app.domain import models
import uuid
from app.interfaces.schemas import UsuarioCreate, UsuarioUpdate
from app.infrastructure.repositories import UsuarioRepository  # Asegúrate de que schemas.py esté en el mismo directorio

def crear_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        cedula=usuario.cedula,
        correo=usuario.correo,
        celular=usuario.celular,
        contraseña=usuario.contraseña
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def actualizar_usuario(db: Session, id: str, usuario: UsuarioUpdate):
    return UsuarioRepository.actualizar_usuario(db, id, usuario)

def buscar_usuario(db: Session, nombre: str = None, cedula: str = None, correo: str = None, celular: str = None):
    return UsuarioRepository.buscar_usuario(db, nombre, cedula, correo, celular)

def eliminar_usuario(db: Session, id: str):
    return UsuarioRepository.eliminar_usuario(db, id)

def listar_usuarios(db: Session):
    return db.query(models.Usuario).all()  # Devuelve todos los usuarios
