import math


def Nombre_Parfait() :
    nombre = int(input("Donner un nombre : "))
    somme = 0
    for i in range(1, math.floor(nombre/2) + 1) :
        reste = nombre % i
        if reste == 0 :
            somme += i
    if somme == nombre :
        print(nombre, " est parfait")
    else :
        print(nombre, " n'est pas parfait")


Nombre_Parfait()