student_scores = [3.29, 3.86, 2.68, 5.25, 4.97, 2.25, 3.17, 5.83, 3.22, 4.46, 2.81]

def pseudo_max(liste_de_nombres:list[int | float]) -> int | float:
    plus_grand = -float('inf')
    for element in liste_de_nombres:
        if element > plus_grand:
            plus_grand = element
    return plus_grand

if __name__ == '__main__':
    print(pseudo_max(student_scores))
