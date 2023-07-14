from datetime import datetime as dt
import json

#Fuente de datos
with open('BD_Comentarios.json') as file:
    data = json.load(file)
    lista_comentarios = data['personas']
    print(data)


class Comentario():
    def __init__(self, usuario, lugar, comentario, calificacion):
        self.usuario = usuario
        self.lugar = lugar
        self.comentario = comentario
        self.calificacion = calificacion
        self.dt_creacion = dt.now().date().isoformat()
        
    def __str__(self):
        return f'Este comentario fue escrito el {self.dt_creacion} por {self.usuario} para {self.lugar} con {self.calificacion} y dice {self.comentario}'


class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.f_creacion = dt.now().date().isoformat()

    def __str__(self):
        return f'Soy {self.nombre} mi mail es {self.email} y mi cuenta fue creada el {self.f_creacion}'

    def comentar(self,comentario,calificacion):
        lista_comentarios.append (Comentario(self.nombre,'lugar',comentario,calificacion))





        
User1 = Usuario('Juan Perez','juanperez@algo.com')

User1.comentar('Hola Mundo','5')

#print (User1)
print (lista_comentarios)
#print (lista_comentarios[-1])
