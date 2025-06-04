class Cancion:
    def __init__(self, id_cancion, titulo, autor, letra, id_tipo, estado, enviado_por, fecha_envio):
        self.id_cancion = id_cancion
        self.titulo = titulo
        self.autor = autor
        self.letra = letra
        self.id_tipo = id_tipo
        self.estado = estado
        self.enviado_por = enviado_por
        self.fecha_envio = fecha_envio
        pass

    def id(self):
        return self.id_cancion

    def titulo(self):
        return self.titulo

    def autor(self):
        return self.autor

    def letra(self):
        return self.letra

    def id_tipo(self):
        return self.id_tipo

    def estado(self):
        return self.estado

    def enviado_por(self):
        return self.enviado_por

    def fecha_envio(self):
        return self.fecha_envio

    def setId(self, id_cancion):
        self.id_cancion = id_cancion

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setAutor(self, autor):
        self.autor = autor

    def setLetra(self, letra):
        self.letra = letra

    def setIdTipo(self, id_tipo):
        self.id_tipo = id_tipo

    def setEstado(self, estado):
        self.estado = estado

    def setEnviadorPor(self, enviado_por):
        self.enviador_por = enviado_por

    def setFechaEnvio(self, fecha_envio):
        self.fecha_envio = fecha_envio
