from datetime import datetime as dt
import json

class Evento:
    def __init__(self, nombre, id_ubicacion, descripcion, imagen):
        with open('data/BD_Eventos.json','r') as f:
            eventos = json.load(f)
        self.id_evento = eventos[-1]['id_evento'] + 1
        self.nombre = nombre
        self.id_ubicacion = id_ubicacion
        self.descripcion = descripcion
        self.imagen = imagen
        self.f_creacion = dt.now().date()
    
    # Guarda las eventos en BD_Eventos.json   
        eventos.append({
                'id_evento': self.id_evento,
                'nombre': self.nombre,
                'id_ubicacion': self.id_ubicacion,
                'descripcion': self.descripcion,
                'imagen': self.imagen,
                'dt_creacion': str(dt.now().date())
        })       
        with open('data/BD_Eventos.json','w') as outfile:    
            json.dump(eventos, outfile, indent=4)

    def __str__(self):
        return f'Soy el evento {self.nombre} y tengo estos datos {self.id_evento}, {self.id_ubicacion}, {self.descripcion}, {self.imagen} . Fui creado el {self.f_creacion}.'

    '''# Agrega eventos a BD_Eventos.json
    def crear_eventos(self, *args):
        with open('data/BD_Eventos.json','r') as f:
            eventos = json.load(f)
        eventos[self.id_evento-1]['eventos'].extend(args)

        with open('data/BD_Eventos.json','w') as outfile:
            json.dump(eventos, outfile, indent=4)
'''
    
#---PRUEBAS---        
Evento1 = Evento('Vino',1,"abc123","/123.jpg")
#print (User1)
