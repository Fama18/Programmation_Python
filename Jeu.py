
def jeu () :
    a = int(input("Entrer la valeur saisi par le premier utilisateur : "))
    b = int(input("Entrer le nombre déviné par le second utilisateur : "))
    i = 1
    while a != b :
        if b > a:
            print("plus grand que le nombre recherché")
        else :
            print("plus petit que le nombre recherché")
        i += 1
        b = int(input("Essayer un autre nombre : "))
    print("vous avez trouvé le nombre aprés", i, " tentatives")


jeu()