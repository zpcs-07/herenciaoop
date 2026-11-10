

class Estancia(object):
    def __init__(self, placa, horas):
        self.placa = placa
        self.horas = horas

    def calcular_cobro(self):
        return self.horas * 20

    def generar_ticket(self):
        return f"{self.placa} ({self.horas} h): ${self.calcular_cobro()}"

class EstanciaPension(Estancia):
    def __init__(self, placa):
        super().__init__(placa, horas=24)

    def calcular_cobro(self):
        return 250

class EstanciaNocturna(Estancia):
    def __init__(self, placa, horas):
        super().__init__(placa, horas)

    def calcular_cobro(self):
        return super().calcular_cobro() + 50