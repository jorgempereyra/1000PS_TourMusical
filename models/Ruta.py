from datetime import datetime as dt
import json

class Ruta:
    def __init__(self,nombre,*args):
        with open('data/BD_Rutas.json','r') as f:
            rutas = json.load(f)
        self.id_ruta = rutas[-1]['id_ruta'] + 1
        self.nombre = nombre
        self.eventos = args
        self.f_creacion = dt.now().date()
    
    # Guarda las rutas en BD_Rutas.json   
        rutas.append({
                'id_ruta': self.id_ruta,
                'nombre': self.nombre,
                'eventos': self.eventos,
                'dt_creacion': str(dt.now().date())
        })       
        with open('data/BD_Rutas.json','w') as outfile:    
            json.dump(rutas, outfile, indent=4)

    def __str__(self):
        return f'Soy {self.nombre} y tengo estos eventos {self.eventos} y mi cuenta fue creada el {self.f_creacion}.'

    # Agrega eventos a rutas de BD_Rutas.json
    def agregar_evento(self, *args):
        with open('data/BD_Rutas.json','r') as f:
            rutas = json.load(f)
        rutas[self.id_ruta-1]['eventos'].extend(args)

        with open('data/BD_Rutas.json','w') as outfile:
            json.dump(rutas, outfile, indent=4)

    
#---PRUEBAS---        
#Ruta1 = Ruta('Vino',1,2,3,6)
#Ruta1.agregar_evento(9)
#print (User1)
