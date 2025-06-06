from abc import ABC, abstractmethod
from typing import List, Optional

from domain.tipo_canto.tipo_canto import TipoCanto

class TipoCantoPort(ABC):
    @abstractmethod
    def get_tipo_canto(self, id_tipo: int) -> Optional[TipoCanto]:
        """Obtener un tipo de canto por su ID."""
        pass

    @abstractmethod
    def get_all_tipos_canto(self) -> List[TipoCanto]:
        """Obtener todos los tipos de canto."""
        pass

    @abstractmethod
    def save_tipo_canto(self, tipo_canto: TipoCanto) -> None:
        """Guardar un tipo de canto."""
        pass

    @abstractmethod
    def delete_tipo_canto(self, id_tipo: int) -> None:
        """Eliminar un tipo de canto por su ID."""
        pass
