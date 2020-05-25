
def long_sequence():
    t = []
    nbr = int(input("Donner le nombre d'elements de la liste : "))
    for i in range(0, nbr):
        print("Donner le nombre numero ", i + 1)
        t.append(eval(input()))
    print(t)
    j = 0
    PremierElement = t[0]
    for i in t:
        if i > PremierElement :
            indice_seq_courant = i
            while i < nbr and i > PremierElement :
                i += 1
                j += 1
        indice_seq_long = indice_seq_courant
        longueur_seq = j
    print("La plus longue sequence est ", t[indice_seq_long]," à ",t[longueur_seq], " qui debute à la position ",
           indice_seq_long, " et sa longueur est ", longueur_seq)


long_sequence()