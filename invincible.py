class Invincible:
    def __init__(self, nombre, edad, planeta, velocidad, fuerza):
        self.__nombre = nombre
        self.__edad = edad
        self.__planeta = planeta
        self.__velocidad = velocidad
        self.__fuerza = fuerza

    ##Getters 
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_planeta(self):
        return self.__planeta

    def get_velocidad(self):
        return self.__velocidad

    def get_fuerza(self):
        return self.__fuerza

    ##Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre  

    def set_edad(self, edad):
        self.__edad = edad
    
    def set_planeta(self, planeta):
        self.__planeta = planeta

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad    

    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza