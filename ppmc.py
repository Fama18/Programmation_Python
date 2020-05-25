
def ppmc() :
    a = int(input("Donner la valeur de a : "))
    b = int(input("Donner la valeur de b : "))
    while a != b :
        if a < b :
            a += a
        else :
            b += b
    ppcm = a
    print("le PPCM de (a , b) est : ", ppcm)


ppmc()