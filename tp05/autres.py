def fact(n: int) -> int:
    """Fonction récursive qui rend la valeur factorielle

    Args:
        n (int): entier de départ

    Returns:
        int: valeur finale
    """
    if n < 0:
        raise ValueError("Pas de nobre entiers en dessous de 0")
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return n * (fact(n - 1))