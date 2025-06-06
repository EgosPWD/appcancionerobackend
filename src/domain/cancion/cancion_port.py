from abc import ABC, abstractmethod

from domain.cancion.cancion import Cancion

class CancionPort(ABC):
    @abstractmethod
    def get_cancion(self, id_cancion: int) -> Cancion:
        """Obtener una canción por su ID."""
        pass

    @abstractmethod
    def get_all_canciones(self) -> list[Cancion]:
        """Obtener todas las canciones."""
        pass

    @abstractmethod
    def save_cancion(self, cancion: Cancion) -> Cancion:
        """Guardar una canción."""
        pass

    @abstractmethod
    def delete_cancion(self, id_cancion: int) -> None:
        """Eliminar una canción por su ID."""
        pass
