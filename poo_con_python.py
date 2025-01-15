class Personaje:
    #Atributos de la clase
    #nombre = 'Default'
    #fuerza = 0
    #inteligencia = 0
    #defensa = 0
    #vida = 0
    
    #Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza: ", self.__fuerza)
        print("-Inteligencia: ", self.__inteligencia)
        print("-Defensa: ", self.__defensa)
        print("-Vida: ", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        #self.__fuerza += fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
    
    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "Ha muerto we")
        #return self.__vida <=0
    
    def dañar(self, enemigo):
        if self.__fuerza - enemigo.__defensa < 0:
            return 0
        else:
            return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "Chris dispara y causa ", daño, "puntos de daño a", enemigo.__nombre)
        print("Vida de ", enemigo.__nombre, "es ", enemigo.__vida)
    
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, valor negativo")
        else:
            self.__fuerza = fuerza

#Variable del constructo vacío de la clase
mi_personaje = Personaje("Chris", 80, 3, 70, 100)
# mi_personaje.imprimir_atributos()
mi_enemigo = Personaje("Wesker",75,30,70,100)
mi_personaje._Personaje__fuerza = -5
mi_personaje.imprimir_atributos()
# mi_personaje.__fuerza
# mi_personaje.fuerza = 0
# mi_personaje.imprimir_atributos()
# mi_personaje.morir()
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.imprimir_atributos()
#print(mi_personaje.dañar(mi_enemigo))
# mi_personaje.__nombre = "ChemaFighter"
# mi_personaje.__fuerza = 9000
# mi_personaje.__inteligencia = 300
# mi_personaje.__defensa = 100
# mi_personaje.__vida = 3
#print("El nombre del personaje es ", mi_personaje.__nombre)
#print("La fuerza de mi personaje es ", mi_personaje.__fuerza)
#print("El IQ de mi personaje es ", mi_personaje.__inteligencia)
#print("El numero de vidas de mi personaje es ", mi_personaje.__vida)
