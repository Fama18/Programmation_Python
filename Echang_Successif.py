
def main() :
    A = int(input("Donner la valeur de A : "))
    B = int(input("Donner la valeur de B : "))
    C = int(input("Donner la valeur de C : "))
    if A > B :
        nombre = A
        A = B
        B = nombre
    if A > C :
        nombre = A
        A = C
        C = nombre
    if B > C :
        nombre = B
        B = C
        C = nombre
    print(" A : ", A, " B : ", B, " C : ", C)


if __name__ == '__main__':
    main()