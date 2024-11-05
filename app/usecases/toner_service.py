from sqlalchemy.orm import Session
from app.interfaces.schemas import TonerBulkCreate, TonerUpdate
from app.infrastructure.repositories import TonerRepository
from uuid import UUID

def registrar_toners(db: Session, toners: TonerBulkCreate):
    repository = TonerRepository(db)
    repository.create_bulk(toners.toners)

def buscar_toner(db: Session, id: UUID):
    repository = TonerRepository(db)
    return repository.buscar_toner(id)  # Llama al método en el repositorio

def actualizar_toner(db: Session, id: UUID, toner: TonerUpdate):
    repository = TonerRepository(db)
    return repository.actualizar_toner(id, toner)  # Asegúrate de pasar ambos argumentos

def eliminar_toner(db: Session, id: UUID):
    repository = TonerRepository(db)
    return repository.eliminar_toner(id)  # Llama al método en el repositorio