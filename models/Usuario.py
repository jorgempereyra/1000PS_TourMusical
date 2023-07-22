from datetime import datetime as dt
from Promedio_calificaciones import act_promedio_calificaciones as aprom
import json

class Usuario:
    def __init__(self,nombre,apellido):
        with open('data/BD_Usuarios.json','r') as f:
            usuarios = json.load(f)
        self.id_usuario = usuarios[-1]['id_usuario'] + 1
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = []
        self.f_creacion = dt.now().date()
    
    # Guarda los comentarios en BD_Usuarios.json   
        usuarios.append({
                'id_usuario': self.id_usuario,
                'nombre': self.nombre,
                'apellido': self.apellido,
                'historial_rutas': [],
                'dt_creacion': str(dt.now().date())
        })       
        with open('data/BD_Usuarios.json','w') as outfile:    
            json.dump(usuarios, outfile, indent=4)

    def __str__(self):
        return f'Soy {self.nombre} mi apellido es {self.apellido} y mi cuenta fue creada el {self.f_creacion}. He visitado {self.historial_rutas}.'

    # Agrega eventos a historial_rutas de BD_Usuarios.json
    def visitar_ruta(self, id_ruta):
        with open('data/BD_Usuarios.json','r') as f:
            usuarios = json.load(f)
        usuarios[self.id_usuario-1]['historial_rutas'].append(id_ruta)

        with open('data/BD_Usuarios.json','w') as outfile:
            json.dump(usuarios, outfile, indent=4)

    # Genera reviews y las guarda en BD_Reviews.json
    def review(self, id_evento, calificacion, comentario, animo):
        with open('data/BD_Reviews.json','r') as f:
            reviews = json.load(f)
            reviews.append({
                'id_review': int(reviews[-1]['id_review'] + 1),
                'id_evento': id_evento,
                'id_usuario': self.id_usuario,
                'calificacion': calificacion,
                'comentario': comentario,            
                'animo': animo,
                'dt_creacion': str(dt.now().date())
            })        
        with open('data/BD_Reviews.json','w') as outfile:    
            json.dump(reviews, outfile, indent=4)
        
        aprom() #Actualiza promedios de calificaciones
#---PRUEBAS---        
User1 = Usuario('Juaon', 'Paepgfjfjinoz')
User1.review(9, 10,'Excelente servicio', 'Feliz')
#User1.visitar_ruta(6)
#print (User1)
