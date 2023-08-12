from customtkinter import CTkFrame, CTkComboBox
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

class Vista_Mapa():
    def __init__(self, root, seleccionar_local_callback=None, seleccionar_ubicacion_callback=None):
        self.root = root
        self.seleccionar_local_callback = seleccionar_local_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.frame_mapa = CTkFrame(self.root, width=root.winfo_width(), height=root.winfo_height())
        self.frame_mapa.pack(side='right')

        self.frame_eventos = CTkFrame(self.root, width=root.winfo_width(), height=root.winfo_height())
        self.frame_eventos.pack(side='left', fill='both', expand=True)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=500, height=500, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)


