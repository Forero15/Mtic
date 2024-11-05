from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
import uuid
from uuid import UUID
from typing import List

class UsuarioBase(BaseModel):
    nombre: str
    cedula: int
    correo: EmailStr
    celular: str

class UsuarioCreate(UsuarioBase):
    contraseña: str

class Usuario(UsuarioCreate):
    id: UUID
    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    cedula: Optional[str] = None
    correo: Optional[str] = None  # Asegúrate de que este campo esté presente
    celular: Optional[str] = None
    contraseña: Optional[str] = None  # Agregar campo para la nueva contraseña

class Empresa(BaseModel):
    id: UUID  # Asegúrate de que este campo esté presente
    nombre_empresa: str
    email: EmailStr
    nit: str
    numero_contacto: str
    sede: bool

class EmpresaCreate(BaseModel):
    nombre_empresa: str
    email: EmailStr
    nit: str
    numero_contacto: str
    sede: bool

class EmpresaUpdate(BaseModel):
    nombre_empresa: Optional[str] = None  # Campo opcional para la actualización
    email: Optional[EmailStr] = None  # Campo opcional para la actualización
    nit: Optional[str] = None  # Campo opcional para la actualización
    numero_contacto: Optional[str] = None  # Campo opcional para la actualización
    sede: Optional[bool] = None  # Campo opcional para la actualización

class Empresa(EmpresaCreate):
    id: UUID

    class Config:
        orm_mode = True

class EmpresaBulkCreate(BaseModel):
    empresas: List[EmpresaCreate]

class SedeUpdate(BaseModel):
    nombre_sede: Optional[str] = None
    email: Optional[str] = None
    empresa_id: Optional[uuid.UUID] = None
    numero_contacto: Optional[str] = None
    departamento_id: Optional[uuid.UUID] = None
    ciudad_id: Optional[uuid.UUID] = None

class DepartamentoCreate(BaseModel):
    nombre_departamento: str  # Agregar definición de la clase

class Departamento(BaseModel):
    id: UUID  # Asegúrate de que este campo esté presente
    nombre_departamento: str



class DepartamentoBulkCreate(BaseModel):
    departamentos: List[DepartamentoCreate]

class DepartamentoUpdate(BaseModel):
    id: Optional[UUID] = None  # Asegúrate de que este campo esté presente
    nombre_departamento: Optional[str] = None

class Ciudad(BaseModel):
    id: UUID  # Asegúrate de que este campo esté presente
    nombre_ciudad: str
    departamento_id: UUID  # Asegúrate de que este campo esté presente

class CiudadCreate(BaseModel):
    nombre_ciudad: str
    departamento_id: uuid.UUID

class CiudadBulkCreate(BaseModel):
    ciudades: List[CiudadCreate]

class CiudadUpdate(BaseModel):
    nombre_ciudad: Optional[str] = None  # Campo opcional para la actualización
    departamento_id: Optional[UUID] = None  # Campo opcional para la actualización

class Sede(BaseModel):
    id: UUID  # Asegúrate de que este campo esté presente
    nombre_sede: str
    email: EmailStr
    numero_contacto: str
    departamento_id: UUID  # Asegúrate de que este campo esté presente
    ciudad_id: UUID  # Asegúrate de que este campo esté presente

class SedeCreate(BaseModel):
    nombre_sede: str
    email: str
    empresa_id: uuid.UUID  # Cambiado de nit a empresa_id
    numero_contacto: str
    departamento_id: uuid.UUID
    ciudad_id: uuid.UUID

class SedeBulkCreate(BaseModel):
    sedes: List[SedeCreate]

class SedeUpdate(BaseModel):
    nombre_sede: Optional[str] = None  # Campo opcional para la actualización
    email: Optional[EmailStr] = None  # Campo opcional para la actualización
    numero_contacto: Optional[str] = None  # Campo opcional para la actualización
    departamento_id: Optional[UUID] = None  # Campo opcional para la actualización
    ciudad_id: Optional[UUID] = None  # Campo opcional para la actualización

class ImpresoraCreate(BaseModel):
    marca: str
    modelo: str
    serial: str
    estado: str
    empresa_id: uuid.UUID = None  # Solo si está en estado 'asignada' o 'en reparación'
    sede_id: uuid.UUID = None      # Solo si cuenta con empresa registrada

class Impresora(BaseModel):
    id: UUID  # Asegúrate de que este campo esté presente
    marca: str
    modelo: str
    serial: str
    estado: str
    empresa_id: UUID  # Asegúrate de que este campo esté presente
    sede_id: UUID  # Asegúrate de que este campo esté presente


class ImpresoraBulkCreate(BaseModel):
    impresoras: List[ImpresoraCreate]

class ImpresoraUpdate(BaseModel):
    marca: Optional[str] = None  # Campo opcional para la actualización
    modelo: Optional[str] = None  # Campo opcional para la actualización
    serial: Optional[str] = None  # Campo opcional para la actualización
    estado: Optional[str] = None  # Campo opcional para la actualización
    empresa_id: Optional[UUID] = None  # Campo opcional para la actualización
    sede_id: Optional[UUID] = None  # Campo opcional para la actualización

class Toner(BaseModel):
    id: UUID  # Asegúrate de que este campo esté presente
    referencia: str
    estado: str
    empresa_id: UUID  # Asegúrate de que este campo esté presente
    sede_id: UUID  # Asegúrate de que este campo esté presente

class TonerCreate(BaseModel):
    referencia: str
    estado: str
    empresa_id: uuid.UUID = None  # Solo si está en estado 'asignada' o 'en reparación'
    sede_id: uuid.UUID = None      # Solo si cuenta con empresa registrada

class TonerBulkCreate(BaseModel):
    toners: List[TonerCreate]

class TonerUpdate(BaseModel):
    referencia: Optional[str] = None  # Campo opcional para la actualización
    estado: Optional[str] = None  # Campo opcional para la actualización
    empresa_id: Optional[UUID] = None  # Campo opcional para la actualización
    sede_id: Optional[UUID] = None  # Campo opcional para la actualización
