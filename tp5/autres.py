def fact(n: int) -> int:
    """Fonction récursive qui rend la valeur factorielle

    Args:
        n (int): entier de départ

    Returns:
        int: valeur finale
    """
    if n < 0:
        raise ValueError("Pas de nobre entiers en dessous de 0")
    if n == 0: 
        return 0
    if n == 1:
        return 1
    return n * (fact(n - 1))