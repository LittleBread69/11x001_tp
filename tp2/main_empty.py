import random

from utils import exercice

#
# EXERCICE 1
#

@exercice
def _exercice1():
    # ******************** Votre code ci-dessous ********************
    age = int(input("Quel est votre age? "))
    reponse_fumeur = input("Est-ce que vous êtes fumeurs (o, n)").capitalize()
    fumeur = True if reponse_fumeur == "O" else None if\
    reponse_fumeur != "N" else False

    while age <= 0:
        print(f"Votre age: {age} n'est pas valide.")
        age = int(input("Quel est votre age? "))
    while fumeur not in (True, False):
        print(f"La réponse n'est pas valide comme réponse.")
        reponse_fumeur = input("Est-ce que vous êtes fumeurs (o, n)").capitalize()
        fumeur = True if reponse_fumeur == "O" else None if reponse_fumeur != "N" else False
    if age < 30:
        print("Peu de Risque")
        return
    #else
    if fumeur:
        print("Grand Risque")
        return
    #else:
    print("Peu de Risque")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    age = int(input("Quel est votre age? "))
    reponse_fumeur = input("Est-ce que vous êtes fumeurs (o, n)? ").capitalize()
    fumeur = True if reponse_fumeur == "O" else None if\
    reponse_fumeur != "N" else False

    while age <= 0:
        print(f"Votre age: {age} n'est pas valide.")
        age = int(input("Quel est votre age? "))
    while fumeur not in (True, False):
        print(f"La réponse n'est pas valide comme réponse.")
        reponse_fumeur = input("Est-ce que vous êtes fumeurs (o, n)? ").capitalize()
        fumeur = True if reponse_fumeur == "O" else None if reponse_fumeur != "N" else False

    if age >= 30 and fumeur:
        print("Grand Risque")
        return
    print("Peu de Risque")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    # ******************** Votre code ci-dessous ********************
    ...
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    # ******************** Votre code ci-dessous ********************
    ...
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    dix_a_vingt = range(10, 21, 2)
    resultats = []
    for i in dix_a_vingt:
        resultats.append(i*i)
    print(resultats)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    resultats = [x*x for x in range(10, 21, 2)]
    print(resultats)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    a = list(range(0, 10))
    b = a
    for ind, val in enumerate(a):
        a[ind] = val * val

    print(a, "\n", b)
    #b est une référence à a, pas une nouvelle liste

    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    # ******************** Votre code ci-dessous ********************
    liste_de_mots = "The quick brown fox jumps over the lazy dog <END>".split()
    input_sequence = liste_de_mots[:4]
    target_sequence = liste_de_mots[4:]
    print(input_sequence, target_sequence)

    # ******************** Votre code ci-dessus *********************

def somme_liste(liste:list[int]) -> int:
    if len(liste) == 1:
        return liste[0]
    return liste[0] + somme_liste(liste[1:])
    # il s'agit de récursion, la fonction appèle à s'éxécuter elle-même.

@exercice
def exercice8():
    # ******************** Votre code ci-dessous ********************
    print(somme_liste([1, 2, 3, 4]))
    # ******************** Votre code ci-dessus *********************

if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    exercice1()
    #exercice2()
    #exercice3()
    exercice4()
    exercice5()
    exercice6()
    exercice7()
    exercice8()
