from __future__ import annotations

def divide(nombre1, nombre2) -> int | float | None:
    if nombre1 <= 0 and nombre2 > 0:
        raise ValueError("'nombre1' est plus petit ou égal à zero")
    elif nombre2 <= 0 and nombre1 > 0:
        raise ValueError("'nombre2' est plus petit ou égal à zero")
    elif nombre1 <= 0 and nombre1 <= 0:
        raise ValueError("'nombre1' et 'nombre2' sont plus petits que zéro")
    return nombre1 // nombre2 if isinstance(nombre1, int) and isinstance(nombre2, int) else nombre1 / nombre2
