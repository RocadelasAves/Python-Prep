diccionario = {
    'nombre' : 'Sue',
    'apellido': 'Rios',
    'subs': 1000000
}

#Devuelve las claves dentro del diccionario, Tambien nos sirve para iterar. obtenemos un objeto dic_items
claves = diccionario.keys()

#Encuentra un elemento detro del dic, nos devuelve el valor, si no encuentra dice 'none', y el programa continua
obtener_elemento= diccionario.get('Subs')

#Elimina todos los elementos del diccionario
#diccionario.clear()

#Elimina elementos dentro del diccionario, los que le indicamos
diccionario.pop('subs','nombre')

#Obtiendo un elemento dict_items iterables
diccionario_iterable= diccionario.items()


print(diccionario_iterable)