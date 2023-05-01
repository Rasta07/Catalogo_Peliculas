import os


class CatalogoPeliculas:

    Ruta_Archivo = "peliculas.txt"


    @classmethod
    def Agregar_Peliculas(cls,pelicula):
        with open(cls.Ruta_Archivo,"a", encoding= "utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @classmethod
    def Listar_Peliculas(cls):
        with open(cls.Ruta_Archivo,"r", encoding= "utf8") as archivo:
            print(f"Catalogo de peliculas".center(50,"-"))
            print(archivo.read())

    @classmethod
    def Eliminar_Peliculas(cls):
        os.remove(cls.Ruta_Archivo)
        print(f"Archivo eliminado: {cls.Ruta_Archivo}")
