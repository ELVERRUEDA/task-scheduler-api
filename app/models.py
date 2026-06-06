from pydantic import BaseModel
from typing import Optional

class Tarea(BaseModel):
    titulo: str
    descripcion: Optional[str] = ""
    hora: Optional[str] = ""
    fecha: Optional[str] = ""
    completado: Optional[bool] = False

class EstadoCompletado(BaseModel):
    completado: bool