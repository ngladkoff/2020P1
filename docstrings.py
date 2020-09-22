def is_str_empty(texto: str) -> bool:
    """
    Funcion para saber si una cadena de caracteres
    esta vacia.


    Parameters

    ----------

    texto : str
        Cadena de caracteres a evaluar


    Returns

    -------

    bool
        True si esta vacia
        False si no lo esta


    """

    if (texto == ""):
        return True

    return False

print(is_str_empty(5))
print()
print()
print(is_str_empty.__doc__)
print()
print()
help(is_str_empty)
print()
print(is_str_empty(True))