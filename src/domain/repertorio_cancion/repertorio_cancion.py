from typing import Optional

class RepertorioCancion:
    def __init__(self, id_repertorio: int, id_tipo: int, id_cancion: int, 
                 posicion: Optional[int] = 1):
        self.id_repertorio = id_repertorio
        self.id_tipo = id_tipo
        self.id_cancion = id_cancion
        self.posicion = posicion

    def get_id_repertorio(self) -> int:
        return self.id_repertorio

    def get_id_tipo(self) -> int:
        return self.id_tipo

    def get_id_cancion(self) -> int:
        return self.id_cancion

    def get_posicion(self) -> Optional[int]:
        return self.posicion

    def set_posicion(self, posicion: int):
        self.posicion = posicion
