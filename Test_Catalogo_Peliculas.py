from Dominio.Pelicula import Pelicula
from Servicio.Catalogo_Peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print("Opciones: ")
        print("1. Agregar Pelicula ")
        print("2. Listar las peliculas ")
        print("3. Eliminar catalogo de peliculas ")
        print("4. Salir")
        opcion = int(input("Digite una opción de menú (1-4): "))
        if opcion == 1:
            Nombre_Pelicula = input("Digite el nombre de la pelicula: ")
            pelicula = Pelicula(Nombre_Pelicula)
            cp.Agregar_Peliculas(pelicula)
        elif opcion == 2:
            cp.Listar_Peliculas()
        elif opcion == 3:
            cp.Eliminar_Peliculas()
    except Exception as e:
        print(f"Ocurrio un error de tipo:{e}")
        opcion = None
    else:
        print("Salimos del programa")
