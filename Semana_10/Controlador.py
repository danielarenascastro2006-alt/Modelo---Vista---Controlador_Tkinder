from Numero import Numero
from Vista_formulario import Formulario

class Controlador:
    def __init__(self):
        self.obj_numero = Numero()
        self.obj_vista = Formulario()
        self.obj_vista.set_controlador(self)

    def iniciar(self):
        self.obj_vista.iniciar_ventana()
        self.obj_vista.formulario() # Esto crea los botones y entries
        self.obj_vista.inicios.mainloop() # Esto mantiene la ventana abierta

    def tomar_numero(self):
        # Ahora sí, el entry_usuario ya existe porque la ventana está abierta
        numero = self.obj_vista.pedir_numero()
        self.obj_numero.set_numero(numero)
        self.imprimir_numero()

    def imprimir_numero(self):
        # 1. Obtenemos el número almacenado en el modeloM
        num = self.obj_numero.get_numero()
        
        # 2. Llamamos a validar_numero pasando 'num' como argumento
        # Ahora no dará error porque el modelo ya tiene 'self' y acepta el parámetro
        resultado = self.obj_numero.validar_numero(num)
        
        # 3. Enviamos los resultados a la vista
        self.obj_vista.imprimir_mensaje(resultado)
        self.obj_vista.imprimir_numero(num)
