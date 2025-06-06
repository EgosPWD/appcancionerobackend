from datetime import datetime
from uuid import UUID
from typing import Optional

class Usuario:
    def __init__(self, id_usuario: UUID, correo: str, nombre: str, id_rol: int, 
                 fecha_creacion: datetime, hash_contraseña: Optional[str] = None, 
                 id_google: Optional[str] = None):
        self.id_usuario = id_usuario
        self.correo = correo
        self.hash_contraseña = hash_contraseña
        self.id_google = id_google
        self.nombre = nombre
        self.id_rol = id_rol
        self.fecha_creacion = fecha_creacion

    def get_id_usuario(self) -> UUID:
        return self.id_usuario

    def get_correo(self) -> str:
        return self.correo

    def get_nombre(self) -> str:
        return self.nombre

    def get_id_rol(self) -> int:
        return self.id_rol

    def get_fecha_creacion(self) -> datetime:
        return self.fecha_creacion

    def get_hash_contraseña(self) -> Optional[str]:
        return self.hash_contraseña

    def get_id_google(self) -> Optional[str]:
        return self.id_google

    def set_correo(self, correo: str):
        self.correo = correo

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_hash_contraseña(self, hash_contraseña: str):
        self.hash_contraseña = hash_contraseña

    def set_id_google(self, id_google: str):
        self.id_google = id_google

    def set_id_rol(self, id_rol: int):
        self.id_rol = id_rol
