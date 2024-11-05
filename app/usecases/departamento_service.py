from sqlalchemy.orm import Session
from app.interfaces.schemas import DepartamentoBulkCreate, DepartamentoUpdate
from app.infrastructure.repositories import DepartamentoRepository
from uuid import UUID

def registrar_departamentos(db: Session, departamentos: DepartamentoBulkCreate):
    repository = DepartamentoRepository(db)
    repository.create_bulk(departamentos.departamentos)

def actualizar_departamento(db: Session, id: str, departamento: DepartamentoUpdate):
    repository = DepartamentoRepository(db)
    return repository.actualizar_departamento(id, departamento)  # Asegúrate de pasar ambos argumentos

def buscar_departamento(db: Session, id: str):
    repository = DepartamentoRepository(db)
    return repository.buscar_departamento(id)

def eliminar_departamento(db: Session, id: UUID):  # Asegúrate de que el tipo de id sea UUID
    repository = DepartamentoRepository(db)
    return repository.eliminar_departamento(id)  # Aquí se pasa el id correctamente