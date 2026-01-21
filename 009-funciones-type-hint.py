def funcion_de_ejemplo(a: int | float, b: int | float) -> int | bool:
    resultado = a / b
    if resultado == 1:
        return False

    print("---")
    print(resultado)
    print("---")

    return 1


funcion_de_ejemplo(1.2, "3")
funcion_de_ejemplo(2.2, 2.2)
