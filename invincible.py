class Invincible:
    def __init__(self, nombre, edad, planeta, velocidad, fuerza):
        self.__nombre = nombre
        self.__edad = edad
        self.__planeta = planeta
        self.__velocidad = velocidad
        self.__fuerza = fuerza
        self.__nivel_vida = 120

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
    
    def get_nivel_vida(self):
        return self.__nivel_vida

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

    def set_nivel_vida(self, nivel):
        if nivel >= 0:
            self.__nivel_vida = nivel

    def info(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, Planeta: {self.__planeta}, Velocidad: {self.__velocidad}, Fuerza: {self.__fuerza}")

    def usar_poder(self):
          if self.__nivel_vida < 10:
            print("No se puede usar el poder, nivel de vida mínimo")
          else:
            self.__nivel_vida -= 1
            print(f"{self.__nombre} está usando su poder, nivel de vida actual: {self.__nivel_vida}")

    def recuperar_vida(self, cantidad):
        self.__nivel_vida += cantidad
        if self.__nivel_vida > 120:
            self.__nivel_vida = 120
        print(f"{self.__nombre} recuperó vida. Vida actual: {self.__nivel_vida}")
    
    #Personaje 
invencible1 = Invincible("Mark", 18, "Tierra", 100, 100)
invencible2 = Invincible("Nolan", 400, "Viltrum", 300, 500)

# Ver info
invencible1.info()
invencible2.info()