class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    #Indicar quie no se haga nada en este momento
    pass
#Variable del constructo vacío de la clase
mi_personaje = Personaje()
mi_personaje.nombre = "ChemaFighter"
mi_personaje.fuerza = 9000
mi_personaje.inteligencia = 300
mi_personaje.defensa = 100
mi_personaje.vida = 3
print("El nombre del personaje es ", mi_personaje.nombre)
print("La fuerza de mi personaje es ", mi_personaje.fuerza)
print("El IQ de mi personaje es ", mi_personaje.inteligencia)
print("La defensa de mi personaje es ", mi_personaje.defensa)
print("El numero de vidas de mi personaje es ", mi_personaje.vida)