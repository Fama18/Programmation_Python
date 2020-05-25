
def pgdc() :
    a = int(input("Donner la valeur de a : "))
    b = int(input("Donner la valeur de b : "))
    while a != b :
        if a > b :
            a -= b
        else :
            b -= a
    pgcd = a
    print("le PGCD de (a , b) est : ", pgcd)


pgdc()