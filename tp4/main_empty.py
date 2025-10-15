import random

from utils import exercice

def somme_liste(liste:list[int]) -> int:
    if len(liste) == 1:
        return liste[0]
    return liste[0] + somme_liste(liste[1:])
    # il s'agit de récursion, la fonction appèle à s'éxécuter elle-même.

#
# EXERCICE 1
#
def recherche_Dichotomique(nombre: int, ma_liste: list[int]) -> int:
    """Retourne l'index du nombre dans la liste. Si le nombre n'est pas dans la liste, retourne -1."""
    if len(ma_liste) <= 0:
        return -1
    
    debut: int = 0
    fin: int = len(ma_liste) - 1

    while debut <= fin:
        milieu = (fin + debut) // 2
        valeur_milieu = ma_liste[milieu]
        if valeur_milieu == nombre:
            return milieu
        elif valeur_milieu < nombre:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    random.seed(42)
    ma_liste = sorted([random.randrange(0, 100, 1) for _ in range(20)])
    print(f"L'entier 1 se trouve à l'indice {recherche_Dichotomique(1, ma_liste)} de \"ma_liste\".")
    print(f"L'entier 11 se trouve à l'indice {recherche_Dichotomique(11, ma_liste)} de \"ma_liste\".")
    print(f"L'entier 84 se trouve à l'indice {recherche_Dichotomique(84, ma_liste)} de \"ma_liste\".")
    print(f"L'entier 299 se trouve à l'indice {recherche_Dichotomique(299, ma_liste)} de \"ma_liste\".")
    print(f"L'entier 3 se trouve à l'indice {recherche_Dichotomique(3, ma_liste)} de \"ma_liste\".")
    # ******************** Votre code ci-dessus *********************

def somme(x: int | float, y: int | float) -> int | float:
    return x + y

def mafct(x: int | float, y: int | float) -> int | float:
    return somme(x + y) * somme(x + y)

#@exercice
#def exercice2():
#    # ******************** Votre code ci-dessous ********************
#    pass
#    # ******************** Votre code ci-dessus *********************
#
#@exercice
#def exercice3():
#    # ******************** Votre code ci-dessous ********************
#    pass
#    # ******************** Votre code ci-dessus *********************

def moyenne_liste(liste: list[float | int]):
    return somme_liste(liste) / len(liste)

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    print(moyenne_liste([1, 1, 1, 2, 2, 2]))
    # ******************** Votre code ci-dessus *********************

def dot_product(liste1: list[int | float], liste2: list[int | float]) -> int | float:
    assert len(liste1) == len(liste2), "Les listes doivent être de même taille"
    produits = [liste1[i] * liste2[i] for i in range(len(liste1))]
    return somme_liste(produits)

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    print(dot_product([6, 2, 3], [1, 2, 3]))
    # ******************** Votre code ci-dessus *********************

def moyenne_ponderee_liste(liste_valeur: list, liste_poids: list) -> float:
    assert len(liste_valeur) == len(liste_poids), "Les listes doivent être de même taille"
    return dot_product(liste_valeur, liste_poids) / somme_liste(liste_poids)


@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    print(moyenne_ponderee_liste([10, 20, 30], [1, 2, 3]))
    # ******************** Votre code ci-dessus *********************

def somme_complexe(z1, z2):
    assert len(z1) == len(z2) == 2
    a = z1[0] + z2[0]
    b = z1[1] + z2[1]
    print(f"({a} + {b}i)")
    return [a, b]


def conjugue(z1):
    assert len(z1) == 2
    a = z1[0]
    b = -z1[1]
    print(f"({a} + {b}i)")
    return [a, b]

from math import sqrt

def module(z1):
    assert len(z1) == 2
    a, b = z1
    mod = sqrt(a**2 + b**2)
    print(f"|z| = {mod}")
    return mod

from math import atan

def argument(z1):
    assert len(z1) == 2
    a, b = z1
    arg = atan(b / a)
    print(f"arg(z) = {arg} radians")
    return arg

@exercice
def exercice7():
    # ******************** Votre code ci-dessous ********************
    z1 = [1, 3]
    z2 = [4, -5]

    print("Somme : ", end="")
    somme_complexe(z1, z2)

    print("Conjugué de z1 : ", end="")
    conjugue(z1)

    print("Module de z1 : ", end="")
    module(z1)

    print("Argument de z1 : ", end="")
    argument(z1)
    # ******************** Votre code ci-dessus *********************

def matrice_vecteur(A, x):
    return [dot_product(ligne, x) for ligne in A]

@exercice
def exercice8():
    # ******************** Votre code ci-dessous ********************
    A = [[1, 0],
    [0, -1]]

    x = [1, 0]

    print(matrice_vecteur(A, x))

    A = [[2, 3, 4],
    [0, 1, -1]]

    x = [1, 2, 3]

    print(matrice_vecteur(A, x))
    # ******************** Votre code ci-dessus *********************

if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    #exercice1()
    ##exercice2()
    ##exercice3()
    #exercice4()
    #exercice5()
    #exercice6()
    #exercice7()
    #exercice8()
    ...
