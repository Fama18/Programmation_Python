
def Plus_Grand() :
    nbr = 10
    val = int(input("Entrer le premier nombre : "))
    indice_plus_grand = 1
    max = val
    for indice in range(2, nbr + 1):
        val = int(input("Entrer le nombre numero suivant : "))
        if val > max :
            indice_plus_grand = indice
            max = val
    print("le plus grand de ces nombres est:", max)
    print(" c'est le nombre numero :", indice_plus_grand)


Plus_Grand()