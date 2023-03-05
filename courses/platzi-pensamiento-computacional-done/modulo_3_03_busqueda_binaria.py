def raiz_n_esima(x: int, n: int=2, epsilon: float=0.001):
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
    bajo = 0.0 # valor más bajo en el espacio de busqueda
    alto = x * 1.  # valor más alto en el espacio de busqueda
    
    # valor de la mitad para ir cortando el espacio de busqueda
    resultado = (bajo + alto) / 2

    while abs(resultado**n - x) >= epsilon:
        if resultado**n > x:
            alto = resultado
        else:
            bajo = resultado
        
        resultado = (bajo + alto) / 2

    response = f"La raiz {n} del numero {x} es {resultado}"
    
    return response