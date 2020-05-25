
def Soustrac_Successif() :
    a = int(input("Donner la valeur du dividende : "))
    b = int(input("Donner la valeur du diviseur : "))
    quotient = 0
    while a >= b :
        a -= b
        quotient += 1
    print("la division de a par b donne : ", quotient)


Soustrac_Successif()