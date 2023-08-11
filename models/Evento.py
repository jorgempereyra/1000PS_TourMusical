from datetime import datetime as dt
import json

class Evento:
    def __init__(self, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        with open('data/BD_Eventos.json','r') as f:
            eventos = json.load(f)
        self.id_evento = eventos[-1]['id_evento'] + 1
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen
        self.promedio_valoraciones = 0
        self.f_creacion = dt.now().date()
    
    # Lee las eventos en BD_Eventos.json   
    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_eventos():
        with open('data/BD_Eventos.json', "r") as archivo:
            datos = json.load(archivo)
        return [Evento.de_json(json.dumps(dato)) for dato in datos]
            
    def __str__(self):
        return f'Soy el evento {self.nombre} y tengo estos datos {self.id_evento}, {self.id_ubicacion}, {self.descripcion}, {self.imagen} . Fui creado el {self.f_creacion}.'
  
#---PRUEBAS---        
#Evento1 = Evento('Vino',1,"abc123","/123.jpg")
#print (User1)
