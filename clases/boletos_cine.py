
class BoletoCine(object):
    def __init__(self,nombre, funcion, precio_base=90):
        self.nombre = nombre
        self.funcion = funcion
        self.precio_base = precio_base

    def calcular_precio(self):
        return self.precio_base

    def descripcion(self):
        return f"{self.nombre}- ${self.funcion}: ${self.calcular_precio():,.2f}"

class BoletoEstudiante(BoletoCine):
    def __init__(self, nombre, funcion):
        super().__init__(nombre, funcion, precio_base=90)

    def calcular_precio(self):
        return self.precio_base * 0.7   

class BoletoTerceraEdad(BoletoCine):
    def __init__(self, nombre, funcion):
        super().__init__(nombre, funcion, precio_base=90)

    def calcular_precio(self):
        return self.precio_base * 0.5

class BoletoCortesia(BoletoCine):
    def __init__(self, nombre, funcion):
        super().__init__(nombre, funcion, precio_base=0)

    def descripcion(self):
        return f"{self.nombre}: ${self.calcular_precio():,.2f}"


    











 