from datetime import datetime as dt
from Promedio_calificaciones import act_promedio_calificaciones as aprom
import json as js

class Usuario:
    def __init__(self,nombre,apellido):
        with open('data/BD_Usuarios.json','r') as f:
            usuarios = js.load(f)
        self.id_usuario = usuarios[-1]['id_usuario'] + 1 #int
        self.nombre = nombre #str
        self.apellido = apellido #str
        self.historial_eventos = [] #list
        self.f_creacion = dt.now().date() #str
    
    # Guarda los comentarios en BD_Usuarios.json   
    def addDB(self):
        with open('data/BD_Usuarios.json','r') as f:
            usuarios = js.load(f)
        usuarios.append({
                'id_usuario': self.id_usuario,
                'nombre': self.nombre,
                'apellido': self.apellido,
                'historial_eventos': [],
                'dt_creacion': str(dt.now().date().fromisoformat)
        })       
        with open('data/BD_Usuarios.json','w') as outfile:    
            js.dump(usuarios, outfile, indent=4)

    def __str__(self):
        return f'Soy {self.nombre} mi apellido es {self.apellido} y mi cuenta fue creada el {self.f_creacion}. He visitado {self.historial_rutas}.'

    # Agrega eventos a historial_rutas de BD_Usuarios.json
    def agregar_lista_eventos(self, id_evento):
        with open('data/BD_Usuarios.json','r') as f:
            usuarios = js.load(f)
        usuarios[self.id_usuario-1]['historial_eventos'].append(id_evento)

        with open('data/BD_Usuarios.json','w') as outfile:
            js.dump(usuarios, outfile, indent=4)

    # Genera reviews y las guarda en BD_Reviews.json
    def review(self, id_evento, calificacion, comentario, animo):
        with open('data/BD_Reviews.json','r') as f:
            reviews = js.load(f)
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
            js.dump(reviews, outfile, indent=4)
        
        aprom() #Actualiza promedios de calificaciones

#---PRUEBAS---        
User1 = Usuario('Juaon', 'Paepgfjfjinoz')
User1.review(9, 10,'Excelente servicio', 'Feliz')
User1.crear()
#print (User1)
