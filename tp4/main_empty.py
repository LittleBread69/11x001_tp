import random

from utils import exercice

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

@exercice
def exercice2():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice8():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    exercice1()
    #exercice2()
    #exercice3()
    #exercice4()
    #exercice5()
    #exercice6()
    #exercice7()
    #exercice8()
