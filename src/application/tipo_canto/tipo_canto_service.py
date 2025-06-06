from typing import List, Optional

from domain.tipo_canto.tipo_canto import TipoCanto
from domain.tipo_canto.tipo_canto_port import TipoCantoPort

class TipoCantoService:
    def __init__(self, tipo_canto_port: TipoCantoPort):
        self.tipo_canto_port = tipo_canto_port

    def get_tipo_canto(self, id_tipo: int) -> Optional[TipoCanto]:
        """Obtener un tipo de canto por su ID."""
        return self.tipo_canto_port.get_tipo_canto(id_tipo)

    def get_all_tipos_canto(self) -> List[TipoCanto]:
        """Obtener todos los tipos de canto."""
        return self.tipo_canto_port.get_all_tipos_canto()

    def save_tipo_canto(self, tipo_canto: TipoCanto) -> None:
        """Guardar un tipo de canto."""
        self.tipo_canto_port.save_tipo_canto(tipo_canto)

    def delete_tipo_canto(self, id_tipo: int) -> None:
        """Eliminar un tipo de canto por su ID."""
        self.tipo_canto_port.delete_tipo_canto(id_tipo)
