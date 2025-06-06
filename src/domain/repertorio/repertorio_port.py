from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from domain.repertorio.repertorio import Repertorio

class RepertorioPort(ABC):
    @abstractmethod
    def get_repertorio(self, id_repertorio: int) -> Optional[Repertorio]:
        """Obtener un repertorio por su ID."""
        pass

    @abstractmethod
    def get_all_repertorios(self) -> List[Repertorio]:
        """Obtener todos los repertorios."""
        pass

    @abstractmethod
    def get_repertorios_by_tiempo(self, id_tiempo: int) -> List[Repertorio]:
        """Obtener todos los repertorios por tiempo litúrgico."""
        pass

    @abstractmethod
    def get_repertorios_by_autor(self, creado_por: UUID) -> List[Repertorio]:
        """Obtener todos los repertorios de un autor específico."""
        pass

    @abstractmethod
    def save_repertorio(self, repertorio: Repertorio) -> None:
        """Guardar un repertorio."""
        pass

    @abstractmethod
    def delete_repertorio(self, id_repertorio: int) -> None:
        """Eliminar un repertorio por su ID."""
        pass
