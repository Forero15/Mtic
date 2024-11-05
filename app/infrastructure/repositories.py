from sqlalchemy.orm import Session
from app.domain import models
from app.interfaces import schemas
from uuid import UUID
import uuid
import random
import string
from app.domain.models import Usuario, Empresa, Departamento, Ciudad, Sede, Impresora, Toner
from app.interfaces.schemas import UsuarioCreate, EmpresaCreate, DepartamentoCreate, CiudadCreate, SedeCreate, ImpresoraCreate, TonerCreate
from app.interfaces.schemas import UsuarioUpdate, DepartamentoUpdate
from uuid import UUID  # Asegúrate de importar UUID

class UsuarioRepository:
    @staticmethod
    def crear_usuario(db: Session, usuario: schemas.UsuarioCreate) -> models.Usuario:
        contraseña = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        db_usuario = models.Usuario(
            id=str(uuid.uuid4()),
            nombre=usuario.nombre,
            cedula=usuario.cedula,
            correo=usuario.correo,
            celular=usuario.celular,
            contraseña=contraseña
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario

    @staticmethod
    def actualizar_usuario(db: Session, id: str, usuario: schemas.UsuarioUpdate) -> models.Usuario:
        db_usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
        if db_usuario:
            # Actualizar los campos que se proporcionan
            if usuario.nombre is not None:
                db_usuario.nombre = usuario.nombre
            if usuario.cedula is not None:
                db_usuario.cedula = usuario.cedula
            if usuario.correo is not None:
                db_usuario.correo = usuario.correo
            if usuario.celular is not None:
                db_usuario.celular = usuario.celular
            
            db.commit()
            db.refresh(db_usuario)
            return db_usuario
        return None  # Retorna None si no se encuentra el usuario

    @staticmethod
    def buscar_usuario(db: Session, nombre: str = None, cedula: str = None, correo: str = None, celular: str = None) -> list:
        query = db.query(models.Usuario)
        
        # Filtrar por cualquiera de los campos proporcionados
        if nombre:
            query = query.filter(models.Usuario.nombre == nombre)
        if cedula:
            query = query.filter(models.Usuario.cedula == cedula)
        if correo:
            query = query.filter(models.Usuario.correo == correo)
        if celular:
            query = query.filter(models.Usuario.celular == celular)

        return query.all()  # Retorna una lista de usuarios que coinciden


    @staticmethod
    def eliminar_departamento(db: Session, id: UUID):
        departamento = db.query(Departamento).filter(Departamento.id == id).first()  # Busca el departamento
        if not departamento:
            print(f"Departamento con ID {id} no encontrado.")  # Log para depuración
            return False  # Retorna False si no se encuentra
        db.delete(departamento)
        db.commit()
        return True

    def get(self, id: uuid.UUID):
        return self.db.query(Usuario).filter(Usuario.id == id).first()

    @staticmethod
    def listar_usuarios(db: Session):
        return db.query(models.Usuario).all()


class EmpresaRepository:
    def __init__(self, db: Session):
       self.db = db

    def create(self, empresa: EmpresaCreate):
        db_empresa = Empresa(
           nombre_empresa=empresa.nombre_empresa,
            email=empresa.email,
            nit=empresa.nit,
            numero_contacto=empresa.numero_contacto,
            sede=empresa.sede,
        )
        self.db.add(db_empresa)
        self.db.commit()
        self.db.refresh(db_empresa)
        return db_empresa

    def create_bulk(self, empresas: list):
        for empresa in empresas:
           self.create(empresa)

    def list(self):
        return self.db.query(Empresa).all()  # Método para listar EMPRESAS
       
    def buscar_empresa(self, id: UUID):
        return self.db.query(Empresa).filter(Empresa.id == id).first()  # Busca la empresa por ID
       

    def actualizar_empresa(self, id: UUID, empresa: schemas.EmpresaUpdate) -> models.Empresa:
        db_empresa = self.db.query(models.Empresa).filter(models.Empresa.id == id).first()
        if db_empresa:
            if empresa.nombre_empresa is not None:
                db_empresa.nombre_empresa = empresa.nombre_empresa
            if empresa.email is not None:
                db_empresa.email = empresa.email
            if empresa.nit is not None:
                db_empresa.nit = empresa.nit
            if empresa.numero_contacto is not None:
                db_empresa.numero_contacto = empresa.numero_contacto
            if empresa.sede is not None:
                db_empresa.sede = empresa.sede
                
            self.db.commit()
            self.db.refresh(db_empresa)
            return db_empresa
        return None  # Retorna None si no se encuentra la empresa

    def eliminar_empresa(self, id: UUID):
        empresa = self.db.query(Empresa).filter(Empresa.id == id).first()  # Busca la empresa
        if not empresa:
            print(f"Empresa con ID {id} no encontrada.")  # Log para depuración
            return False  # Retorna False si no se encuentra
        self.db.delete(empresa)
        self.db.commit()
        return True
       
       

class DepartamentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, departamento: DepartamentoCreate):
        db_departamento = Departamento(
            nombre_departamento=departamento.nombre_departamento,
        )
        self.db.add(db_departamento)
        self.db.commit()
        self.db.refresh(db_departamento)
        return db_departamento

    def create_bulk(self, departamentos: list):
        for departamento in departamentos:
            self.create(departamento)

    def list(self):  # Método para listar departamentos
        return self.db.query(Departamento).all()  # Esto devolverá todos los departamentos, incluyendo el UUID

    def actualizar_departamento(self, id: str, departamento: schemas.DepartamentoUpdate) -> models.Departamento:
        # Asegúrate de que el ID sea un UUID
        try:
            uuid_id = uuid.UUID(id)  # Convertir a UUID
        except ValueError:
            return None  # Retorna None si el ID no es válido

        db_departamento = self.db.query(models.Departamento).filter(models.Departamento.id == uuid_id).first()
        if db_departamento:
            if departamento.nombre_departamento is not None:
                db_departamento.nombre_departamento = departamento.nombre_departamento
            
            self.db.commit()
            self.db.refresh(db_departamento)
            return db_departamento
        return None  # Retorna None si no se encuentra el departamento
    
    @staticmethod
    def buscar_departamento(db: Session, id: str) -> models.Departamento:
        return db.query(models.Departamento).filter(models.Departamento.id == id).first()

    def eliminar_departamento(self, id: UUID):  # Asegúrate de que el tipo de id sea UUID
        departamento = self.db.query(Departamento).filter(Departamento.id == id).first()  # Busca el departamento
        if not departamento:
            print(f"Departamento con ID {id} no encontrado.")  # Log para depuración
            return False  # Retorna False si no se encuentra
        self.db.delete(departamento)
        self.db.commit()
        return True
    

class CiudadRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, ciudad: CiudadCreate):
        db_ciudad = Ciudad(
            nombre_ciudad=ciudad.nombre_ciudad,
            departamento_id=ciudad.departamento_id,
        )
        self.db.add(db_ciudad)
        self.db.commit()
        self.db.refresh(db_ciudad)
        return db_ciudad

    def create_bulk(self, ciudades: list):
        for ciudad in ciudades:
            self.create(ciudad)
    def list(self):
        return self.db.query(Ciudad).all()  # Método para listar ciudades
    
    def buscar_ciudad(self, id: UUID):
        return self.db.query(Ciudad).filter(Ciudad.id == id).first()  # Busca la ciudad por ID

    def actualizar_ciudad(self, id: UUID, ciudad: schemas.CiudadUpdate) -> models.Ciudad:
        db_ciudad = self.db.query(models.Ciudad).filter(models.Ciudad.id == id).first()
        if db_ciudad:
            if ciudad.nombre_ciudad is not None:
                db_ciudad.nombre_ciudad = ciudad.nombre_ciudad
            
            self.db.commit()
            self.db.refresh(db_ciudad)
            return db_ciudad
        return None  # Retorna None si no se encuentra la ciudad

    def eliminar_ciudad(self, id: UUID):
        ciudad = self.db.query(Ciudad).filter(Ciudad.id == id).first()  # Busca la ciudad
        if not ciudad:
            print(f"Ciudad con ID {id} no encontrada.")  # Log para depuración
            return False  # Retorna False si no se encuentra
        self.db.delete(ciudad)
        self.db.commit()
        return True


class SedeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, sede: SedeCreate):
        # Verificar que la empresa existe
        empresa = self.db.query(Empresa).filter(Empresa.id == sede.empresa_id).first()
        if not empresa:
            raise ValueError("La empresa con el ID proporcionado no existe.")

        db_sede = Sede(
            nombre_sede=sede.nombre_sede,
            email=sede.email,
            empresa_id=sede.empresa_id,  # Usar empresa_id en lugar de nit
            numero_contacto=sede.numero_contacto,
            departamento_id=sede.departamento_id,
            ciudad_id=sede.ciudad_id,
        )
        self.db.add(db_sede)
        self.db.commit()
        self.db.refresh(db_sede)
        return db_sede

    def create_bulk(self, sedes: list):
        for sede in sedes:
            self.create(sede)
    def list(self):
        return self.db.query(Sede).all()  # Método para listar todas las sedes
    
    def buscar_sede(self, id: UUID):
        return self.db.query(Sede).filter(Sede.id == id).first()  # Busca la sede por ID

    def actualizar_sede(self, id: UUID, sede: schemas.SedeUpdate) -> models.Sede:
        db_sede = self.db.query(models.Sede).filter(models.Sede.id == id).first()
        if db_sede:
            if sede.nombre_sede is not None:
                db_sede.nombre_sede = sede.nombre_sede
            if sede.email is not None:
                db_sede.email = sede.email
            if sede.numero_contacto is not None:
                db_sede.numero_contacto = sede.numero_contacto
            if sede.departamento_id is not None:
                db_sede.departamento_id = sede.departamento_id
            if sede.ciudad_id is not None:
                db_sede.ciudad_id = sede.ciudad_id
            
            self.db.commit()
            self.db.refresh(db_sede)
            return db_sede
        return None  # Retorna None si no se encuentra la sede

    def eliminar_sede(self, id: UUID):
        sede = self.db.query(Sede).filter(Sede.id == id).first()  # Busca la sede
        if not sede:
            print(f"Sede con ID {id} no encontrada.")  # Log para depuración
            return False  # Retorna False si no se encuentra
        self.db.delete(sede)
        self.db.commit()
        return True


class ImpresoraRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, impresora: ImpresoraCreate):
        db_impresora = Impresora(
            marca=impresora.marca,
            modelo=impresora.modelo,
            serial=impresora.serial,
            estado=impresora.estado,
            empresa_id=impresora.empresa_id,
            sede_id=impresora.sede_id,
           )
        self.db.add(db_impresora)
        self.db.commit()
        self.db.refresh(db_impresora)
        return db_impresora

    def create_bulk(self, impresoras: list):
        for impresora in impresoras:
            self.create(impresora)
    
    def list(self):
        return self.db.query(Impresora).all()  # Método para listar impresoras

    def buscar_impresora(self, id: UUID):
        return self.db.query(Impresora).filter(Impresora.id == id).first()  # Busca la impresora por ID

    def actualizar_impresora(self, id: UUID, impresora: schemas.ImpresoraUpdate) -> models.Impresora:
        db_impresora = self.db.query(models.Impresora).filter(models.Impresora.id == id).first()
        if db_impresora:
            if impresora.marca is not None:
                db_impresora.marca = impresora.marca
            if impresora.modelo is not None:
                db_impresora.modelo = impresora.modelo
            if impresora.serial is not None:
                db_impresora.serial = impresora.serial
            if impresora.estado is not None:
                db_impresora.estado = impresora.estado
            if impresora.empresa_id is not None:
                db_impresora.empresa_id = impresora.empresa_id
            if impresora.sede_id is not None:
                db_impresora.sede_id = impresora.sede_id
            
            self.db.commit()
            self.db.refresh(db_impresora)
            return db_impresora
        return None  # Retorna None si no se encuentra la impresora

    def eliminar_impresora(self, id: UUID):
        impresora = self.db.query(Impresora).filter(Impresora.id == id).first()  # Busca la impresora
        if not impresora:
            print(f"Impresora con ID {id} no encontrada.")  # Log para depuración
            return False  # Retorna False si no se encuentra
        self.db.delete(impresora)
        self.db.commit()
        return True


class TonerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, toner: TonerCreate):
        db_toner = Toner(
            referencia=toner.referencia,
           estado=toner.estado,
           empresa_id=toner.empresa_id,
           sede_id=toner.sede_id,
           )
        self.db.add(db_toner)
        self.db.commit()
        self.db.refresh(db_toner)
        return db_toner

    def create_bulk(self, toners: list):
        for toner in toners:
            self.create(toner)

    def list(self):
        return self.db.query(Toner).all()  # Método para listar toners
    
    def buscar_toner(self, id: UUID):
        return self.db.query(Toner).filter(Toner.id == id).first()  # Busca el toner por ID

    def actualizar_toner(self, id: UUID, toner: schemas.TonerUpdate) -> models.Toner:
        db_toner = self.db.query(models.Toner).filter(models.Toner.id == id).first()
        if db_toner:
            if toner.referencia is not None:
                db_toner.referencia = toner.referencia
            if toner.estado is not None:
                db_toner.estado = toner.estado
            if toner.empresa_id is not None:
                db_toner.empresa_id = toner.empresa_id
            if toner.sede_id is not None:
                db_toner.sede_id = toner.sede_id
            
            self.db.commit()
            self.db.refresh(db_toner)
            return db_toner
        return None  # Retorna None si no se encuentra el toner

    def eliminar_toner(self, id: UUID):
        toner = self.db.query(Toner).filter(Toner.id == id).first()  # Busca el toner
        if not toner:
            print(f"Toner con ID {id} no encontrado.")  # Log para depuración
            return False  # Retorna False si no se encuentra
        self.db.delete(toner)
        self.db.commit()
        return True