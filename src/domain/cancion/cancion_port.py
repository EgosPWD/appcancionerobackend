from abc import ABC, abstractmethod

from domain.cancion.cancion import Cancion

class CancionPort(ABC):
    @abstractmethod
    def get_cancion(self, id_cancion: int) -> Cancion:
        """Retrieve a song by its ID."""
        pass

    @abstractmethod
    def get_all_canciones(self) -> list[Cancion]:
        """Retrieve all songs."""
        pass

    @abstractmethod
    def save_cancion(self, cancion: Cancion) -> None:
        """Save a song."""
        pass

    @abstractmethod
    def delete_cancion(self, id_cancion: int) -> None:
        """Delete a song by its ID."""
        pass