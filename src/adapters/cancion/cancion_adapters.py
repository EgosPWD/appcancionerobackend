from domain.cancion.cancion_port import CancionPort
from domain.cancion.cancion import Cancion

from connection.connection import get_connection

from supabase import Client

class CancionAdapter(CancionPort):
    def __init__(self):
        self.supabase: Client = get_connection()

    def get_cancion(self, id_cancion: int) -> Cancion:
        response = self.supabase.table('cancion').select('*').eq('id_cancion', id_cancion).execute()
        if response.data:
            data = response.data[0]
            return Cancion(
                id_cancion=data['id_cancion'],
                titulo=data['titulo'],
                autor=data['autor'],
                letra=data['letra'],
                id_tipo=data['id_tipo'],
                estado=data['estado'],
                enviado_por=data['enviado_por'],
                fecha_envio=data['fecha_envio']
            )
        return None

    def get_all_canciones(self) -> list[Cancion]:
        response = self.supabase.table('cancion').select('*').execute()
        canciones = []
        for data in response.data:
            canciones.append(Cancion(
                id_cancion=data['id_cancion'],
                titulo=data['titulo'],
                autor=data['autor'],
                letra=data['letra'],
                id_tipo=data['id_tipo'],
                estado=data['estado'],
                enviado_por=data['enviado_por'],
                fecha_envio=data['fecha_envio']
            ))
        return canciones

    def save_cancion(self, cancion: Cancion) -> None:
        self.supabase.table('cancion').upsert({
            'id_cancion': cancion.id(),
            'titulo': cancion.titulo(),
            'autor': cancion.autor(),
            'letra': cancion.letra(),
            'id_tipo': cancion.id_tipo(),
            'estado': cancion.estado(),
            'enviado_por': cancion.enviado_por(),
            'fecha_envio': cancion.fecha_envio()
        }).execute()

    def delete_cancion(self, id_cancion: int) -> None:
        self.supabase.table('cancion').delete().eq('id_cancion', id_cancion).execute()