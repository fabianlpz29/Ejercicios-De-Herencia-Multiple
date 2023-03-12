from Peliculas import Peliculas
from Peliculas import tipoPelicula

class Cliente(Peliculas):
    pass

    def Eleccion():
        ciclo = True
        while (ciclo):
            print("-------------------------------------------------------------------------------------------------------------")
            print("1-Listar las peliculas de accion \n 2-Listar las peliculas de comedia \n 2-Listar las peliculas de comedia \n 4- Salir")
            print("\n")
            eleccion = int(input("Ingrese la categoria de peliculas que desea ver (!!! INGRESAR EL NUMERO !!!):"))
            print("-------------------------------------------------------------------------------------------------------------")

            if eleccion == 1:
                print(tipoPelicula.CategoriaAccion())

            elif eleccion == 2:
                print(tipoPelicula.CategoriaComedia())

            elif eleccion == 3:
                print(tipoPelicula.CategoriaTerror())

            elif eleccion == 4:
                ciclo = False
                print("El programa finalizo")

            else:
                print("!! Ingrese una caracter valido !!!")

elejir =  Cliente

elejir.Eleccion()
