from fastapi import FastAPI, Depends, Form, HTTPException
from sqlalchemy.orm import Session
import uuid
from uuid import UUID
from typing import List
from app.infrastructure.database import engine, SessionLocal, Base, get_db
from app.interfaces import schemas
from app.interfaces.schemas import UsuarioCreate, EmpresaBulkCreate, SedeBulkCreate, ImpresoraBulkCreate, DepartamentoBulkCreate, CiudadBulkCreate,TonerBulkCreate, UsuarioUpdate,DepartamentoUpdate    
from app.usecases import usuario_service ,empresa_service, sede_service, impresora_service, departamento_service, ciudad_service, toner_service
from app.usecases.usuario_service import (crear_usuario,actualizar_usuario,eliminar_usuario,buscar_usuario,listar_usuarios)
from app.usecases.departamento_service import ( actualizar_departamento, buscar_departamento,eliminar_departamento)
from app.usecases.impresora_service import registrar_impresoras, buscar_impresora, actualizar_impresora, eliminar_impresora
from app.usecases.toner_service import registrar_toners, buscar_toner, actualizar_toner, eliminar_toner
from app.usecases.empresa_service import registrar_empresas, listar_empresas,buscar_empresa, actualizar_empresa, eliminar_empresa
from app.usecases.sede_service import registrar_sedes, buscar_sede, actualizar_sede, eliminar_sede
from app.usecases.departamento_service import registrar_departamentos
from app.usecases.ciudad_service import (registrar_ciudades, buscar_ciudad, actualizar_ciudad, eliminar_ciudad)
from app.infrastructure.repositories import (DepartamentoRepository,CiudadRepository,SedeRepository,ImpresoraRepository,TonerRepository)
# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para crear usuarios
@app.post("/usuarios/", response_model=schemas.Usuario)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.crear_usuario(db, usuario)

