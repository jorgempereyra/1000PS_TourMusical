from datetime import datetime as dt
import json

class Ubicacion:
    def __init__(self, ubicacion, direccion, latitud, longitud):
        with open('data/BD_Ubicaciones.json','r') as f:
            ubicaciones = json.load(f)
        self.id_ubicacion = ubicaciones[-1]['id_ubicacion'] + 1
        self.ubicacion = ubicacion
        self.direccion = direccion
        self.coordenadas = [latitud,longitud]
        self.f_creacion = dt.now().date()
    # Guarda los comentarios en BD_Ubicaciones.json   
        ubicaciones.append({
                'id_ubicacion': self.id_ubicacion,
                'ubicacion': self.ubicacion,
                'direccion': self.direccion,
                'coordenadas': self.coordenadas,
                'dt_creacion': str(dt.now().date())
        })       
        with open('data/BD_Ubicaciones.json','w') as outfile:    
            json.dump(ubicaciones, outfile, indent=4)

    def __str__(self):
        return f'Soy la ubicacion {self.id_ubicacion}, estoy en {self.direccion} en coordenadas {self.coordenadas} y fui agregado el {self.f_creacion}'    
    #Calcula promedio de calificaciones
    def promedio_calificaciones():   
        with open("data/BD_Reviews.json", "r") as f_com:
            reviews = json.load(f_com)
            promedio = sum(int(reviews['calificacion'])*(reviews['calificacion']==reviews['calificacion']) for calificacion in calificaciones) / len(calificaciones)

        #Guarda el valor del promedio en BD_Variables.json
        with open("data/BD_Ubicaciones.json", "r") as f_var:    
            variables = json.load(f_var)
            variables['Promedio_Calificaciones'] = round(promedio,2)

        with open("data/BD_Ubicaciones.json", "w") as f_var:
            json.dump(variables, f_var, indent=4)

#---PRUEBAS---        
Ubi1 = Ubicacion('Hotel','Calle 1', 3.4, 4.4)
#Ubi1.promedio_calificaciones()
#print (User1)
#print (comentarios)

