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


root.mainloop()

