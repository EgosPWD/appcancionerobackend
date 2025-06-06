from typing import Optional

class TiempoLiturgico:
    def __init__(self, id_tiempo: int, nombre: str, descripcion: Optional[str] = None,
                 color: Optional[str] = None):
        self.id_tiempo = id_tiempo
        self.nombre = nombre
        self.descripcion = descripcion
        self.color = color

    def get_id_tiempo(self) -> int:
        return self.id_tiempo

    def get_nombre(self) -> str:
        return self.nombre

    def get_descripcion(self) -> Optional[str]:
        return self.descripcion

    def get_color(self) -> Optional[str]:
        return self.color

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_descripcion(self, descripcion: str):
        self.descripcion = descripcion

    def set_color(self, color: str):
        self.color = color
