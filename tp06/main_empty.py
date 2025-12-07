from utils import exercice

class Voiture:
    #exercice1
    def __init__(self, marque: str, couleur:str, kilometrage: int | float) -> None:
        self.marque = marque.capitalize()
        self.couleur = couleur.lower() 
        self.kilometrage = kilometrage #m

    def avancer(self, vitesse: float | int, temps: float | int) -> None:
        """
            `self.avancer()` permet d'augmenter le kilometrage de la voiture en prenant la vitesse (m/s) et le temps (s).
        """
        self.kilometrage += abs(vitesse * temps)
    #exercice2

    def obtenir_kilomètres(self, vitesse: float | int, temps: float | int) -> float:
        x = lambda vitesse, temps: (vitesse * temps)/1000 if temps > 0 else 0
        self.kilometrage += x(vitesse, temps)
        return x(vitesse, temps)


@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    ma_voiture = Voiture("Toyota", "blanche", 25_000)
    ma_voiture.avancer(50/3.6, 20*60)
    print(ma_voiture.kilometrage)
    # ******************** Votre code ci-dessus *********************

    
@exercice
def exercice2():
    # ******************** Votre code ci-dessous ********************
    x = lambda vitesse, temps: (vitesse * temps)/1000 if temps > 0 else 0
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    import random
    random.seed(0)
    a = [random.randrange(0, 100) for _ in range(1000)]

    # ******************** Votre code ci-dessous ********************
    def rm_dup_list_u_dict(input_list: list) -> list:
        """Removes duplicates from a list by using a dict."""
        return list(dict.fromkeys(input_list))
    
    def rm_dup_list_u_2lists(input_list: list) -> list:
        """Removes duplicates from a list by returning a clean list with unique elements."""
        clean_list = []
        for element in input_list:
            if element not in clean_list:
                clean_list.append(element)
        return clean_list
    
    def rm_dup_list_u_set(input_list: list) -> list:
        """Removes duplicates from a list by using a set (best option out of here)."""
        return list(set(input_list))
    
    print(f"No duplicates using a dict proprety:    {sorted(rm_dup_list_u_dict(a))}")
    print(f"No duplicates using 2 lists:            {sorted(rm_dup_list_u_2lists(a))}")
    print(f"No duplicates using a set:              {sorted(rm_dup_list_u_set(a))}")

    def rm_even_numbers_using_set_difference(input_list: list) -> list:
        return list(set(input_list) - set(range(0, 100, 2)))
    
    print(f"No duplicates, no even numbers:         {sorted(rm_even_numbers_using_set_difference(a))}")
    # ******************** Votre code ci-dessus *********************


if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    exercice1()
    exercice2()
    exercice3()
    ...
