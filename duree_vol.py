
def main() :
    h_depart = int(input("Donner l'heure de depart : "))
    min_depart = int(input("Donner les minutes de depart : "))
    h_arrive = int(input("Donner l'heure d'arrivee : "))
    min_arrive = int(input("Donner les minutes d'arrivee : "))
    if h_arrive > h_depart :
        if min_arrive > min_depart :
            h_duree = h_arrive - h_depart
            min_duree = min_arrive - min_depart
            print("la duree du vol est : ", h_duree, " : ", min_duree)
        else:
            h_duree = h_arrive - h_depart - 1
            min_duree = min_arrive + 60 - min_depart
            print("la duree du vol est : ", h_duree, " : ", min_duree)
    else :
        if min_arrive > min_depart :
            h_duree = h_arrive - h_depart + 24
            min_duree = min_arrive - min_depart
            print("la duree du vol est : ", h_duree, " : ", min_duree)
        else :
            h_duree = h_arrive - h_depart + 24 - 1
            min_duree = min_arrive + 60 - min_depart
            print("la duree du vol est : ", h_duree, " : ", min_duree)


if __name__ == '__main__':
   main()