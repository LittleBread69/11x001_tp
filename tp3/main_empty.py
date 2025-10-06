import random

from utils import exercice

#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    number = int(input("Entrez un nombre: "))
    print(f"{number} est {'positif' if number>0 else 'nul' if number==0 else 'négatif'}.")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    ma_liste = [4, 3, 7, 10, 42, 1]
    ind = 0
    biggest_number = -float('inf')
    # ******************** Votre code ci-dessous ********************
    while ind < len(ma_liste):
        biggest_number = ma_liste[ind] if ma_liste[ind] > biggest_number else biggest_number
        ind += 1
    print(f"{biggest_number} est le nombre le plus grand (selon while)")
    biggest_number = -float('inf')
    for _, element in enumerate(ma_liste):
        biggest_number = element if element > biggest_number else biggest_number
    print(f"{biggest_number} est le nombre le plus grand (selon for enumerate)")

    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    ma_liste = [4, 3, 7, 10, 42, 1]
    # ******************** Votre code ci-dessous ********************
    ind = 0
    smallest_number = float('inf')
    # ******************** Votre code ci-dessous ********************
    while ind < len(ma_liste):
        smallest_number = ma_liste[ind] if ma_liste[ind] < smallest_number else smallest_number
        ind += 1
    print(f"{smallest_number} est le nombre le plus petit (selon while)")
    smallest_number = float('inf')
    for _, element in enumerate(ma_liste):
        smallest_number = element if element < smallest_number else smallest_number
    print(f"{smallest_number} est le nombre le plus petit (selon for enumerate)")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    hauteur = int(input("Hauteur du carré: "))
    for i in range(hauteur):
        print(" "*(hauteur-i), "*"*(i*2+1))
    for i in range(hauteur-2, -1, -1):
        print(" "*(hauteur-i), "*"*(i*2+1))

    # ******************** Votre code ci-dessus *********************

def fibo_iteratif(n:int):   # fonction à un seul argument
    # TODO n° 2 de l'ex 5:
    # ******************** Votre code ci-dessous ********************
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    F_n = int(input("Entier à calculer (Fib): "))
    print(f"{fibo_iteratif} returns {fibo_iteratif(F_n)}")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    liste_1 = ["Alice", "Bob"]
    liste_2 = ["Charlie", "Eve"]
    ma_liste = liste_1+liste_2
    print(f"Ma liste utilisant '+=': {ma_liste}")
    print("\n")

    ma_liste = liste_1
    for element in liste_2:
        ma_liste.append(element)
    print(f"Ma liste utilisant '.append' {ma_liste}")
    # ******************** Votre code ci-dessus *********************

def tri(ma_liste):  # fonction à un seul argument
    # TODO n° 2 de l'exercice 7 (version in-place):
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    import random
    random.seed(42)
    # Liste pseudo-aléatoire avec seed fixée (la liste ne change pas si vous relancez)
    ma_liste = [random.randrange(100) for _ in range(20)]   # 20 nombres
    # Cette façon de créer des listes s'appelle "list comprehension" et s'exécute
    # généralement plus rapidement qu'une boucle for en plusieurs lignes.
    # Cependant, par soucis de compréhension, il est des fois préférable d'écrire
    # la boucle sur plusieurs lignes.
    # Le _ entre le for et le in est juste pour dire qu'on n'utilise pas cette valeur.
    print("Liste à trier:", ma_liste)
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice8():
    import random
    random.seed(7)
    # Liste pseudo-aléatoire avec seed fixée (la liste ne change pas si vous relancez)
    ma_liste = [random.randrange(100) for _ in range(10)]   # 10 nombres
    print("Liste à séparer:", ma_liste)
    # ******************** Votre code ci-dessous ********************
    pairs = [i for i in ma_liste if i%2 == 0]
    print(f"\nPairs: {pairs}")
    impaires = [i for i in ma_liste if i%2 == 1]
    print(f"\nImpairs: {impaires}")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice9():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice10():
    liste_de_liste = [[93, 49, 71], [36, 83, 53], [66, 32, 51]]
    liste_applatie = []
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

# Fonction à compléter ex11:
def est_palindrome(ma_chaine):
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice11():
    ma_chaine = input("Entrez la chaine de caractères: ")
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************


if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    ##exercice1()
    ##exercice2()
    ##exercice3()
    ##exercice4()
    ##exercice5()
    exercice6()
    exercice7()
    exercice8()
    exercice9()
    exercice10()
    exercice11()
