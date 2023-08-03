import json as js
def BuscarEventos():
    with open('data/BD_Eventos.json','r') as f:
        eventos = js.load(f)
    eventos
    return