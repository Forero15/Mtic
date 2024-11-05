from sqlalchemy.orm import Session
from app.interfaces.schemas import SedeBulkCreate, SedeUpdate
from app.infrastructure.repositories import SedeRepository
from uuid import UUID

def registrar_sedes(db: Session, sedes: SedeBulkCreate):
    repository = SedeRepository(db)
    repository.create_bulk(sedes.sedes)

def buscar_sede(db: Session, id: UUID):
    repository = SedeRepository(db)
    return repository.buscar_sede(id)  # Llama al método en el repositorio

def actualizar_sede(db: Session, id: UUID, sede: SedeUpdate):
    repository = SedeRepository(db)
    return repository.actualizar_sede(id, sede)  # Asegúrate de pasar ambos argumentos

def eliminar_sede(db: Session, id: UUID):
    repository = SedeRepository(db)
    return repository.eliminar_sede(id)  # Llama al método en el repositorio