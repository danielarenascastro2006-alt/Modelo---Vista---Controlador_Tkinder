from Numero import Numero
from Vista_formulario import Formulario

class Controlador:
    def __init__(self):
        self.obj_numero = Numero()
        self.obj_vista = Formulario()

        self.obj_vista.set_controlador(self)

    def iniciar(self):
        self.obj_vista.iniciar_ventana()
        self.obj_vista.formulario()
        self.obj_vista.inicios.mainloop()

    def tomar_numero(self):
        numero = Formulario.get_numero()
        self.obj_numero.set_numero(numero)
        self.imprimir_numero()

    def imprimir_numero(self):
        numero = self.obj_numero.get_numero()
        resultado = self.obj_numero.validar_numero(numero)
        self.obj_vista.imprimir_mensaje(resultado)