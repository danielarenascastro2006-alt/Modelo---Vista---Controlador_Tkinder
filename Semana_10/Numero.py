class Numero:
    def __init__(self, dato_numero=0):
        self.dato_numero = dato_numero
        
    def set_numero(self, nuevo_numero):
        self.dato_numero = nuevo_numero

    def get_numero(self):
        return self.dato_numero
    
    # IMPORTANTE: Agregar 'self' y 'dato_numero' como pide el UML
    def validar_numero(self, dato_numero):
        # Lógica de paridad
        paridad = "par" if dato_numero % 2 == 0 else "impar"
        
        # Lógica de tipo (positivo/negativo/neutro)
        if dato_numero > 0:
            tipo = "positivo"
        elif dato_numero < 0:
            tipo = "negativo"
        else:
            tipo = "neutro"
            
        return f"Es {paridad} y {tipo}"
    
        
        #imprime validación
        resultado = self.obj_numero.validar_numero(numero)
        self.obj_vista.imprimir_mensaje(resultado)
