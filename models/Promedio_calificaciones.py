import json as js   
def act_promedio_calificaciones():   
        total_sum, count = 0, 0
        # Carga desde BD_Reviews.json
        with open("data/BD_Reviews.json", "r") as f_rev:
            reviews = js.load(f_rev)
        with open("data/BD_Eventos.json", "r") as f_eve:
            eventos = js.load(f_eve)
        # Busca coincidencias entre BD_Reviews.json y BD_Eventos.json para el campo 'id_evento'
            for evento in eventos:
                for review in reviews:
                    if (review['id_evento'] == evento['id_evento']):
                        total_sum += review['calificacion']
                        count += 1
                        # Calcula promedio
                        promedio = total_sum / count
                        # Sobreescribe valor en temporal
                        evento['promedio_valoraciones'] = round(promedio, 2)
                total_sum, count = 0, 0
        # Actualiza Promedio_Calificaciones en BD_Eventos.json           
            with open("data/BD_Eventos.json", "w") as f_even:
                js.dump(eventos, f_even, indent=4)

#act_promedio_calificaciones()