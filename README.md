# ⚙️ Task Scheduler — API

API REST construida con FastAPI y Firebase Firestore para gestionar tareas automatizadas conectadas a un sistema IoT con ESP32. Parte del sistema completo de automatización de cortina inteligente.

---

## 🏗️ Arquitectura del sistema

```
task-scheduler-frontend  →  task-scheduler-api  →  Firebase Firestore
                                                          ↑
                                               task-scheduler-esp32
```

---

## ✨ Funcionalidades

- CRUD completo de tareas programadas
- Integración con Firebase Firestore
- Manejo de errores con códigos HTTP correctos (404, 503)
- Variables de entorno con `.env`
- CORS configurado para integración con frontend
- Documentación automática con Swagger UI

---

## 🛠️ Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=firebase&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

---

## 📁 Estructura del proyecto

```
task-scheduler-api/
├── app/
│   ├── main.py          # Entrada FastAPI + CORS
│   ├── routes.py        # Endpoints CRUD
│   ├── models.py        # Modelos Pydantic
│   └── database.py      # Conexión Firebase
├── .env                 # ⚠️ No incluido (ver .env.example)
├── requirements.txt
└── README.md
```

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/ELVERRUEDA/task-scheduler-api.git
cd task-scheduler-api

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

---

## ⚙️ Configuración

**1. Firebase** — descarga las credenciales de tu proyecto Firebase y guárdalas como `app/firebase_credentials.json`

**2. Variables de entorno** — crea un archivo `.env` en la raíz:
```
FIREBASE_CREDENTIALS=app/firebase_credentials.json
```

---

## ▶️ Ejecutar

```bash
uvicorn app.main:app --reload --port 8080
```

La API estará disponible en `http://localhost:8080`

Documentación automática en `http://localhost:8080/docs`

---

## 📡 Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Health check |
| GET | `/tareas/` | Obtener todas las tareas |
| POST | `/tareas/` | Crear nueva tarea |
| PUT | `/tareas/{id}` | Editar tarea |
| DELETE | `/tareas/{id}` | Eliminar tarea |
| PATCH | `/tareas/{id}/completado` | Marcar como completada |

---

## 🐳 Docker

```bash
docker run -d -p 8080:8080 task-scheduler-api
```

---

## 🔗 Repositorios relacionados

| Repositorio | Descripción |
|---|---|
| [task-scheduler-frontend](https://github.com/ELVERRUEDA/task-scheduler-frontend) | Frontend React |
| [task-scheduler-esp32](https://github.com/ELVERRUEDA/cortina-automatica-esp32) | Firmware ESP32 + motor DC |

---

## 👤 Autor

**Elver Rueda** — [@ELVERRUEDA](https://github.com/ELVERRUEDA)