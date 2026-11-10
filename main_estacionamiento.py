


from clases.estacionamiento import Estancia, EstanciaPension, EstanciaNocturna

def main():
    estancia1 = Estancia("ABC-123", 3)
    estancia2 = EstanciaPension("XYZ-789")
    estancia3 = EstanciaNocturna("JKL-456", 5)


    print(estancia1.generar_ticket())
    print(estancia2.generar_ticket())
    print(estancia3.generar_ticket())


if __name__ == '__main__':
    main()
