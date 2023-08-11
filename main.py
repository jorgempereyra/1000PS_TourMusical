from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton
import tkinter as tk

#from controllers.buscador import BuscarEventos
from controllers.controlador_principal import ControladorPrincipal
#from controllers.promedio_calificaciones import act_promedio_calificaciones as aprom

from models.evento import Evento
from models.ruta_visita import Ruta
from models.ubicacion import Ubicacion
from models.usuario import Usuario

from views.eventos import Vista_Lista_Eventos
from views.formulario import Vista_Formulario
from views.mapa import Vista_Mapa
from views.buscador import Vista_Buscar

from models.evento import Evento
from models.ubicacion import Ubicacion
from models.usuario import Usuario
from models.ruta_visita import Ruta

current_view = None
root = CTk()

root.geometry("1000x1000")
root.config(bg="black")
root.title('Bienvenido a la aplicación')

def mostrar_lista_eventos():
    global current_view
    if current_view is not None:
        current_view.destroy()
    current_view = Vista_Lista_Eventos(root)
    current_view.pack(fill="both", expand=True)

def mostrar_buscador_eventos():
    global current_view
    if current_view is not None:
        current_view.destroy()
    current_view = Vista_Lista_Eventos(root)
    current_view.pack(fill="both", expand=True)

def mostrar_mapa_eventos():
    global current_view
    if current_view is not None:
        current_view.destroy()
    current_view = Vista_Mapa(root)
    current_view.pack(fill="both", expand=True)

class Vista_Lista_Eventos(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
    Button_Lista_Eventos = CTkButton(root, text="Lista de Eventos", command = mostrar_lista_eventos)
    Button_Lista_Eventos.pack(fill="both", expand=False, padx=10, pady=10)

    Button_Buscador_Eventos = CTkButton(root, text="Buscador de Eventos", command = mostrar_buscador_eventos)
    Button_Buscador_Eventos.pack(fill="both", expand=False, padx=10, pady=10)

    Mis_Eventos = CTkButton(root, text="Mapa de Eventos", command = mostrar_mapa_eventos)
    Mis_Eventos.pack(fill="both", expand=False, padx=10, pady=10)

root.mainloop()

