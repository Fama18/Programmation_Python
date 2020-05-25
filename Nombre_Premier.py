
def nombre_premier() :
    a = int(input("Donner un nombre : "))
    b = 0
    for i in range(2, a + 1) :
        if a % i == 0 :
            b += 1
    if b == 1 :
        print(a , " est un nombre premier ")
    else :
        print(a, " n'est pas un nombre premier ")


nombre_premier()