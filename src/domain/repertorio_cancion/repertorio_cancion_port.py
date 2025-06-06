from abc import ABC, abstractmethod
from typing import List

from domain.repertorio_cancion.repertorio_cancion import RepertorioCancion

class RepertorioCancionPort(ABC):
    @abstractmethod
    def get_canciones_by_repertorio(self, id_repertorio: int) -> List[RepertorioCancion]:
        """Obtener todas las canciones de un repertorio."""
        pass

    @abstractmethod
    def get_canciones_by_repertorio_and_tipo(self, id_repertorio: int, id_tipo: int) -> List[RepertorioCancion]:
        """Obtener canciones de un repertorio por tipo."""
        pass

    @abstractmethod
    def add_cancion_to_repertorio(self, repertorio_cancion: RepertorioCancion) -> None:
        """Agregar una canción a un repertorio."""
        pass

    @abstractmethod
    def remove_cancion_from_repertorio(self, id_repertorio: int, id_tipo: int, id_cancion: int) -> None:
        """Eliminar una canción de un repertorio."""
        pass

    @abstractmethod
    def update_posicion_cancion(self, id_repertorio: int, id_tipo: int, id_cancion: int, posicion: int) -> None:
        """Actualizar la posición de una canción en un repertorio."""
        pass
