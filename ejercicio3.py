lista = ["hola", 1, 2, "adios"]
print(lista)
print("---------------------------")

contenido = False

while True:
    try:
        consulta = int(input("¿qué elemento quieres?"))

        print = lista.pop(lista.index(consulta))

        elemento2 = int(input("Introduce un nuevo elemento"))

        lista.insert(lista.index(consulta),elemento2)



        break
    except ValueError:
        print('Elemento inexistente, introduce otro elemento...!')







print(lista)
