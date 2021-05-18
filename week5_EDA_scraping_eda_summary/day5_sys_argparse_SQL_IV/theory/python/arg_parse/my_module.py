def exponent(x, y, v=None):
    result = x ** y
    return (result * v) if v else result # si pones if v significa que es diferente a algo de eso se retorna esa multiplicacion y si el resultado es cualquier otro valor, se retorna el result