# LLAMAR o invocar la función print()
# para llamar escribmos el IDENTIFICADOR de la función seguido de la LLAMADA: el paréntesis
# Aquí invocamos a print 3 veces
print("Patata")
print()
print("Melón")
print()
print()
print()
print(7)

# En los paréntisis podemos darle "argumentos" a las funciones
#   En la primera llamada el argumento es el str:"Patata"
#   En las siguientes NO HAY argumento
#   Posteriormente el argumento es "Melón" o también 7

# ----------------------------------------------------------------------------------

# Podemos DEFINIR una función para declorar un bloque de código que se debe repetir
"""
def identificador(parametro(s)<OPCIONAL>):
    accion 1
    accion 2
    ...
    accion n
"""

print("FUNCION:")
def duplicar(numero_base):
    numero_duplicado = numero_base * 2
    return numero_duplicado

print(duplicar(3))
