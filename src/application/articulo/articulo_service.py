from typing import List, Optional
from uuid import UUID

from domain.articulo.articulo import Articulo
from domain.articulo.articulo_port import ArticuloPort

class ArticuloService:
    def __init__(self, articulo_port: ArticuloPort):
        self.articulo_port = articulo_port

    def get_articulo(self, id_articulo: int) -> Optional[Articulo]:
        """Obtener un artículo por su ID."""
        return self.articulo_port.get_articulo(id_articulo)

    def get_all_articulos(self) -> List[Articulo]:
        """Obtener todos los artículos."""
        return self.articulo_port.get_all_articulos()

    def get_articulos_by_autor(self, creado_por: UUID) -> List[Articulo]:
        """Obtener todos los artículos de un autor específico."""
        return self.articulo_port.get_articulos_by_autor(creado_por)

    def save_articulo(self, articulo: Articulo) -> None:
        """Guardar un artículo."""
        self.articulo_port.save_articulo(articulo)

    def delete_articulo(self, id_articulo: int) -> None:
        """Eliminar un artículo por su ID."""
        self.articulo_port.delete_articulo(id_articulo)
