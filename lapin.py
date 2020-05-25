
def nb_lapin() :
    f_0 = 2
    f_1 = 2
    for i in range(1, 13) :
        f = f_0 + f_1
        f_0 = f_1
        f_1 = f
    print("Au bout de 12 mois on aura ", f, " lapins")


def nb_mois() :
    f_0 = 2
    f_1 = 2
    f = 0
    i = 0
    while f != 1000000000 :
        f = f_0 + f_1
        f_0 = f_1
        f_1 = f
        i += 1
    print("on aura 1000000000 de lapins au ", i, " eme mois")


nb_lapin()
nb_mois()