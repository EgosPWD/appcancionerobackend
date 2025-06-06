class Rol:
    def __init__(self, id_rol: int, nombre: str):
        self.id_rol = id_rol
        self.nombre = nombre

    def get_id_rol(self) -> int:
        return self.id_rol

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre
