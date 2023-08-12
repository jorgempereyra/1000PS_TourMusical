from customtkinter import CTk,CTkFrame, CTkButton
from views.eventos import Vista_Lista_Eventos
from views.formulario import Vista_Formulario
from views.mapa import Vista_Mapa
from views.buscador import Vista_Buscar

current_view = None
root = CTk()

root.geometry("1000x1000")
root.config(bg="black")
root.title('Bienvenido a la aplicación')

root.mainloop()

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

class Vista_Principal(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = root
        self.lista_eventos_button = CTkButton(root, text="Lista de Eventos", command = mostrar_lista_eventos)
        self.lista_eventos_button.pack(fill="both", expand=False, padx=10, pady=10)

        Button_Buscador_Eventos = CTkButton(root, text="Buscador de Eventos", command = mostrar_buscador_eventos)
        Button_Buscador_Eventos.pack(fill="both", expand=False, padx=10, pady=10)

        Mis_Eventos = CTkButton(root, text="Mapa de Eventos", command = mostrar_mapa_eventos)
        Mis_Eventos.pack(fill="both", expand=False, padx=10, pady=10)

