from datetime import datetime
from uuid import UUID

class Sugerencia:
    def __init__(self, id_sugerencia: int, fecha_sugerencia: datetime,
                 id_usuario: UUID = None, id_cancion: int = None):
        self.id_sugerencia = id_sugerencia
        self.id_usuario = id_usuario
        self.id_cancion = id_cancion
        self.fecha_sugerencia = fecha_sugerencia

    def get_id_sugerencia(self) -> int:
        return self.id_sugerencia

    def get_id_usuario(self) -> UUID:
        return self.id_usuario

    def get_id_cancion(self) -> int:
        return self.id_cancion

    def get_fecha_sugerencia(self) -> datetime:
        return self.fecha_sugerencia

    def set_id_usuario(self, id_usuario: UUID):
        self.id_usuario = id_usuario

    def set_id_cancion(self, id_cancion: int):
        self.id_cancion = id_cancion
