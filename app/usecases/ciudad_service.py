from sqlalchemy.orm import Session
from app.interfaces.schemas import CiudadBulkCreate, CiudadUpdate
from app.infrastructure.repositories import CiudadRepository
from uuid import UUID

def registrar_ciudades(db: Session, ciudades: CiudadBulkCreate):
    repository = CiudadRepository(db)
    repository.create_bulk(ciudades.ciudades)

def buscar_ciudad(db: Session, id: UUID):
    repository = CiudadRepository(db)
    return repository.buscar_ciudad(id)  # Llama al método en el repositorio

def actualizar_ciudad(db: Session, id: UUID, ciudad: CiudadUpdate):
    repository = CiudadRepository(db)
    return repository.actualizar_ciudad(id, ciudad)  # Asegúrate de pasar ambos argumentos

def eliminar_ciudad(db: Session, id: UUID):
    repository = CiudadRepository(db)
    return repository.eliminar_ciudad(id)  # Llama al método en el repositorio