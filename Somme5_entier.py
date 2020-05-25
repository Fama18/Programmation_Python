
def main() :
    somme = 0
    for i in range(1,6):
        nombre = int(input("Donner un nombre : "))
        somme += nombre
    print("la somme des 5 nombres est : ", str(somme))


if __name__ == '__main__':
    main()