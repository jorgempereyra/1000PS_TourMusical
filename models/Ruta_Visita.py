from datetime import datetime as dt
import json

class Ruta:
    def __init__(self,nombre,*args):
        with open('data/BD_Rutas_Visitas.json','r') as f:
            rutas = json.load(f)
        self.id_ruta = rutas[-1]['id_ruta'] + 1 #int
        self.nombre = nombre #str
        self.eventos = args #list
        self.f_creacion = dt.now().isoformat() #str
        
    # Guarda las rutas en BD_Rutas_Visitas.json   
    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_ubicaciones():
        with open('data/BD_Rutas_Visitas.json', "r") as archivo:
            datos = json.load(archivo)
        return [Ruta.de_json(json.dumps(dato)) for dato in datos]

    def __str__(self):
        return f'Soy {self.nombre} y tengo estos eventos {self.eventos} y mi cuenta fue creada el {self.f_creacion}.'

    # Agrega eventos a rutas de BD_Rutas_Visitas.json
    def add_eventos(self, *args):
        with open('data/BD_Rutas_Visitas.json','r') as f:
            rutas = json.load(f)
        rutas[self.id_ruta-1]['eventos'].extend(args)

        with open('data/BD_Rutas_Visitas.json','w') as outfile:
            json.dump(rutas, outfile, indent=4)

    
#---PRUEBAS---        
#Ruta1 = Ruta('Vino',1,2,3,6)
#Ruta1.agregar_evento(9)
#print (User1)
