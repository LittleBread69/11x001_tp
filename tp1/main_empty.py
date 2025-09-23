import random

from utils import exercice

#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    print("Bonjour monde !")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    # ******************** Votre code ci-dessous ********************
    print("Nom     : Adam KUDELAS")
    print("Né le   : 02.06.2005")
    print("Contact : michel.lambda@unige.ch")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    # ******************** Votre code ci-dessous ********************
    char1: str = "U"
    char2: str = "N"
    char3: str = "I"
    char4: str = "G"
    char5: str = "E"
    unige:str = " ".join((char1, char2, char3, char4, char5))
    unige_reverse:str = " ".join((char5, char4, char3, char2, char1))
    print(unige)
    print(unige_reverse)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    nombre = input("Donner un nombre entre 0 et 9: ")
    if len(nombre) != 1:
        print(f"{int(nombre)} n'est pas un nombre valide.")
    nombre = int(nombre)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    PI = 3.1415926535
    rayon = int(input("Entrer le rayon du cercle (en m) : "))   # int(.) fait une conversion de type vers int
    # ******************** Votre code ci-dessous ********************
    print(f"Cercle avec un périmètre de {2 * PI * rayon} m et une aire de {PI * rayon * rayon} m^2")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    nb_of_days = int(input("Entrez un nombre de jours à convertir : "))
    _jours = nb_of_days
    # ******************** Votre code ci-dessous ********************
    #Je considère qu'une année est 365 jours
    annees = nb_of_days // 365
    nb_of_days %= 365
    semaines = nb_of_days // 7
    nb_of_days %= 7
    print(f"{_jours} jours font {annees} année(s), {semaines} semaine(s) et {nb_of_days} jour(s).")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    a = 7
    b = 2
    c = 7 // 2  # Ne modifier que cette ligne
    d = 7 % 2   # L'opérateur % est le "modulo", aussi écrit "mod" en maths
    print(f"{a} / {b} = {c:.2f}, reste = {d}")

@exercice
def exercice8():
    n = int(input("Entrez un entier strictement supérieur à 1: "))
    # ******************** Votre code ci-dessous ********************
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n+1
        print(int(n))
    # ******************** Votre code ci-dessus *********************

if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    exercice1()
    exercice2()
    exercice3()
    exercice4()
    exercice5()
    exercice6()
    exercice7()
    exercice8()
