from typing import List, Optional

from domain.tipo_canto.tipo_canto_port import TipoCantoPort
from domain.tipo_canto.tipo_canto import TipoCanto
from connection.connection import get_connection
from supabase import Client

class TipoCantoAdapter(TipoCantoPort):
    def __init__(self):
        self.supabase: Client = get_connection()

    def get_tipo_canto(self, id_tipo: int) -> Optional[TipoCanto]:
        response = self.supabase.table('tipo_canto').select('*').eq('id_tipo', id_tipo).execute()
        if response.data:
            data = response.data[0]
            return TipoCanto(
                id_tipo=data['id_tipo'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                orden=data.get('orden')
            )
        return None

    def get_all_tipos_canto(self) -> List[TipoCanto]:
        response = self.supabase.table('tipo_canto').select('*').order('orden').execute()
        tipos = []
        for data in response.data:
            tipos.append(TipoCanto(
                id_tipo=data['id_tipo'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                orden=data.get('orden')
            ))
        return tipos

    def save_tipo_canto(self, tipo_canto: TipoCanto) -> None:
        tipo_data = {
            'id_tipo': tipo_canto.get_id_tipo(),
            'nombre': tipo_canto.get_nombre()
        }
        
        if tipo_canto.get_descripcion():
            tipo_data['descripcion'] = tipo_canto.get_descripcion()
            
        if tipo_canto.get_orden():
            tipo_data['orden'] = tipo_canto.get_orden()
            
        self.supabase.table('tipo_canto').upsert(tipo_data).execute()

    def delete_tipo_canto(self, id_tipo: int) -> None:
        self.supabase.table('tipo_canto').delete().eq('id_tipo', id_tipo).execute()
