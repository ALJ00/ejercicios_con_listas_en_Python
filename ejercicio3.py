lista = ["hola", "1", "2", "adios"]
print(lista)
print("---------------------------")



elemento = input("¿Qué elemento deseas buscar?")

while True:
    if elemento in lista:
        nuevo_elemento = input("¿Elemento encontrado, qué nuevo elemento deseas introducir?")
        indice = lista.index(elemento)
        lista.pop(indice)
        lista.insert(indice, nuevo_elemento)
        break
    else:
        elemento = input("Elemento no encontrado, introduce un nuevo dato por favor...")

print(lista)
