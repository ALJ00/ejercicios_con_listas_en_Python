lista = ["1","2","3","4","5"]

elemento = input("¿qué elemento deseas buscar?")

while True:
    if elemento in lista:
        indice = lista.index(elemento)
        lista.remove(elemento)
        print("El elemento {} de la lista se encontraba"
              "en la posición {}. Ha sido eliminado y ésta es la lista resultante: {}".format(elemento,
                                                                                              indice,lista))
        break
    else:
        elemento = input("Elemento no encontrado, introduzca otro: ")