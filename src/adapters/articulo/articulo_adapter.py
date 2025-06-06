from typing import List, Optional
from uuid import UUID
from datetime import datetime

from domain.articulo.articulo_port import ArticuloPort
from domain.articulo.articulo import Articulo
from connection.connection import get_connection
from supabase import Client

class ArticuloAdapter(ArticuloPort):
    def __init__(self):
        self.supabase: Client = get_connection()

    def get_articulo(self, id_articulo: int) -> Optional[Articulo]:
        response = self.supabase.table('articulo').select('*').eq('id_articulo', id_articulo).execute()
        if response.data:
            data = response.data[0]
            return Articulo(
                id_articulo=data['id_articulo'],
                titulo=data['titulo'],
                contenido=data['contenido'],
                creado_por=UUID(data['creado_por']) if data.get('creado_por') else None,
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00'))
            )
        return None

    def get_all_articulos(self) -> List[Articulo]:
        response = self.supabase.table('articulo').select('*').execute()
        articulos = []
        for data in response.data:
            articulos.append(Articulo(
                id_articulo=data['id_articulo'],
                titulo=data['titulo'],
                contenido=data['contenido'],
                creado_por=UUID(data['creado_por']) if data.get('creado_por') else None,
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00'))
            ))
        return articulos

    def get_articulos_by_autor(self, creado_por: UUID) -> List[Articulo]:
        response = self.supabase.table('articulo').select('*').eq('creado_por', str(creado_por)).execute()
        articulos = []
        for data in response.data:
            articulos.append(Articulo(
                id_articulo=data['id_articulo'],
                titulo=data['titulo'],
                contenido=data['contenido'],
                creado_por=UUID(data['creado_por']) if data.get('creado_por') else None,
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00'))
            ))
        return articulos

    def save_articulo(self, articulo: Articulo) -> None:
        articulo_data = {
            'id_articulo': articulo.get_id_articulo(),
            'titulo': articulo.get_titulo(),
            'contenido': articulo.get_contenido(),
            'fecha_creacion': articulo.get_fecha_creacion().isoformat()
        }
        
        if articulo.get_creado_por():
            articulo_data['creado_por'] = str(articulo.get_creado_por())
            
        self.supabase.table('articulo').upsert(articulo_data).execute()

    def delete_articulo(self, id_articulo: int) -> None:
        self.supabase.table('articulo').delete().eq('id_articulo', id_articulo).execute()
