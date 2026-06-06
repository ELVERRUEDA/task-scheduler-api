from fastapi import APIRouter, HTTPException
from app.models import Tarea, EstadoCompletado
from app.database import db
from google.cloud.exceptions import GoogleCloudError

router = APIRouter()

def tarea_a_dict(tarea_ref):
    """Convierte un documento de Firestore a diccionario normalizado."""
    data = tarea_ref.to_dict()
    return {
        "id": tarea_ref.id,
        "titulo": data.get("titulo", ""),
        "descripcion": data.get("descripcion", ""),
        "hora": data.get("hora", ""),
        "fecha": data.get("fecha", ""),
        "completado": data.get("completado", data.get("completada", False))
    }

# Obtener todas las tareas
@router.get("/tareas/")
def obtener_tareas():
    try:
        tareas_ref = db.collection("tareas").stream()
        return [tarea_a_dict(t) for t in tareas_ref]
    except GoogleCloudError as e:
        raise HTTPException(status_code=503, detail=f"Error al conectar con Firebase: {str(e)}")

# Crear una nueva tarea
@router.post("/tareas/", status_code=201)
def crear_tarea(tarea: Tarea):
    try:
        nueva_tarea_ref = db.collection("tareas").document()
        tarea_data = tarea.dict()
        tarea_data.setdefault("completado", False)
        tarea_data.setdefault("fecha", "")
        nueva_tarea_ref.set(tarea_data)
        return {"id": nueva_tarea_ref.id, **tarea_data}
    except GoogleCloudError as e:
        raise HTTPException(status_code=503, detail=f"Error al crear tarea: {str(e)}")

# Eliminar una tarea por ID
@router.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: str):
    try:
        tarea_ref = db.collection("tareas").document(tarea_id)
        if not tarea_ref.get().exists:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        tarea_ref.delete()
        return {"mensaje": "Tarea eliminada correctamente"}
    except HTTPException:
        raise
    except GoogleCloudError as e:
        raise HTTPException(status_code=503, detail=f"Error al eliminar tarea: {str(e)}")

# Editar una tarea por ID
@router.put("/tareas/{tarea_id}")
def editar_tarea(tarea_id: str, tarea: Tarea):
    try:
        tarea_ref = db.collection("tareas").document(tarea_id)
        doc = tarea_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        tarea_data = tarea.dict()
        tarea_data.setdefault("completado", doc.to_dict().get("completado", False))
        tarea_ref.update(tarea_data)
        return {"mensaje": "Tarea actualizada correctamente"}
    except HTTPException:
        raise
    except GoogleCloudError as e:
        raise HTTPException(status_code=503, detail=f"Error al editar tarea: {str(e)}")

# Marcar tarea como completada/incompleta
@router.patch("/tareas/{tarea_id}/completado")
def actualizar_estado_completado(tarea_id: str, estado: EstadoCompletado):
    try:
        tarea_ref = db.collection("tareas").document(tarea_id)
        if not tarea_ref.get().exists:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        tarea_ref.update({"completado": estado.completado})
        return {"mensaje": f"Tarea actualizada: completado = {estado.completado}"}
    except HTTPException:
        raise
    except GoogleCloudError as e:
        raise HTTPException(status_code=503, detail=f"Error al actualizar estado: {str(e)}")