from typing import List, Optional

from domain.tiempo_liturgico.tiempo_liturgico_port import TiempoLiturgicoPort
from domain.tiempo_liturgico.tiempo_liturgico import TiempoLiturgico
from connection.connection import get_connection
from supabase import Client

class TiempoLiturgicoAdapter(TiempoLiturgicoPort):
    def __init__(self):
        self.supabase: Client = get_connection()

    def get_tiempo_liturgico(self, id_tiempo: int) -> Optional[TiempoLiturgico]:
        response = self.supabase.table('tiempo_liturgico').select('*').eq('id_tiempo', id_tiempo).execute()
        if response.data:
            data = response.data[0]
            return TiempoLiturgico(
                id_tiempo=data['id_tiempo'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                color=data.get('color')
            )
        return None

    def get_all_tiempos_liturgicos(self) -> List[TiempoLiturgico]:
        response = self.supabase.table('tiempo_liturgico').select('*').execute()
        tiempos = []
        for data in response.data:
            tiempos.append(TiempoLiturgico(
                id_tiempo=data['id_tiempo'],
                nombre=data['nombre'],
                descripcion=data.get('descripcion'),
                color=data.get('color')
            ))
        return tiempos

    def save_tiempo_liturgico(self, tiempo_liturgico: TiempoLiturgico) -> None:
        tiempo_data = {
            'id_tiempo': tiempo_liturgico.get_id_tiempo(),
            'nombre': tiempo_liturgico.get_nombre()
        }
        
        if tiempo_liturgico.get_descripcion():
            tiempo_data['descripcion'] = tiempo_liturgico.get_descripcion()
            
        if tiempo_liturgico.get_color():
            tiempo_data['color'] = tiempo_liturgico.get_color()
            
        self.supabase.table('tiempo_liturgico').upsert(tiempo_data).execute()

    def delete_tiempo_liturgico(self, id_tiempo: int) -> None:
        self.supabase.table('tiempo_liturgico').delete().eq('id_tiempo', id_tiempo).execute()
