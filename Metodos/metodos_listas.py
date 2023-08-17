lista= list(['juan','pedro',24])

#cuenta la cantidad de elementos
cantidad_elemtos= len(lista)

#Agrega un elemento a la lista
lista.append(False)

#Agrega un elemento en un punto especifico
lista.insert(2,True)

#Agrea varios elementos a la lista
lista.extend([False, 45, 2221])

#elimina un elemento de la lista, -1 para eliminar de el ultimo hacia atras
lista.pop(0)

#Elimina un elemento de la lista
lista.remove('pedro')

#Elimina todos los elementos de la lista
#lista.clear()

#Organiza los elementos de forma ascendente, solo funciona en lista sin cadenas de texto
lista.sort(reverse=True)# el parametro reverse=true lo que hace es que invierte la lista despues de ordenarla

#Invierte los elementos de la lista ,sin importar el orden
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado= dir(lista.index(True))


print(elemento_encontrado)

