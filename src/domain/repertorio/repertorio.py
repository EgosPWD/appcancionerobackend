from datetime import date, datetime
from uuid import UUID
from typing import Optional

class Repertorio:
    def __init__(self, id_repertorio: int, nombre: str, id_tiempo: int, 
                 fecha_creacion: datetime, descripcion: Optional[str] = None,
                 creado_por: Optional[UUID] = None, fecha: Optional[date] = None,
                 tipo_misa: Optional[str] = None):
        self.id_repertorio = id_repertorio
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_tiempo = id_tiempo
        self.creado_por = creado_por
        self.fecha_creacion = fecha_creacion
        self.fecha = fecha
        self.tipo_misa = tipo_misa

    def get_id_repertorio(self) -> int:
        return self.id_repertorio

    def get_nombre(self) -> str:
        return self.nombre

    def get_descripcion(self) -> Optional[str]:
        return self.descripcion

    def get_id_tiempo(self) -> int:
        return self.id_tiempo

    def get_creado_por(self) -> Optional[UUID]:
        return self.creado_por

    def get_fecha_creacion(self) -> datetime:
        return self.fecha_creacion

    def get_fecha(self) -> Optional[date]:
        return self.fecha

    def get_tipo_misa(self) -> Optional[str]:
        return self.tipo_misa

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_descripcion(self, descripcion: str):
        self.descripcion = descripcion

    def set_id_tiempo(self, id_tiempo: int):
        self.id_tiempo = id_tiempo

    def set_creado_por(self, creado_por: UUID):
        self.creado_por = creado_por

    def set_fecha(self, fecha: date):
        self.fecha = fecha

    def set_tipo_misa(self, tipo_misa: str):
        self.tipo_misa = tipo_misa
