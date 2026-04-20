class Invincible:
    def __init__(self, nombre, edad, superpoderes, velocidad, fuerza):
        self.__nombre = nombre
        self.__edad = edad
        self.__superpoderes = superpoderes
        self.__velocidad = velocidad
        self.__fuerza = fuerza

    ##Getters 
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_superpoderes(self):
        return self.__superpoderes

    def get_velocidad(self):
        return self.__velocidad

    def get_fuerza(self):
        return self.__fuerza
