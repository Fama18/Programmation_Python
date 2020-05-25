import math


def main() :
        x = float(input("Donner la valeur de x : "))
        n = int(input("Donner la valeur de n : "))
        puissance_x = math.pow(x,n)
        print("x puissance n egal : ", str(puissance_x))


if __name__ == '__main__':
    main()