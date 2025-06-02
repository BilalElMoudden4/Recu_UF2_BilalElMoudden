import json

#Faltan cosas pero que puesto lo que sabia
def transformador(resultados):
    def convertir_info(info):
        return info
    
    if resultados is None:
        return None
            
        # Que los nombres se vean bien y no con faltas
        clave_es = {
            'nombre': 'nombre',
            'apellido': 'apellido',
            'email': 'email',
            'curso': 'curso',
            'ano': 'año',
            'direccion': 'dirección',
            'id': 'id'
        }
        
    
    return 