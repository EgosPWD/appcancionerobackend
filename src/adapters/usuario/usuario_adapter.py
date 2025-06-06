from typing import List, Optional
from uuid import UUID
from datetime import datetime

from domain.usuario.usuario_port import UsuarioPort
from domain.usuario.usuario import Usuario
from connection.connection import get_connection
from supabase import Client

class UsuarioAdapter(UsuarioPort):
    def __init__(self):
        self.supabase: Client = get_connection()

    def get_usuario(self, id_usuario: UUID) -> Optional[Usuario]:
        response = self.supabase.table('usuario').select('*').eq('id_usuario', str(id_usuario)).execute()
        if response.data:
            data = response.data[0]
            return Usuario(
                id_usuario=UUID(data['id_usuario']),
                correo=data['correo'],
                hash_contraseña=data.get('hash_contraseña'),
                id_google=data.get('id_google'),
                nombre=data['nombre'],
                id_rol=data['id_rol'],
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00'))
            )
        return None

    def get_usuario_by_correo(self, correo: str) -> Optional[Usuario]:
        response = self.supabase.table('usuario').select('*').eq('correo', correo).execute()
        if response.data:
            data = response.data[0]
            return Usuario(
                id_usuario=UUID(data['id_usuario']),
                correo=data['correo'],
                hash_contraseña=data.get('hash_contraseña'),
                id_google=data.get('id_google'),
                nombre=data['nombre'],
                id_rol=data['id_rol'],
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00'))
            )
        return None

    def get_usuario_by_google_id(self, id_google: str) -> Optional[Usuario]:
        response = self.supabase.table('usuario').select('*').eq('id_google', id_google).execute()
        if response.data:
            data = response.data[0]
            return Usuario(
                id_usuario=UUID(data['id_usuario']),
                correo=data['correo'],
                hash_contraseña=data.get('hash_contraseña'),
                id_google=data.get('id_google'),
                nombre=data['nombre'],
                id_rol=data['id_rol'],
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00'))
            )
        return None

    def get_all_usuarios(self) -> List[Usuario]:
        response = self.supabase.table('usuario').select('*').execute()
        usuarios = []
        for data in response.data:
            usuarios.append(Usuario(
                id_usuario=UUID(data['id_usuario']),
                correo=data['correo'],
                hash_contraseña=data.get('hash_contraseña'),
                id_google=data.get('id_google'),
                nombre=data['nombre'],
                id_rol=data['id_rol'],
                fecha_creacion=datetime.fromisoformat(data['fecha_creacion'].replace('Z', '+00:00'))
            ))
        return usuarios

    def save_usuario(self, usuario: Usuario) -> None:
        usuario_data = {
            'id_usuario': str(usuario.get_id_usuario()),
            'correo': usuario.get_correo(),
            'nombre': usuario.get_nombre(),
            'id_rol': usuario.get_id_rol(),
            'fecha_creacion': usuario.get_fecha_creacion().isoformat()
        }
        
        if usuario.get_hash_contraseña():
            usuario_data['hash_contraseña'] = usuario.get_hash_contraseña()
        
        if usuario.get_id_google():
            usuario_data['id_google'] = usuario.get_id_google()
            
        self.supabase.table('usuario').upsert(usuario_data).execute()

    def delete_usuario(self, id_usuario: UUID) -> None:
        self.supabase.table('usuario').delete().eq('id_usuario', str(id_usuario)).execute()
