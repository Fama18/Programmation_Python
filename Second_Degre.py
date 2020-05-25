import math


def main() :
      a = float(input("Donner la valeur de a : "))
      b = float(input("Donner la valeur de b : "))
      c = float(input("Donner la valeur de c : "))
      if a == 0 :
          print("l'equation est du premier degre")
          if b != 0:
              print("la solution est : ", str(-c/b))
          else:
              print("Pas de solution")
      else:
          delta = (b * b) - (4 * a * c)
          if delta > 0:
              x1 = (- b - math.sqrt(delta))/(2*a)
              x2 = (- b + math.sqrt(delta)) / (2 * a)
              print("les solutions de l'equation sont : ", str(x1) , str(x2))
          else:
              if delta ==0:
                  print(" la solution est : ", str(-b / (2 * a)))
              else :
                  print("Pas de solution")


if __name__ == '__main__':
    main()