from typing import List, Optional
from uuid import UUID

from domain.repertorio.repertorio import Repertorio
from domain.repertorio.repertorio_port import RepertorioPort

class RepertorioService:
    def __init__(self, repertorio_port: RepertorioPort):
        self.repertorio_port = repertorio_port

    def get_repertorio(self, id_repertorio: int) -> Optional[Repertorio]:
        """Obtener un repertorio por su ID."""
        return self.repertorio_port.get_repertorio(id_repertorio)

    def get_all_repertorios(self) -> List[Repertorio]:
        """Obtener todos los repertorios."""
        return self.repertorio_port.get_all_repertorios()

    def get_repertorios_by_tiempo(self, id_tiempo: int) -> List[Repertorio]:
        """Obtener todos los repertorios por tiempo litúrgico."""
        return self.repertorio_port.get_repertorios_by_tiempo(id_tiempo)

    def get_repertorios_by_autor(self, creado_por: UUID) -> List[Repertorio]:
        """Obtener todos los repertorios de un autor específico."""
        return self.repertorio_port.get_repertorios_by_autor(creado_por)

    def save_repertorio(self, repertorio: Repertorio) -> None:
        """Guardar un repertorio."""
        self.repertorio_port.save_repertorio(repertorio)

    def delete_repertorio(self, id_repertorio: int) -> None:
        """Eliminar un repertorio por su ID."""
        self.repertorio_port.delete_repertorio(id_repertorio)
