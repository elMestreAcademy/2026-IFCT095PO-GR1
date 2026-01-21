# 005-ejercicio-01-caracteres

## Con estas herramients transforma "Hola mundo" a su sequencia de cifras equivalente

texto = chr(97)
print(texto)


def describir(caracter):
    print(ord(caracter))


for letra in "Hola mundo":
    describir(letra)
