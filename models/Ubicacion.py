from datetime import datetime as dt
import json

class Ubicacion:
    def __init__(self, nombre, direccion, latitud, longitud):
        with open('data/BD_Ubicaciones.json','r') as f:
            ubicaciones = json.load(f)
        self.id_ubicacion = ubicaciones[-1]['id_ubicacion'] + 1 #int
        self.nombre = nombre #str
        self.direccion = direccion #str
        self.coordenadas = [latitud,longitud] #float
        self.f_creacion = dt.now().isoformat() #str
    
    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_ubicaciones():
        with open('data/BD_Ubicaciones.json', "r") as archivo:
            datos = json.load(archivo)
        return [Ubicacion.de_json(json.dumps(dato)) for dato in datos]

    def __str__(self):
        return f'Soy la ubicacion {self.id_ubicacion}, estoy en {self.direccion} en coordenadas {self.coordenadas} y fui agregado el {self.f_creacion}'    
    
#---PRUEBAS---        
#Ubi1 = Ubicacion('Hotel','Calle 1', 3.4, 4.4)

