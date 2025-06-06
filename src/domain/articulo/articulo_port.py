from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from domain.articulo.articulo import Articulo

class ArticuloPort(ABC):
    @abstractmethod
    def get_articulo(self, id_articulo: int) -> Optional[Articulo]:
        """Obtener un artículo por su ID."""
        pass

    @abstractmethod
    def get_all_articulos(self) -> List[Articulo]:
        """Obtener todos los artículos."""
        pass

    @abstractmethod
    def get_articulos_by_autor(self, creado_por: UUID) -> List[Articulo]:
        """Obtener todos los artículos de un autor específico."""
        pass

    @abstractmethod
    def save_articulo(self, articulo: Articulo) -> None:
        """Guardar un artículo."""
        pass

    @abstractmethod
    def delete_articulo(self, id_articulo: int) -> None:
        """Eliminar un artículo por su ID."""
        pass
