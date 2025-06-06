from abc import ABC, abstractmethod
from typing import List, Optional

from domain.tiempo_liturgico.tiempo_liturgico import TiempoLiturgico

class TiempoLiturgicoPort(ABC):
    @abstractmethod
    def get_tiempo_liturgico(self, id_tiempo: int) -> Optional[TiempoLiturgico]:
        """Obtener un tiempo litúrgico por su ID."""
        pass

    @abstractmethod
    def get_all_tiempos_liturgicos(self) -> List[TiempoLiturgico]:
        """Obtener todos los tiempos litúrgicos."""
        pass

    @abstractmethod
    def save_tiempo_liturgico(self, tiempo_liturgico: TiempoLiturgico) -> None:
        """Guardar un tiempo litúrgico."""
        pass

    @abstractmethod
    def delete_tiempo_liturgico(self, id_tiempo: int) -> None:
        """Eliminar un tiempo litúrgico por su ID."""
        pass
