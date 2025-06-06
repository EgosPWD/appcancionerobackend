from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
from datetime import datetime
from uuid import UUID, uuid4

def format_datetime(dt):
    """Función auxiliar para formatear objetos datetime de forma segura"""
    if dt is None:
        return None
    if isinstance(dt, str):
        return dt
    if hasattr(dt, 'isoformat'):
        return dt.isoformat()
    return str(dt)

from api.models import (
    CancionCreate, CancionUpdate, CancionResponse,
    UsuarioCreate, UsuarioUpdate, UsuarioResponse,
    ArticuloCreate, ArticuloUpdate, ArticuloResponse,
    RepertorioCreate, RepertorioUpdate, RepertorioResponse,
    TipoCantoCreate, TipoCantoUpdate, TipoCantoResponse,
    TiempoLiturgicoCreate, TiempoLiturgicoUpdate, TiempoLiturgicoResponse,
    MessageResponse, ErrorResponse
)

# Importar modelos de dominio
from domain.cancion.cancion import Cancion
from domain.usuario.usuario import Usuario
from domain.articulo.articulo import Articulo
from domain.repertorio.repertorio import Repertorio
from domain.tipo_canto.tipo_canto import TipoCanto
from domain.tiempo_liturgico.tiempo_liturgico import TiempoLiturgico

# Importar servicios
from application.cancion.cancion_service import CancionService
from application.usuario.usuario_service import UsuarioService
from application.articulo.articulo_service import ArticuloService
from application.repertorio.repertorio_service import RepertorioService
from application.tipo_canto.tipo_canto_service import TipoCantoService
from application.tiempo_liturgico.tiempo_liturgico_service import TiempoLiturgicoService

# Importar adaptadores
from adapters.cancion.cancion_adapters import CancionAdapter
from adapters.usuario.usuario_adapter import UsuarioAdapter
from adapters.articulo.articulo_adapter import ArticuloAdapter
from adapters.repertorio.repertorio_adapter import RepertorioAdapter
from adapters.tipo_canto.tipo_canto_adapter import TipoCantoAdapter
from adapters.tiempo_liturgico.tiempo_liturgico_adapter import TiempoLiturgicoAdapter

