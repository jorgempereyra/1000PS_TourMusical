from customtkinter import CTkFrame, CTkLabel

class Vista_Lista_Eventos(CTkFrame):
    def __init__(self,root, master=None):
        super().__init__(master)
        self.root = root
        self.label = CTkLabel(self, text="Esta es la vista de Lista de Eventos")
        self.label.pack(fill="both", expand=True, padx=10, pady=10)