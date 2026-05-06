
class Numero:
    def __init__(self, dato_numero):
        self.numero= dato_numero
        
    def set_numero(self, nuevo_numero):
        self.dato_numero = nuevo_numero

    def get_numero(self):
        return self.dato_numero
    
    def validar_paridad(self):
        if self.dato_numero % 2 == 0:
            return "Es par"
        else:
            return "Es impar"

    def validar_tipo(self):
        if self.dato_numero > 0:
            return "Es positivo"
        elif self.dato_numero < 0:
            return "Es negativo"
        else:
            return "Es neutro (cero)"
    
    def imprimir_numero(self):
        numero = self.obj_numero.get_numero()
        
        #imprime el número (faltaba esto)
        self.obj_vista.imprimir_numero(numero)
        
        #imprime validación
        resultado = self.obj_numero.validar_numero(numero)
        self.obj_vista.imprimir_mensaje(resultado)