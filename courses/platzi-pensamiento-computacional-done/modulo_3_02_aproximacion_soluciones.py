def raiz_n_esima(x: int, n: int=2, paso: float=0.01, epsilon: float=0.001):
    """
    Programa para sacar la raiz n-esima de un numero entero dado

    Arguments
    ---------
    x (int): Numero para ser evaluado y sacar la raiz n-esima.
    n (int): Indica la raiz que se buscara. default=2
    paso (float): default=0.01
    epsilon (float): default=0.001

    Return
    ------
    response: str
    """
    resultado = paso*1.
    while abs(resultado**n - x) >= epsilon and (resultado**n <= x):
        resultado += paso
    
    response = f"La raiz {n} del numero {x} es {resultado}"
    
    return response