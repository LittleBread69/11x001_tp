import random

from utils import exercice, generer_resultats

#
# EXERCICE 1
#
from functools import lru_cache
from pprint import pprint

lru_cache(2048)
def fibonacci(n: int) -> int:
    if n <= 0: return 0
    elif n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    print(fibonacci(20))
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    nombres = list(range(10))
    # ******************** Votre code ci-dessous ********************
    carres = [nb * nb for nb in nombres]
    for pairs_de_nombres in zip(nombres, carres):
        print(f"{pairs_de_nombres[0]}, {pairs_de_nombres[1]}")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    resultats = generer_resultats(False)
    # ******************** Votre code ci-dessous ********************
    eleves = {}
    for cours in resultats:
        for eleve, note in cours.items():
            if eleve not in eleves.keys():
                eleves[eleve] = [note]
            else:
                eleves[eleve].append(note)
    for resultat in eleves.items():
        print(f"{resultat[0]} : {len(resultat[1])} note{'s' if {len(resultat[1]) > 1} else ''} - {(sum(resultat[1])/len(resultat[1])):.2f} de moyenne.")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    user_text = "Ce procédé est parfois appelé slugify car on convertit notre texte en son équivalent limace" #texte fixe à la place d'un `input()`
    limace_text = "-".join(user_text.lower().split())
    print(limace_text)
    # ******************** Votre code ci-dessus *********************

def hamming(str1, str2) -> int:
    # ******************** Votre code ci-dessous ********************
    if len(str1) != len(str2):
        return -1
    difference = 0
    for lettres in zip(str1, str2):
        if lettres[0] != lettres[1]:
            difference += 1
    return difference 
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    str1 = input("str1 = ")
    str2 = input("str2 = ")
    print(f"\nHamming({str1}, {str2}) = {hamming(str1, str2)}.")
    # ******************** Votre code ci-dessus *********************

from autres import fact

def coefficient_binomial(n: int, k: int) -> int:
    return fact(n) // (fact(k) * fact(n - k))

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    entier1 = random.randint(1, 20)
    entier2 = random.randint(1, 20)
    entier1, entier2 = (entier1, entier2) if entier1 >= entier2 else (entier2, entier1)

    print(coefficient_binomial(entier1, entier2))
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    # ******************** Votre code ci-dessous ********************
    try:
        a = (1, 2, 3)
        a[0] = 42
        print(a)
    except Exception as e:
        print(f"Erreur: {e}")
    
    try:   
        a = ([1, 2], 2, 3)
        b = a
        b[0][0] = 42
        print(a)
        print(b)
    except Exception as e:
        print(f"Erreur: {e}")
    
    try:
        import random

        def createurDeTuples():
            x = random.randint(0, 10)
            y = random.randint(0, 10) 
            return x, y

        ma_liste = [createurDeTuples() for _ in range(10)]
        print(ma_liste)
    except Exception as e:
        print(f"Erreur: {e}")
    # ******************** Votre code ci-dessus *********************

def afficher_instruction_hanoi(nom_tour_1, nom_tour_2):
    input(f"Prendre le disque sur la tour {nom_tour_1} et le déposer sur "\
          f"la tour {nom_tour_2} (appuyer sur n'importe quelle touche pour continuer)\n")

def hanoi_idiot(nb_disques, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire):

    match nb_disques:
        case 1:
            afficher_instruction_hanoi(nom_tour_depart, nom_tour_arrivee)
        case 2:
            afficher_instruction_hanoi(nom_tour_depart, nom_tour_auxiliaire)
            afficher_instruction_hanoi(nom_tour_depart, nom_tour_arrivee)
            afficher_instruction_hanoi(nom_tour_auxiliaire, nom_tour_arrivee)
        case _:
            print("Je ne sais pas comment faire avec %d disques.\n", nb_disques)

    return

def hanoi(nb_disques, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire):

    if (nb_disques < 1):
        print("Le nombre de disques ne peut pas être inférieur à 1.\n")
        return

    # TODO : commenter (ou supprimer) la ligne suivante
    hanoi_idiot(nb_disques, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire)
    
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice8():
    print("\n*** Tours de Hanoi ***\n\n");
    print("Par ici pour jouer : https://www.mathsisfun.com/games/towerofhanoi.html\n\n");

    nb_disques = int(input("Avec combien de disques voulez-vous jouer ? "));

    hanoi(nb_disques, '1', '3', '2');

if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    #exercice1()
    #exercice2()
    #exercice3()
    #exercice4()
    #exercice5()
    #exercice6()
    ##exercice7()
    #exercice8()
    ...