from typing import Optional

class TipoCanto:
    def __init__(self, id_tipo: int, nombre: str, descripcion: Optional[str] = None, 
                 orden: Optional[int] = None):
        self.id_tipo = id_tipo
        self.nombre = nombre
        self.descripcion = descripcion
        self.orden = orden

    def get_id_tipo(self) -> int:
        return self.id_tipo

    def get_nombre(self) -> str:
        return self.nombre

    def get_descripcion(self) -> Optional[str]:
        return self.descripcion

    def get_orden(self) -> Optional[int]:
        return self.orden

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_descripcion(self, descripcion: str):
        self.descripcion = descripcion

    def set_orden(self, orden: int):
        self.orden = orden
