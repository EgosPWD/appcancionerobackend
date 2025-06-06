class Cancion:
    def __init__(self, id_cancion, titulo, autor, letra, id_tipo, estado, enviado_por, fecha_envio):
        self._id_cancion = id_cancion
        self._titulo = titulo
        self._autor = autor
        self._letra = letra
        self._id_tipo = id_tipo
        self._estado = estado
        self._enviado_por = enviado_por
        self._fecha_envio = fecha_envio

    @property
    def id_cancion(self):
        return self._id_cancion

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def letra(self):
        return self._letra

    @property
    def id_tipo(self):
        return self._id_tipo

    @property
    def estado(self):
        return self._estado

    @property
    def enviado_por(self):
        return self._enviado_por

    @property
    def fecha_envio(self):
        return self._fecha_envio

    def id(self):
        return self._id_cancion

    def titulo_method(self):
        return self._titulo

    def autor_method(self):
        return self._autor

    def letra_method(self):
        return self._letra

    def id_tipo_method(self):
        return self._id_tipo

    def estado_method(self):
        return self._estado

    def enviado_por_method(self):
        return self._enviado_por

    def fecha_envio_method(self):
        return self._fecha_envio

    def setId(self, id_cancion):
        self._id_cancion = id_cancion

    def setTitulo(self, titulo):
        self._titulo = titulo

    def setAutor(self, autor):
        self._autor = autor

    def setLetra(self, letra):
        self._letra = letra

    def setIdTipo(self, id_tipo):
        self._id_tipo = id_tipo

    def setEstado(self, estado):
        self._estado = estado

    def setEnviadoPor(self, enviado_por):
        self._enviado_por = enviado_por

    def setFechaEnvio(self, fecha_envio):
        self._fecha_envio = fecha_envio
