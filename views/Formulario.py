# formulario.py

import customtkinter as ctk
from tkinter import filedialog
import json
from ..models.Evento import Evento

def guardar_evento():
    nombre = entry_nombre.get()
    artista = entry_artista.get()
    genero = entry_genero.get()
    id_ubicacion = entry_id_ubicacion.get()
    hora_inicio = entry_hora_inicio.get()
    hora_fin = entry_hora_fin.get()
    descripcion = text_descripcion.get("1.0", ctk.tk.END).strip()
    imagen = entry_imagen.get()

    evento = Evento(nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen)

    with open('data/BD_Eventos.json', 'r') as f:
        eventos = json.load(f)

    eventos.append({
        'id_evento': evento.id_evento,
        'nombre': evento.nombre,
        'artista': evento.artista,
        'genero': evento.genero,
        'id_ubicacion': evento.id_ubicacion,
        'hora_inicio': evento.hora_inicio,
        'hora_fin': evento.hora_fin,
        'descripcion': evento.descripcion,
        'imagen': evento.imagen,
        'promedio_valoraciones': evento.promedio_valoraciones,
        'f_creacion': str(evento.f_creacion),
    })

    with open('data/BD_Eventos.json', 'w') as f:
        json.dump(eventos, f, indent=4)

    # Mostrar un mensaje de éxito
    label_mensaje.config(text="Evento guardado exitosamente.", fg="#A1A892")

# Crear ventana principal
ventana = ctk.tk.CTk()

# Cambiar el color de fondo de la ventana
ventana.config(bg="#E5E5E5")

ventana.set_theme("light")

# Crear widgets
label_nombre = ctk.Label(ventana, text="Nombre:", font=("Arial", 12), bg="#E5E5E5")
entry_nombre = ctk.Entry(ventana)

# Resto del código igual al formulario anterior