from sqlalchemy.orm import Session
from app.interfaces.schemas import ImpresoraBulkCreate, ImpresoraUpdate
from app.infrastructure.repositories import ImpresoraRepository
from uuid import UUID

def registrar_impresoras(db: Session, impresoras: ImpresoraBulkCreate):
    repository = ImpresoraRepository(db)
    repository.create_bulk(impresoras.impresoras)

def buscar_impresora(db: Session, id: UUID):
    repository = ImpresoraRepository(db)
    return repository.buscar_impresora(id)  # Llama al método en el repositorio

def actualizar_impresora(db: Session, id: UUID, impresora: ImpresoraUpdate):
    repository = ImpresoraRepository(db)
    return repository.actualizar_impresora(id, impresora)  # Asegúrate de pasar ambos argumentos

def eliminar_impresora(db: Session, id: UUID):
    repository = ImpresoraRepository(db)
    return repository.eliminar_impresora(id)  # Llama al método en el repositorio