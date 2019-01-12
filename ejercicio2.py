lista = [1,2,3,4,4,6,7,7,9,10]
posicion = 0

for i in lista:
    print("Posición [{0}] de la lista"
          " = {1} ---- Se repite: "
          " {2} veces.".format(posicion,
                               i,lista.count(i)))
    posicion+=1