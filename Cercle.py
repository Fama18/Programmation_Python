import math


def main() :

        PI = 4 * math.atan(1)
        rayon = float(input("Donner le rayon : "))
        surface = PI * rayon * rayon
        perimetre = 2 * PI * rayon
        print("la surface du cercle est : ", str(surface))
        print("le perimetre est : ", str(perimetre))


if __name__ == '__main__':
    main()