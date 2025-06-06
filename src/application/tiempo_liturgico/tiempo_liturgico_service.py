from typing import List, Optional

from domain.tiempo_liturgico.tiempo_liturgico import TiempoLiturgico
from domain.tiempo_liturgico.tiempo_liturgico_port import TiempoLiturgicoPort

class TiempoLiturgicoService:
    def __init__(self, tiempo_liturgico_port: TiempoLiturgicoPort):
        self.tiempo_liturgico_port = tiempo_liturgico_port

    def get_tiempo_liturgico(self, id_tiempo: int) -> Optional[TiempoLiturgico]:
        """Obtener un tiempo litúrgico por su ID."""
        return self.tiempo_liturgico_port.get_tiempo_liturgico(id_tiempo)

    def get_all_tiempos_liturgicos(self) -> List[TiempoLiturgico]:
        """Obtener todos los tiempos litúrgicos."""
        return self.tiempo_liturgico_port.get_all_tiempos_liturgicos()

    def save_tiempo_liturgico(self, tiempo_liturgico: TiempoLiturgico) -> None:
        """Guardar un tiempo litúrgico."""
        self.tiempo_liturgico_port.save_tiempo_liturgico(tiempo_liturgico)

    def delete_tiempo_liturgico(self, id_tiempo: int) -> None:
        """Eliminar un tiempo litúrgico por su ID."""
        self.tiempo_liturgico_port.delete_tiempo_liturgico(id_tiempo)
