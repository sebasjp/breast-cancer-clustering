def raiz_n_esima(x: int, n: int=2):
    """
    Programa para sacar la raiz n-esima de un numero entero dado

    Arguments
    ---------
    x (int): Numero para ser evaluado y sacar la raiz n-esima.
    n (int): Indica la raiz que se buscara. default=2

    Return
    ------
    response: str
    """
    resultado = 0
    while resultado**n < x:
        resultado += 1
    
    if resultado**n == x:
        response = f"La raiz {n} del numero {x} es {resultado}"
    else:
        response = f"No fue posible encontrar la raiz {n} del numero {x}"

    return response