from datetime import datetime as dt
import json
import math

class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.f_creacion = dt.now().date()

    def __str__(self):
        return f'Soy {self.nombre} mi mail es {self.email} y mi cuenta fue creada el {self.f_creacion}'

    # Guarda los comentarios en BD_Comentarios.json
    def comentar(self,comentario,lugar,calificacion):
        with open('BD_Comentarios.json','r') as file:
            comentarios = json.load(file)
            comentarios.append({
                'nombre': self.nombre,
                'comentario': comentario,
                'lugar': lugar,
                'calificacion': calificacion,
                'dt_creacion': str(dt.now().date())
            })        
        with open('BD_Comentarios.json','w') as outfile:    
            json.dump(comentarios, outfile, indent=4)
        
        #Guarda promedio
        with open("BD_Comentarios.json", "r") as f:
            calificaciones = json.load(f)

        # Calcular el promedio de las calificaciones.
        promedio = sum(calificaciones["calificacion"] for calificacion in calificaciones) / len(calificaciones)

        with open('BD_Variables.json','r') as file:    
            calificaciones=json.load(file)
            calificaciones['Promedio_Calificaciones']= promedio
        
        with open('BD_Variables.json','w') as outfile:
            json.dump(calificaciones, outfile, indent=4)

        #print (lista_comentarios)





#---PRUEBAS---        
User1 = Usuario('Juan Perez','juanperez@algo.com')

User1.comentar('Hola Mundo','Hotel','241')
#print (User1)
#print (comentarios)

