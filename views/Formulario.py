# formulario.py
from customtkinter import CTkFrame, CTkLabel

class Vista_Formulario(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.label = CTkLabel(self, text="Esta es la vista de Formulario")
        self.label.pack(fill="both", expand=True, padx=10, pady=10)