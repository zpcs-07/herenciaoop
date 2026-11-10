

from clases.boletos_cine import BoletoCine, BoletoCortesia, BoletoEstudiante, BoletoTerceraEdad 

def main():
   Boleto1 = BoletoCine("Andrea", "Sala 2, 18:00")
   Boleto2 = BoletoEstudiante("Bruno", "Sala 2, 18:00")
   Boleto3 = BoletoCortesia("Carla", "Sala 5, 20:30")
   Boleto4 = BoletoTerceraEdad("Diana", "Sala 1, 16:00")

   print(Boleto1.descripcion())
   print(Boleto2.descripcion())
   print(Boleto3.descripcion())
   print(Boleto4.descripcion())

if __name__ == '__main__':
    main()

