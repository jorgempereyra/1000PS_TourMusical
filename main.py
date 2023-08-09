from views.eventos import VistaInicio
from views.vista_juegos import VistaJuegos
from views.vista_info import VistaInfo
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_juegos import ControladorJuegos
from controllers.controlador_info import ControladorInfo


from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton
root = CTk()

root.geometry("500x500")
root.config(bg = "black")
root.title('Bienvenido a la aplicación')
print(str(root._current_width))
print(str(root._current_height))

Button_Lista_Eventos = CTkLabel(root, text="Lista de Eventos")
Button_Lista_Eventos.pack(fill = "both", expand=False, padx=10, pady=10)

Button_Buscador_Eventos = CTkLabel(root, text="Buscador de Eventos")
Button_Buscador_Eventos.pack(fill = "both", expand=False, padx=10, pady=10)

Mis_Eventos = CTkLabel(root, text="Lista de Eventos")
Mis_Eventos.pack(fill="both", expand = False, padx=10, pady=10)
