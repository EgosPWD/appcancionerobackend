from domain.cancion.cancion import Cancion
from domain.cancion.cancion_port import CancionPort

class CancionService:
    def __init__(self, cancion_port: CancionPort):
        self.cancion_port = cancion_port

    def get_cancion(self, id_cancion: int) -> Cancion:
        """Obtener una canción por su ID."""
        return self.cancion_port.get_cancion(id_cancion)

    def get_all_canciones(self) -> list[Cancion]:
        """Obtener todas las canciones."""
        return self.cancion_port.get_all_canciones()

    def save_cancion(self, cancion: Cancion) -> Cancion:
        """Guardar una canción."""
        return self.cancion_port.save_cancion(cancion)

    def delete_cancion(self, id_cancion: int) -> None:
        """Eliminar una canción por su ID."""
        self.cancion_port.delete_cancion(id_cancion)
