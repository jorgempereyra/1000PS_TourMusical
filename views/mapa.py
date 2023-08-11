from customtkinter import CTkFrame, CTkComboBox
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

class Vista_Mapa(CTk):
    def __init__(self, root, seleccionar_local_callback=None, seleccionar_ubicacion_callback=None):
        self.root = root
        self.seleccionar_local_callback = seleccionar_local_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.frame_mapa = CTkFrame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='right')

        self.frame_eventos = CTkFrame(self.root, width=300, height=600)
        self.frame_eventos.pack(side='left', fill='both', expand=True)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        # Listbox para los eventos
        self.lista_eventos = CTkComboBox(self.frame_eventos)
        self.lista_eventos.bind('<<ListboxSelect>>', seleccionar_local_callback)
        self.lista_eventos.pack(fill='both', expand=True)

    def agregar_evento(self, evento):
        nombre = evento.nombre
        self.lista_eventos.insert(CTk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)


