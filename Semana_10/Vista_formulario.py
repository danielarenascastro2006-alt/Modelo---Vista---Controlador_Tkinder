import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.inicios = None
        self.controlador = None
        # Atributos del UML
        self.titulo = "Registro de Sesión"
        self.pregunta_campo_numero = "Digite un número"
        # Inicializamos entry_usuario en None para evitar el AttributeError
        self.entry_usuario = None 
        
    def set_controlador(self, controlador):
        self.controlador = controlador
        
    def iniciar_ventana(self):
        self.inicios = Ventana.Tk()
        self.inicios.title(self.titulo)
        self.inicios.geometry("400x350")
    
    def formulario(self):
        Ventana.Label(self.inicios, text=self.pregunta_campo_numero).pack(pady=5)
        
        # Aquí se crea el atributo que te daba error
        self.entry_usuario = Ventana.Entry(self.inicios)
        self.entry_usuario.pack(pady=5)

        # Usamos lambda para conectar con el controlador
        boton = Ventana.Button(self.inicios, text="Enviar", command=lambda: self.enviar())
        boton.pack(pady=10)

        self.label_resultado = Ventana.Label(self.inicios, text="")
        self.label_resultado.pack(pady=10)
        
    def pedir_numero(self):
        # Verificamos que el entry exista y no esté vacío
        if self.entry_usuario:
            try:
                return int(self.entry_usuario.get())
            except ValueError:
                return 0
        return 0
    
    def enviar(self):
        self.controlador.tomar_numero()
    
    def imprimir_mensaje(self, dato_mensaje):
        self.label_resultado.config(text=dato_mensaje)

    def imprimir_numero(self, dato_numero):
        print(f"Número en vista: {dato_numero}")
