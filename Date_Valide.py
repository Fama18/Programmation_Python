
def Date_Valide() :
    jour = int(input("Donner le jour : "))
    mois = int(input("Donner le mois : "))
    annee = int(input("Donner l'annee : "))
    max = 31
    temp = True
    if 1000 <= annee <= 2020 :
        if mois == 1 and mois == 3 and mois == 5 and mois == 7 and mois == 8 and mois == 10 and mois == 12 :
            max = 31
        elif mois == 4 and mois == 6 and mois == 9 and mois == 11 :
            max = 30
        elif mois == 2 :
            max = 28
        else :
            temp = False
        if temp == True and ((jour >= 1) and (jour <= max)) :
            print("Date valide")
        else :
            print("Date non valide")


Date_Valide()