app = FastAPI(
    title="Cancionero API",
    version="2.0.0",
    description="API REST completa para administrar repertorios de canciones de iglesia, incluyendo todas las operaciones CRUD (crear, leer, actualizar y eliminar)",
    contact={
        "name": "Quods",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cancion_service = CancionService(CancionAdapter())
usuario_service = UsuarioService(UsuarioAdapter())
articulo_service = ArticuloService(ArticuloAdapter())
repertorio_service = RepertorioService(RepertorioAdapter())
tipo_canto_service = TipoCantoService(TipoCantoAdapter())
tiempo_liturgico_service = TiempoLiturgicoService(TiempoLiturgicoAdapter())


@app.get("/", tags=["System"])
async def root():
    return {
        "message": "Cancionero API - Church Song Management System",
        "version": "2.0.0",
        "features": ["Full CRUD operations", "Clean Architecture", "Type Safety"],
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "healthy", "service": "cancionero-backend", "version": "2.0.0"}


@app.get("/api/v1/canciones", response_model=List[CancionResponse], tags=["Canciones"])
async def get_canciones():
    """Obtener todas las canciones"""
    try:
        canciones = cancion_service.get_all_canciones()
        return [
            CancionResponse(
                id_cancion=c.id_cancion,
                titulo=c.titulo,
                autor=c.autor,
                letra=c.letra,
                id_tipo=c.id_tipo,
                estado=c.estado,
                enviado_por=c.enviado_por if c.enviado_por else None,
                fecha_envio=format_datetime(c.fecha_envio)
            ) for c in canciones
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching songs: {str(e)}")


@app.get("/api/v1/canciones/{id_cancion}", response_model=CancionResponse, tags=["Canciones"])
async def get_cancion(id_cancion: int):
    """Obtener una canción específica"""
    try:
        cancion = cancion_service.get_cancion(id_cancion)
        if not cancion:
            raise HTTPException(status_code=404, detail="Song not found")

        return CancionResponse(
            id_cancion=cancion.id_cancion,
            titulo=cancion.titulo,
            autor=cancion.autor,
            letra=cancion.letra,
            id_tipo=cancion.id_tipo,
            estado=cancion.estado,
            enviado_por=cancion.enviado_por if cancion.enviado_por else None,
            fecha_envio=format_datetime(cancion.fecha_envio)
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching song: {str(e)}")


@app.post("/api/v1/canciones", response_model=CancionResponse, status_code=status.HTTP_201_CREATED, tags=["Canciones"])
async def create_cancion(cancion_data: CancionCreate):
    """Crear una nueva canción"""
    try:
        # Crear objeto de dominio desde los datos de la petición
        cancion = Cancion(
            id_cancion=0,  # Será autogenerado por la base de datos
            titulo=cancion_data.titulo,
            autor=cancion_data.autor,
            letra=cancion_data.letra,
            id_tipo=cancion_data.id_tipo,
            estado=cancion_data.estado if cancion_data.estado else "pendiente",
            enviado_por=cancion_data.enviado_por,
            fecha_envio=datetime.now()
        )
        
        # Guardar usando el servicio
        saved_cancion = cancion_service.save_cancion(cancion)
        
        # Usar acceso directo a atributos
        return CancionResponse(
            id_cancion=saved_cancion.id_cancion,
            titulo=saved_cancion.titulo,
            autor=saved_cancion.autor,
            letra=saved_cancion.letra,
            id_tipo=saved_cancion.id_tipo,
            estado=saved_cancion.estado,
            enviado_por=saved_cancion.enviado_por if saved_cancion.enviado_por else None,
            fecha_envio=format_datetime(saved_cancion.fecha_envio)
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating song: {str(e)}")

@app.put("/api/v1/canciones/{id_cancion}", response_model=CancionResponse, tags=["Canciones"])
async def update_cancion(id_cancion: int, cancion_data: CancionUpdate):
    """Actualizar una canción existente"""
    try:
        existing_cancion = cancion_service.get_cancion(id_cancion)
        if not existing_cancion:
            raise HTTPException(status_code=404, detail="Song not found")

        updated_cancion = Cancion(
            id_cancion=existing_cancion.id_cancion,
            titulo=cancion_data.titulo if cancion_data.titulo is not None else existing_cancion.titulo,
            autor=cancion_data.autor if cancion_data.autor is not None else existing_cancion.autor,
            letra=cancion_data.letra if cancion_data.letra is not None else existing_cancion.letra,
            id_tipo=cancion_data.id_tipo if cancion_data.id_tipo is not None else existing_cancion.id_tipo,
            estado=cancion_data.estado if cancion_data.estado is not None else existing_cancion.estado,
            enviado_por=existing_cancion.enviado_por,
            fecha_envio=existing_cancion.fecha_envio
        )

        # Guardar usando el servicio
        saved_cancion = cancion_service.save_cancion(updated_cancion)

        return CancionResponse(
            id_cancion=saved_cancion.id_cancion,
            titulo=saved_cancion.titulo,
            autor=saved_cancion.autor,
            letra=saved_cancion.letra,
            id_tipo=saved_cancion.id_tipo,
            estado=saved_cancion.estado,
            enviado_por=str(saved_cancion.enviado_por) if saved_cancion.enviado_por else None,
            fecha_envio=format_datetime(saved_cancion.fecha_envio)
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error updating song: {str(e)}")


@app.delete("/api/v1/canciones/{id_cancion}", response_model=MessageResponse, tags=["Canciones"])
async def delete_cancion(id_cancion: int):
    """Eliminar una canción"""
    try:
        # Verificar si la canción existe
        existing_cancion = cancion_service.get_cancion(id_cancion)
        if not existing_cancion:
            raise HTTPException(status_code=404, detail="Song not found")

        # Eliminar usando el servicio
        cancion_service.delete_cancion(id_cancion)

        return MessageResponse(message=f"Song with ID {id_cancion} deleted successfully")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error deleting song: {str(e)}")


@app.get("/api/v1/usuarios", response_model=List[UsuarioResponse], tags=["Usuarios"])
async def get_usuarios():
    """Obtener todos los usuarios"""
    try:
        usuarios = usuario_service.get_all_usuarios()
        return [
            UsuarioResponse(
                id_usuario=str(u.get_id_usuario()),
                correo=u.get_correo(),
                nombre=u.get_nombre(),
                id_rol=u.get_id_rol(),
                fecha_creacion=u.get_fecha_creacion().isoformat()
            ) for u in usuarios
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching users: {str(e)}")


@app.get("/api/v1/usuarios/{id_usuario}", response_model=UsuarioResponse, tags=["Usuarios"])
async def get_usuario(id_usuario: str):
    """Obtener un usuario específico"""
    try:
        # Convertir string UUID a objeto UUID
        user_uuid = UUID(id_usuario)
        usuario = usuario_service.get_usuario(user_uuid)
        if not usuario:
            raise HTTPException(status_code=404, detail="User not found")

        return UsuarioResponse(
            id_usuario=str(usuario.get_id_usuario()),
            correo=usuario.get_correo(),
            nombre=usuario.get_nombre(),
            id_rol=usuario.get_id_rol(),
            fecha_creacion=usuario.get_fecha_creacion().isoformat()
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching user: {str(e)}")


@app.post("/api/v1/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED, tags=["Usuarios"])
async def create_usuario(usuario_data: UsuarioCreate):
    """Crear un nuevo usuario"""
    try:
        usuario = Usuario(
            id_usuario=uuid4(),
            correo=usuario_data.correo,
            nombre=usuario_data.nombre,
            id_rol=usuario_data.id_rol,
            fecha_creacion=datetime.now()
        )

        usuario_service.save_usuario(usuario)

        return UsuarioResponse(
            id_usuario=str(usuario.get_id_usuario()),
            correo=usuario.get_correo(),
            nombre=usuario.get_nombre(),
            id_rol=usuario.get_id_rol(),
            fecha_creacion=usuario.get_fecha_creacion().isoformat()
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error creating user: {str(e)}")


@app.get("/api/v1/tipos-canto", response_model=List[TipoCantoResponse], tags=["Tipos de Canto"])
async def get_tipos_canto():
    """Obtener todos los tipos de canto"""
    try:
        tipos = tipo_canto_service.get_all_tipos_canto()
        return [
            TipoCantoResponse(
                id_tipo=t.get_id_tipo(),
                nombre=t.get_nombre(),
                descripcion=t.get_descripcion(),
                orden=t.get_orden()
            ) for t in tipos
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching song types: {str(e)}")


@app.post("/api/v1/tipos-canto", response_model=TipoCantoResponse, status_code=status.HTTP_201_CREATED, tags=["Tipos de Canto"])
async def create_tipo_canto(tipo_data: TipoCantoCreate):
    """Crear un nuevo tipo de canto"""
    try:
        # Crear objeto de dominio
        tipo_canto = TipoCanto(
            id_tipo=0,  # Será autogenerado por la base de datos
            nombre=tipo_data.nombre,
            descripcion=tipo_data.descripcion,
            orden=tipo_data.orden
        )

        # Guardar usando el servicio
        tipo_canto_service.save_tipo_canto(tipo_canto)

        return TipoCantoResponse(
            id_tipo=tipo_canto.get_id_tipo(),
            nombre=tipo_canto.get_nombre(),
            descripcion=tipo_canto.get_descripcion(),
            orden=tipo_canto.get_orden()
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error creating song type: {str(e)}")


@app.get("/api/v1/tiempos-liturgicos", response_model=List[TiempoLiturgicoResponse], tags=["Tiempos Litúrgicos"])
async def get_tiempos_liturgicos():
    """Obtener todos los tiempos litúrgicos"""
    try:
        tiempos = tiempo_liturgico_service.get_all_tiempos_liturgicos()
        return [
            TiempoLiturgicoResponse(
                id_tiempo=t.get_id_tiempo(),
                nombre=t.get_nombre(),
                descripcion=t.get_descripcion(),
                color=t.get_color()
            ) for t in tiempos
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching liturgical times: {str(e)}")


@app.post("/api/v1/tiempos-liturgicos", response_model=TiempoLiturgicoResponse, status_code=status.HTTP_201_CREATED, tags=["Tiempos Litúrgicos"])
async def create_tiempo_liturgico(tiempo_data: TiempoLiturgicoCreate):
    """Crear un nuevo tiempo litúrgico"""
    try:
        # Crear objeto de dominio
        tiempo_liturgico = TiempoLiturgico(
            id_tiempo=0,  # Será autogenerado por la base de datos
            nombre=tiempo_data.nombre,
            descripcion=tiempo_data.descripcion,
            color=tiempo_data.color
        )

        # Guardar usando el servicio
        tiempo_liturgico_service.save_tiempo_liturgico(tiempo_liturgico)

        return TiempoLiturgicoResponse(
            id_tiempo=tiempo_liturgico.get_id_tiempo(),
            nombre=tiempo_liturgico.get_nombre(),
            descripcion=tiempo_liturgico.get_descripcion(),
            color=tiempo_liturgico.get_color()
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error creating liturgical time: {str(e)}")


if __name__ == "__main__":
    print("Starting Cancionero Backend API v2.0.0...")
    print("Full CRUD operations available")
    print("API documentation: http://localhost:8000/docs")
    print("Health check: http://localhost:8000/health")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
