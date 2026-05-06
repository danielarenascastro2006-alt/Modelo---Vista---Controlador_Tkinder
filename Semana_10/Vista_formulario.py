import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.color="grey"
        self.entry_usuario= " "
        self.label_usuario=" "
        self.inicios=" "
        
    def iniciar_ventana(self):
        self.inicios = Ventana.Tk()
        self.inicios.title("registro de Sesión")
        self.inicios.geometry("600x650")
        self.inicios.resizable()
        self.inicios.configure(bg="#121212", padx=20, pady=20, cursor="hand2")
        return self.inicios
    
    def formulario(self):
        label_usuario = Ventana.Label(self.inicios, text="Digite un número")
        label_usuario.pack(pady=5)

        self.entry_usuario = Ventana.Entry(self.inicios)
        self.entry_usuario.pack(pady=5)

        boton = Ventana.Button(self.inicios, text="Enviar", command=self.enviar)
        boton.pack(pady=10)

        self.label_resultado = Ventana.Label(self.inicios, text="")
        self.label_resultado.pack(pady=10)
        
    def pedir_numero(self):
        return int(self.entry_usuario.get())
    
    def enviar(self):
        self.controlador.tomar_numero()  # 🔥 conexión MVC
    
    def imprimir_mensaje(self, mensaje):
        self.label_resultado.config(text=mensaje)