from fastapi import FastAPI, Form
from services.user_service import crear_usuario #Aqui esta el problema
#Aqui deberia ir el import del HttpException pero no lo recuerdo

app = FastAPI()

@app.post("/usuarios/",) #Dentro deberia ir algo mas pero no lo recuerdo
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


@app.get("/usuarios/{email}")
async def leer_usuario(email: str):
    usuario = await leer_usuario(email)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado") #Falta el import!!!!! (da probelmas)
    return usuario


@app.put("/usuarios/{email}")
async def actualizar_usuario(
    email: str,
    apellido: str = Form(None),
    direccion: str = Form(None)
):
    if not apellido and not direccion:
        raise HTTPException( #Aqui tambien da error por el import que no recuerdo
            status_code=400,
            detail="Hay que rellenar minimo 1"
        )
    
    actualizacion = {
        "apellido": apellido,
        "direccion": direccion
    }
    
    resultado = await actualizar_usuario(email, actualizacion)
    return resultado


