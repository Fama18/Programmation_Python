
def main() :
      x = float(input("Donner la valeur de x : "))
      n = int(input("Donner la valeur de n : "))
      puissance_x = 1
      for i in range(1,n+1):
          puissance_x *= x
      print("x puissance n egal : ", str(puissance_x))


if __name__ == '__main__':
    main()