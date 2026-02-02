a = 12
b = "This is an exceptional error"
try:
    c = a + b
except TypeError:
    print("TypeError: No son del tipo adecuado")
    print(f"type: {type(a)} a: {a}")
    print(f"type: {type(b)} b: {b}")

for i in range(5):
    print("*")

raise TypeError("Hemos llegado al final, pero se fuerza error por motivos didácticos")
print("Esta linea no se ejecutará")