
def main() :
        R1 = float(input("Donner la valeur de R1 : "))
        R2 = float(input("Donner la valeur de R2 : "))
        R3 = float(input("Donner la valeur de R3 : "))
        choix = int(input("Donner le numero de votre choix (1 ou 2) : "))
        if choix == 1 :
            R = R1 + R2 + R3
            print("la resistance est en serie, sa valeur est : ", str(R))
        elif choix == 2 :
            R = (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R1 * R3)
            print("la resistance est en parallele, sa valeur est : ", str(R))
        else:
            print("Veuillez saisir 1 ou 2 pour pouvoir calculer la resistance ")


if __name__ == '__main__':
        main()