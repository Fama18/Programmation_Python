def operation():
    a = int(input("Donner la valeur de a : "))
    op = str(input("Donner l'operateur : "))
    b = int(input("Donner la valeur de b : "))
    if op == '+':
        print("l'addition de a par b est ", str(a + b))
    elif op == '-':
        print("la soustraction de a par b est ", str(a - b))
    elif op == '*':
        print("la multiplication de a par b est ", str(a * b))
    elif op == '/':
        if b == 0 :
            print("Division impossible")
        else :
            print("la division de a par b est ", str(a / b))


operation()
