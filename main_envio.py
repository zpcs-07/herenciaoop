from clases.paqueteria import Envio, EnvioExpress, EnvioSobre

def main():
    envio = Envio("Hugo", 10 )
    envioSobre = EnvioSobre("Paco")
    envioExpress = EnvioExpress("Luis", 20)

    print(envio.resumen())
    print(envioSobre.resumen())
    print(envioExpress.resumen())


if __name__ == '__main__':
    main()
