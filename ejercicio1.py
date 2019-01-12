lista = []
parsed = False
while not parsed:
    try:
        num_elementos = int(input("¿Cuántos elementos quieres introudcir en la lista?"))
        parsed = True # we only get here if the previous line didn't throw an exception
    except ValueError:
        print ('Valor inválido, introduce un número...!')

for i in range(num_elementos):
    lista.append(i)

print(lista)