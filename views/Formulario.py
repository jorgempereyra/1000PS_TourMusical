# formulario.py
import customtkinter as CTkField
from tkinter import filedialog
import json
from models.evento import Evento

Evento1 = Evento('Vino',1,"abc123","/123.jpg")
print(Evento1.from_json())