
def main() :
        R1 = float(input("Donner la valeur de R1 : "))
        R2 = float(input("Donner la valeur de R2 : "))
        R3 = float(input("Donner la valeur de R3 : "))
        Rserie = R1 + R2 + R3
        Rparallele = (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R1 * R3)
        print("la resistance en serie est : ", str(Rserie))
        print("la resistance en parallele est : ", str(Rparallele))


if __name__ == '__main__':
    main()