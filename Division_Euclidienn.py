import math


def main() :

     a = int(input("Entrer la valeur de a : "))
     b = int(input("Entrer la valeur de b : "))
     if b != 0 :
        quotient = math.floor(a/b)
        reste = (a%b)
        ratio = a/b
        print("le quotient de a par b est : ", str(quotient))
        print("le quotient reel de a par b est : ", str(ratio))
        print("le reste de la division de a par b est : ", str(reste))
     else:
        print("division impossible")


if __name__ == '__main__':
    main()

