import json
def BuscarEventos():
    with open('data/BD_Eventos.json','r') as f:
        eventos = json.load(f)
    eventos
    return