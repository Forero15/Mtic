from sqlalchemy.orm import Session
from app.interfaces.schemas import EmpresaBulkCreate, EmpresaUpdate, EmpresaCreate
from app.infrastructure.repositories import EmpresaRepository
from uuid import UUID

def registrar_empresas(db: Session, empresas: EmpresaBulkCreate):
    repository = EmpresaRepository(db)
    repository.create_bulk(empresas.empresas)

def listar_empresas(db: Session):
    repository = EmpresaRepository(db)
    return repository.list()  # Llama al método de listar empresas en el repositorio

def buscar_empresa(db: Session, id: UUID):
    repository = EmpresaRepository(db)
    return repository.buscar_empresa(id)  # Llama al método en el repositorio

def actualizar_empresa(db: Session, id: UUID, empresa: EmpresaUpdate):
    repository = EmpresaRepository(db)
    return repository.actualizar_empresa(id, empresa)  # Asegúrate de pasar ambos argumentos

def eliminar_empresa(db: Session, id: UUID):
    repository = EmpresaRepository(db)
    return repository.eliminar_empresa(id)  # Llama al método en el repositorio