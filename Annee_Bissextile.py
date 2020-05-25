

def Annee_bissextile() :
    jour = int(input("Donner le jour : "))
    mois = int(input("Donner le mois : "))
    annee = int(input("Donner l'annee : "))
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 ==0) :
        print("l'annee est bissextile")
    else :
        print("l'annee n'est pas bissextile")


Annee_bissextile()