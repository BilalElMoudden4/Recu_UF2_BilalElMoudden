from fastapi import FastAPI, Form
from services.user_service import crear_usuario


app = FastAPI()

@app.post("/usuarios/",)
async def crear_usuario(
    nombre: str = Form(...),
    apellido: str = Form(...),
    email: str = Form(...),
    descripcion: str = Form(None),
    curso: str = Form(...),
    ano: int = Form(...),
    direccion: str = Form(...),
    cp: str = Form(None),
    password: str = Form(...)
):
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "descripcion": descripcion,
        "curso": curso,
        "ano": ano,
        "direccion": direccion,
        "cp": cp,
        "password": password
    }
    
    resultado = await crear_usuario(datos)
    return resultado

