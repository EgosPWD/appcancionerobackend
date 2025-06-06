from typing import List, Optional
from uuid import UUID

from domain.usuario.usuario import Usuario
from domain.usuario.usuario_port import UsuarioPort

class UsuarioService:
    def __init__(self, usuario_port: UsuarioPort):
        self.usuario_port = usuario_port

    def get_usuario(self, id_usuario: UUID) -> Optional[Usuario]:
        """Obtener un usuario por su ID."""
        return self.usuario_port.get_usuario(id_usuario)

    def get_usuario_by_correo(self, correo: str) -> Optional[Usuario]:
        """Obtener un usuario por su correo electrónico."""
        return self.usuario_port.get_usuario_by_correo(correo)

    def get_usuario_by_google_id(self, id_google: str) -> Optional[Usuario]:
        """Obtener un usuario por su ID de Google."""
        return self.usuario_port.get_usuario_by_google_id(id_google)

    def get_all_usuarios(self) -> List[Usuario]:
        """Obtener todos los usuarios."""
        return self.usuario_port.get_all_usuarios()

    def save_usuario(self, usuario: Usuario) -> None:
        """Guardar un usuario."""
        self.usuario_port.save_usuario(usuario)

    def delete_usuario(self, id_usuario: UUID) -> None:
        """Eliminar un usuario por su ID."""
        self.usuario_port.delete_usuario(id_usuario)
