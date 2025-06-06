from typing import List, Optional
from uuid import UUID
from datetime import datetime, date

from domain.repertorio.repertorio_port import RepertorioPort
from domain.repertorio.repertorio import Repertorio
from connection.connection import get_connection
from supabase import Client

class RepertorioAdapter(RepertorioPort):
    def __init__(self):
        self.supabase: Client = get_connection()

    def get_repertorio(self, id_repertorio: int) -> Optional[Repertorio]:
        response = self.supabase.table('repertorio').select('*').eq('id_repertorio', id_repertorio).execute()
        if response.data:
            data = response.data[0]
            return Repertorio(
                id_repertorio=data['id_repertorio'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                id_tiempo=data['id_tiempo'],
                creado_por=UUID(data['creado_por']) if data.get('creado_por') else None,
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00')),
                fecha=date.fromisoformat(data['fecha']) if data.get('fecha') else None,
                tipo_misa=data.get('tipo_misa')
            )
        return None

    def get_all_repertorios(self) -> List[Repertorio]:
        response = self.supabase.table('repertorio').select('*').execute()
        repertorios = []
        for data in response.data:
            repertorios.append(Repertorio(
                id_repertorio=data['id_repertorio'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                id_tiempo=data['id_tiempo'],
                creado_por=UUID(data['creado_por']) if data.get('creado_por') else None,
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00')),
                fecha=date.fromisoformat(data['fecha']) if data.get('fecha') else None,
                tipo_misa=data.get('tipo_misa')
            ))
        return repertorios

    def get_repertorios_by_tiempo(self, id_tiempo: int) -> List[Repertorio]:
        response = self.supabase.table('repertorio').select('*').eq('id_tiempo', id_tiempo).execute()
        repertorios = []
        for data in response.data:
            repertorios.append(Repertorio(
                id_repertorio=data['id_repertorio'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                id_tiempo=data['id_tiempo'],
                creado_por=UUID(data['creado_por']) if data.get('creado_por') else None,
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00')),
                fecha=date.fromisoformat(data['fecha']) if data.get('fecha') else None,
                tipo_misa=data.get('tipo_misa')
            ))
        return repertorios

    def get_repertorios_by_autor(self, creado_por: UUID) -> List[Repertorio]:
        response = self.supabase.table('repertorio').select('*').eq('creado_por', str(creado_por)).execute()
        repertorios = []
        for data in response.data:
            repertorios.append(Repertorio(
                id_repertorio=data['id_repertorio'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                id_tiempo=data['id_tiempo'],
                creado_por=UUID(data['creado_por']) if data.get('creado_por') else None,
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00')),
                fecha=date.fromisoformat(data['fecha']) if data.get('fecha') else None,
                tipo_misa=data.get('tipo_misa')
            ))
        return repertorios

    def save_repertorio(self, repertorio: Repertorio) -> None:
        repertorio_data = {
            'id_repertorio': repertorio.get_id_repertorio(),
            'nombre': repertorio.get_nombre(),
            'id_tiempo': repertorio.get_id_tiempo(),
            'fecha_creacion': repertorio.get_fecha_creacion().isoformat()
        }
        
        if repertorio.get_descripcion():
            repertorio_data['descripcion'] = repertorio.get_descripcion()
            
        if repertorio.get_creado_por():
            repertorio_data['creado_por'] = str(repertorio.get_creado_por())
            
        if repertorio.get_fecha():
            repertorio_data['fecha'] = repertorio.get_fecha().isoformat()
            
        if repertorio.get_tipo_misa():
            repertorio_data['tipo_misa'] = repertorio.get_tipo_misa()
            
        self.supabase.table('repertorio').upsert(repertorio_data).execute()

    def delete_repertorio(self, id_repertorio: int) -> None:
        self.supabase.table('repertorio').delete().eq('id_repertorio', id_repertorio).execute()
