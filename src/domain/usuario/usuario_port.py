from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from domain.usuario.usuario import Usuario

class UsuarioPort(ABC):
    @abstractmethod
    def get_usuario(self, id_usuario: UUID) -> Optional[Usuario]:
        """Obtener un usuario por su ID."""
        pass

    @abstractmethod
    def get_usuario_by_correo(self, correo: str) -> Optional[Usuario]:
        """Obtener un usuario por su correo electrónico."""
        pass

    @abstractmethod
    def get_usuario_by_google_id(self, id_google: str) -> Optional[Usuario]:
        """Obtener un usuario por su ID de Google."""
        pass

    @abstractmethod
    def get_all_usuarios(self) -> List[Usuario]:
        """Obtener todos los usuarios."""
        pass

    @abstractmethod
    def save_usuario(self, usuario: Usuario) -> None:
        """Guardar un usuario."""
        pass

    @abstractmethod
    def delete_usuario(self, id_usuario: UUID) -> None:
        """Eliminar un usuario por su ID."""
        pass