# Endpoint para listar usuarios
@app.get("/usuarios/", response_model=List[schemas.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return usuario_service.listar_usuarios(db)

@app.put("/usuarios/{id}", response_model=UsuarioUpdate)
def actualizar_usuario_endpoint(id: uuid.UUID, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    updated_user = actualizar_usuario(db, id, usuario)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated_user

@app.delete("/usuarios/{id}")
def eliminar_usuario_endpoint(id: uuid.UUID, db: Session = Depends(get_db)):
    if not eliminar_usuario(db, id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado"}

@app.get("/usuarios/{id}", response_model=UsuarioUpdate)
def buscar_usuario_endpoint(id: uuid.UUID, db: Session = Depends(get_db)):
    user = buscar_usuario(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Endpoint para crear empresas en bulk
@app.post("/empresas/bulk/")
def registrar_empresas_endpoint(empresas: EmpresaBulkCreate, db: Session = Depends(get_db)):
    registrar_empresas(db, empresas)
    return {"message": "Empresas registradas exitosamente"}

# Endpoint para listar empresas
@app.get("/empresas/")
def listar_empresas_endpoint(db: Session = Depends(get_db)):
    return listar_empresas(db)  # Llama a la función listar_empresas

# Endpoint para buscar una empresa por ID
@app.get("/empresas/{id}", response_model=schemas.Empresa)
def buscar_empresa_endpoint(id: UUID, db: Session = Depends(get_db)):
    empresa = buscar_empresa(db, id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa

# Endpoint para actualizar una empresa
@app.put("/empresas/{id}", response_model=schemas.Empresa)
def actualizar_empresa_endpoint(id: UUID, empresa: schemas.EmpresaUpdate, db: Session = Depends(get_db)):
    updated_empresa = actualizar_empresa(db, id, empresa)
    if not updated_empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return updated_empresa

# Endpoint para eliminar una empresa
@app.delete("/empresas/{id}")
def eliminar_empresa_endpoint(id: UUID, db: Session = Depends(get_db)):
    if not eliminar_empresa(db, id):
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return {"detail": "Empresa eliminada"}

# Endpoint para registrar departamentos en bulk
@app.post("/departamentos/bulk/")
def registrar_departamentos_endpoint(departamentos: DepartamentoBulkCreate, db: Session = Depends(get_db)):
    registrar_departamentos(db, departamentos)
    return {"message": "Departamentos registrados exitosamente"}

@app.get("/departamentos/", response_model=List[schemas.Departamento])
def listar_departamentos(db: Session = Depends(get_db)):
    repository = DepartamentoRepository(db)
    return repository.list()  # Esto debería devolver una lista de objetos Departamento, que incluyen el UUID

@app.put("/departamentos/{id}", response_model=schemas.DepartamentoUpdate)
def actualizar_departamento_endpoint(id: str, departamento: schemas.DepartamentoUpdate, db: Session = Depends(get_db)):
    updated_departamento = actualizar_departamento(db, id, departamento)
    if not updated_departamento:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return updated_departamento

@app.delete("/departamentos/{id}")
def eliminar_departamento_endpoint(id: UUID, db: Session = Depends(get_db)):
    if not eliminar_departamento(db, id):
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return {"detail": "Departamento eliminado"}

# Endpoint para registrar ciudades en bulk
@app.post("/ciudades/bulk/")
def registrar_ciudades_endpoint(ciudades: CiudadBulkCreate, db: Session = Depends(get_db)):
    registrar_ciudades(db, ciudades)
    return {"message": "Ciudades registradas exitosamente"}

# Endpoint para listar ciudades
@app.get("/ciudades/")
def listar_ciudades(db: Session = Depends(get_db)):
    repository = CiudadRepository(db)
    return repository.list()

# Endpoint para buscar una ciudad por ID
@app.get("/ciudades/{id}", response_model=schemas.Ciudad)
def buscar_ciudad_endpoint(id: UUID, db: Session = Depends(get_db)):
    ciudad = buscar_ciudad(db, id)
    if not ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return ciudad

# Endpoint para actualizar una ciudad
@app.put("/ciudades/{id}", response_model=schemas.Ciudad)
def actualizar_ciudad_endpoint(id: UUID, ciudad: schemas.CiudadUpdate, db: Session = Depends(get_db)):
    updated_ciudad = actualizar_ciudad(db, id, ciudad)
    if not updated_ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return updated_ciudad

# Endpoint para eliminar una ciudad
@app.delete("/ciudades/{id}")
def eliminar_ciudad_endpoint(id: UUID, db: Session = Depends(get_db)):
    if not eliminar_ciudad(db, id):
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return {"detail": "Ciudad eliminada"}

# Endpoint para registrar sedes en bulk
@app.post("/sedes/bulk/")
def registrar_sedes_endpoint(sedes: SedeBulkCreate, db: Session = Depends(get_db)):
    registrar_sedes(db, sedes)
    return {"message": "Sedes registradas exitosamente"}

# Endpoint para listar sedes
@app.get("/sedes/")
def listar_sedes(db: Session = Depends(get_db)):
    repository = SedeRepository(db)
    return repository.list()  # Llama al método list para obtener todas las sedes

# Endpoint para buscar una sede por ID
@app.get("/sedes/{id}", response_model=schemas.Sede)
def buscar_sede_endpoint(id: UUID, db: Session = Depends(get_db)):
    sede = buscar_sede(db, id)
    if not sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return sede

# Endpoint para actualizar una sede
@app.put("/sedes/{id}", response_model=schemas.Sede)
def actualizar_sede_endpoint(id: UUID, sede: schemas.SedeUpdate, db: Session = Depends(get_db)):
    updated_sede = actualizar_sede(db, id, sede)
    if not updated_sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return updated_sede

# Endpoint para eliminar una sede
@app.delete("/sedes/{id}")
def eliminar_sede_endpoint(id: UUID, db: Session = Depends(get_db)):
    if not eliminar_sede(db, id):
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return {"detail": "Sede eliminada"}


# Endpoint para registrar impresoras en bulk
@app.post("/impresoras/bulk/")
def registrar_impresoras_endpoint(impresoras: ImpresoraBulkCreate, db: Session = Depends(get_db)):
    registrar_impresoras(db, impresoras)
    return {"message": "Impresoras registradas exitosamente"}

# Endpoint para listar impresoras
@app.get("/impresoras/")
def listar_impresoras(db: Session = Depends(get_db)):
    repository = ImpresoraRepository(db)
    return repository.list()

# Endpoint para buscar una impresora por ID
@app.get("/impresoras/{id}", response_model=schemas.Impresora)
def buscar_impresora_endpoint(id: UUID, db: Session = Depends(get_db)):
    impresora = buscar_impresora(db, id)
    if not impresora:
        raise HTTPException(status_code=404, detail="Impresora no encontrada")
    return impresora

# Endpoint para actualizar una impresora
@app.put("/impresoras/{id}", response_model=schemas.Impresora)
def actualizar_impresora_endpoint(id: UUID, impresora: schemas.ImpresoraUpdate, db: Session = Depends(get_db)):
    updated_impresora = actualizar_impresora(db, id, impresora)
    if not updated_impresora:
        raise HTTPException(status_code=404, detail="Impresora no encontrada")
    return updated_impresora

# Endpoint para eliminar una impresora
@app.delete("/impresoras/{id}")
def eliminar_impresora_endpoint(id: UUID, db: Session = Depends(get_db)):
    if not eliminar_impresora(db, id):
        raise HTTPException(status_code=404, detail="Impresora no encontrada")
    return {"detail": "Impresora eliminada"}

# Endpoint para registrar toners en bulk
@app.post("/toners/bulk/")
def registrar_toners_endpoint(toners: TonerBulkCreate, db: Session = Depends(get_db)):
    registrar_toners(db, toners)
    return {"message": "Toners registrados exitosamente"}

# Endpoint para listar toners
@app.get("/toners/")
def listar_toners(db: Session = Depends(get_db)):
    repository = TonerRepository(db)
    return repository.list()

# Endpoint para buscar un toner por ID
@app.get("/toners/{id}", response_model=schemas.Toner)
def buscar_toner_endpoint(id: UUID, db: Session = Depends(get_db)):
    toner = buscar_toner(db, id)
    if not toner:
        raise HTTPException(status_code=404, detail="Toner no encontrado")
    return toner

# Endpoint para actualizar un toner
@app.put("/toners/{id}", response_model=schemas.Toner)
def actualizar_toner_endpoint(id: UUID, toner: schemas.TonerUpdate, db: Session = Depends(get_db)):
    updated_toner = actualizar_toner(db, id, toner)
    if not updated_toner:
        raise HTTPException(status_code=404, detail="Toner no encontrado")
    return updated_toner

# Endpoint para eliminar un toner
@app.delete("/toners/{id}")
def eliminar_toner_endpoint(id: UUID, db: Session = Depends(get_db)):
    if not eliminar_toner(db, id):
        raise HTTPException(status_code=404, detail="Toner no encontrado")
    return {"detail": "Toner eliminado"}