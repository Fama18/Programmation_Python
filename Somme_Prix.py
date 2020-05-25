
def Somme_Prix() :
    prix = int(input("Entrer le prix du premier nombre : "))
    somme = 0
    while prix != 0 :
        somme += prix
        prix = int(input("Entrer le prix du premier nombre (0 si Fin) : "))
    print("la somme des prix des articles " , somme)


Somme_Prix()