import math


def main():
    x1 = float(input("Donner l'abscisse de A : "))
    y1 = float(input("Donner l'ordonne de A : "))
    x2 = float(input("Donner l'abscisse de B : "))
    y2 = float(input("Donner l'ordonne de A : "))
    distance = math.sqrt((x1-x2)*2 + (y1-y2)*2)
    print("La distance entre le point A et le point B est : ", (distance))


if __name__ == '__main__':
    main()