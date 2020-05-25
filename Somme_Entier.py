
def Somme_Entier() :
    somme = 0
    nombre = int(input("Donner un nombre : "))
    for i in range(1,nombre + 1) :
        somme += i
    print("la somme des entiers de 1 à ", nombre, " est : ", somme)
    moyenne = somme / nombre
    print("la moyenne des entiers de 1 à ", nombre, " est : ", moyenne)


Somme_Entier()
