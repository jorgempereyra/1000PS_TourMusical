from views.mapa import Vista_Mapa
from models.evento import Evento
from models.ubicacion import Ubicacion
from PIL import Image, ImageTk

class ControladorPrincipal:
    def __init__(self, root):
        self.vista = Vista_Mapa(root, self.seleccionar_local, seleccionar_ubicacion)
        self.eventos = Evento.cargar_eventos("app/data/eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("app/data/ubicaciones.json")
        self.marcadores = []
        self.imagenes = []

        self.cargar_eventos()
        self.cargar_imagenes()
        self.cargar_marcadores()
        
    def cargar_eventos(self):
        for evento in self.eventos:
            self.vista.agregar_evento(evento)
        
    def cargar_imagenes(self):
        for evento in self.eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"app/views/images/{evento.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for ubicacion, evento in zip(self.ubicaciones, self.eventos):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, evento.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_local(self, evento):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.lista_eventos.curselection()
        # Obtiene el evento seleccionado
        local_seleccionado = self.eventos[indice_seleccionado[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        # Busca la ubicación correspondiente al evento seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == local_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        # Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)

        print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}")

def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print("Ubicación seleccionada: ", marcador.text)