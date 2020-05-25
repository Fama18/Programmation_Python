def tab_croissant_decroissant():
    croissant = True
    decroissant = True
    t = []
    nbr = int(input("Donner le nombre d'elements de la liste : "))
    for i in range(0, nbr):
        print("Donner le nombre numero ", i + 1)
        t.append(eval(input()))
    print(t)
    PremierElement = t[0]
    for j in t:
        if PremierElement > j:
            croissant = False
            PremierElement = j
        elif PremierElement < j:
            decroissant = False
            PremierElement = j
    if croissant and not decroissant:
        print("le tableau est croissant")
    elif not croissant and decroissant:
        print("le tableau est decroissant")
    else:
        print("le tableau est quelconque")


tab_croissant_decroissant()
