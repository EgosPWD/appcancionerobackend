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

    def save_cancion(self, cancion: Cancion) -> Cancion:
        # Convert datetime to string if needed
        fecha_envio = cancion.fecha_envio
        if hasattr(fecha_envio, 'isoformat'):
            fecha_envio = fecha_envio.isoformat()
        elif fecha_envio is not None and not isinstance(fecha_envio, str):
            fecha_envio = str(fecha_envio)
        
        # Prepare data for database
        data = {
            'titulo': cancion.titulo,
            'autor': cancion.autor,
            'letra': cancion.letra,
            'id_tipo': cancion.id_tipo,
            'estado': cancion.estado,
            'enviado_por': str(cancion.enviado_por) if cancion.enviado_por else None,
            'fecha_envio': fecha_envio
        }
        
        # Only include id_cancion if it's not 0 (for updates)
        if cancion.id_cancion and cancion.id_cancion != 0:
            data['id_cancion'] = cancion.id_cancion
        
        response = self.supabase.table('cancion').upsert(data).execute()
        
        # Return the saved cancion with updated data
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
        return cancion

    def delete_cancion(self, id_cancion: int) -> None:
        self.supabase.table('cancion').delete().eq('id_cancion', id_cancion).execute()