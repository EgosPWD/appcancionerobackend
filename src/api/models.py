from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID

# Modelos de Canción
class CancionCreate(BaseModel):
    titulo: str = Field(..., description="Título de la canción")
    autor: Optional[str] = Field(None, description="Autor de la canción")
    letra: Optional[str] = Field(None, description="Letra de la canción")
    id_tipo: Optional[int] = Field(None, description="ID del tipo de canto")
    estado: Optional[str] = Field("pendiente", description="Estado de la canción")
    enviado_por: Optional[UUID] = Field(None, description="Usuario que envió la canción")


class CancionUpdate(BaseModel):
    titulo: Optional[str] = Field(None, description="Título de la canción")
    autor: Optional[str] = Field(None, description="Autor de la canción")
    letra: Optional[str] = Field(None, description="Letra de la canción")
    id_tipo: Optional[int] = Field(None, description="ID del tipo de canto")
    estado: Optional[str] = Field(None, description="Estado de la canción")


class CancionResponse(BaseModel):
    id_cancion: int
    titulo: str
    autor: Optional[str]
    letra: Optional[str]
    id_tipo: Optional[int]
    estado: Optional[str]
    enviado_por: Optional[str]
    fecha_envio: Optional[str]

# Modelos de Usuario
class UsuarioCreate(BaseModel):
    correo: str = Field(..., description="Correo electrónico del usuario")
    nombre: str = Field(..., description="Nombre del usuario")
    id_rol: Optional[int] = Field(None, description="ID del rol del usuario")


class UsuarioUpdate(BaseModel):
    correo: Optional[str] = Field(None, description="Correo electrónico del usuario")
    nombre: Optional[str] = Field(None, description="Nombre del usuario")
    id_rol: Optional[int] = Field(None, description="ID del rol del usuario")


class UsuarioResponse(BaseModel):
    id_usuario: str
    correo: str
    nombre: str
    id_rol: Optional[int]
    fecha_creacion: str

# Modelos de Artículo
class ArticuloCreate(BaseModel):
    titulo: str = Field(..., description="Título del artículo")
    contenido: str = Field(..., description="Contenido del artículo")
    creado_por: Optional[UUID] = Field(None, description="Usuario que creó el artículo")


class ArticuloUpdate(BaseModel):
    titulo: Optional[str] = Field(None, description="Título del artículo")
    contenido: Optional[str] = Field(None, description="Contenido del artículo")


class ArticuloResponse(BaseModel):
    id_articulo: int
    titulo: str
    contenido: str
    creado_por: Optional[str]
    fecha_creacion: str

# Modelos de Repertorio
class RepertorioCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del repertorio")
    descripcion: Optional[str] = Field(None, description="Descripción del repertorio")
    id_tiempo: Optional[int] = Field(None, description="ID del tiempo litúrgico")
    creado_por: Optional[UUID] = Field(None, description="Usuario que creó el repertorio")
    fecha: Optional[datetime] = Field(None, description="Fecha del repertorio")
    tipo_misa: Optional[str] = Field(None, description="Tipo de misa")


class RepertorioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, description="Nombre del repertorio")
    descripcion: Optional[str] = Field(None, description="Descripción del repertorio")
    id_tiempo: Optional[int] = Field(None, description="ID del tiempo litúrgico")
    fecha: Optional[datetime] = Field(None, description="Fecha del repertorio")
    tipo_misa: Optional[str] = Field(None, description="Tipo de misa")


class RepertorioResponse(BaseModel):
    id_repertorio: int
    nombre: str
    descripcion: Optional[str]
    id_tiempo: Optional[int]
    creado_por: Optional[str]
    fecha_creacion: str
    fecha: Optional[str]
    tipo_misa: Optional[str]

# Modelos de Tipo de Canto
class TipoCantoCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del tipo de canto")
    descripcion: Optional[str] = Field(None, description="Descripción del tipo de canto")
    orden: Optional[int] = Field(None, description="Orden de visualización")


class TipoCantoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, description="Nombre del tipo de canto")
    descripcion: Optional[str] = Field(None, description="Descripción del tipo de canto")
    orden: Optional[int] = Field(None, description="Orden de visualización")


class TipoCantoResponse(BaseModel):
    id_tipo: int
    nombre: str
    descripcion: Optional[str]
    orden: Optional[int]

# Modelos de Tiempo Litúrgico
class TiempoLiturgicoCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del tiempo litúrgico")
    descripcion: Optional[str] = Field(None, description="Descripción del tiempo litúrgico")
    color: Optional[str] = Field(None, description="Color litúrgico")


class TiempoLiturgicoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, description="Nombre del tiempo litúrgico")
    descripcion: Optional[str] = Field(None, description="Descripción del tiempo litúrgico")
    color: Optional[str] = Field(None, description="Color litúrgico")


class TiempoLiturgicoResponse(BaseModel):
    id_tiempo: int
    nombre: str
    descripcion: Optional[str]
    color: Optional[str]

# Modelos genéricos de respuesta
class MessageResponse(BaseModel):
    message: str  # Mensaje de respuesta


class ErrorResponse(BaseModel):
    error: str  # Mensaje de error
    detail: Optional[str] = None  # Detalle adicional del error
