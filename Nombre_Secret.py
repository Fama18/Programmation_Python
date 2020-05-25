
def nombre_secret() :
    a = int(input("Donner le nombre secret : "))
    b = int(input("Donner le nombre déviné par le second utilisateur : "))
    i = 1
    while a != b :
        if b > a :
            print("Trop grand")
        else :
            print("Trop petit")
        i += 1
        b = int(input("Donner un autre nombre : "))
    print("vous avez trouvé le nombre aprés", i, " tentatives")


nombre_secret()