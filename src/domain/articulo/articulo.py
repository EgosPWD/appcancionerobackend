from datetime import datetime
from uuid import UUID
from typing import Optional

class Articulo:
    def __init__(self, id_articulo: int, titulo: str, contenido: str, 
                 fecha_creacion: datetime, creado_por: Optional[UUID] = None):
        self.id_articulo = id_articulo
        self.titulo = titulo
        self.contenido = contenido
        self.creado_por = creado_por
        self.fecha_creacion = fecha_creacion

    def get_id_articulo(self) -> int:
        return self.id_articulo

    def get_titulo(self) -> str:
        return self.titulo

    def get_contenido(self) -> str:
        return self.contenido

    def get_creado_por(self) -> Optional[UUID]:
        return self.creado_por

    def get_fecha_creacion(self) -> datetime:
        return self.fecha_creacion

    def set_titulo(self, titulo: str):
        self.titulo = titulo

    def set_contenido(self, contenido: str):
        self.contenido = contenido

    def set_creado_por(self, creado_por: UUID):
        self.creado_por = creado_por
