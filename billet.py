import math


def main() :
    montant = int(input("donner un montant : "))
    billet_20 = math.floor(montant/20)
    reste = montant % 20

    billet_10 = math.floor(reste /10)
    reste = reste % 10

    billet_5 = math.floor(reste / 5)
    reste = reste % 5

    piece_2 = math.floor(reste / 2)
    reste = reste % 2

    piece_1 = reste
    print("le montant ", str(montant), "decomposé donne : ")
    print(str(billet_20), "billets de 20")
    print(str(billet_10), "billets de 10")
    print(str(billet_5), "billets de 5")
    print(str(piece_2), "pieces de 2")
    print(str(piece_1), "pieces de 1")


if __name__ == '__main__':
    main()