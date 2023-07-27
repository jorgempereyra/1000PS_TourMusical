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
    
    # Guarda los comentarios en BD_Ubicaciones.json   
    def addDB(self):
        with open('data/BD_Ubicaciones.json','r') as f:
            ubicaciones = json.load(f)  
        ubicaciones.append({
                'id_ubicacion': self.id_ubicacion,
                'ubicacion': self.nombre,
                'direccion': self.direccion,
                'coordenadas': self.coordenadas,
                'dt_creacion': str(dt.now().isoformat())
        })       
        with open('data/BD_Ubicaciones.json','w') as outfile:    
            json.dump(ubicaciones, outfile, indent=4)

    def __str__(self):
        return f'Soy la ubicacion {self.id_ubicacion}, estoy en {self.direccion} en coordenadas {self.coordenadas} y fui agregado el {self.f_creacion}'    
    #Calcula promedio de calificaciones
    
#---PRUEBAS---        
Ubi1 = Ubicacion('Hotel','Calle 1', 3.4, 4.4)

