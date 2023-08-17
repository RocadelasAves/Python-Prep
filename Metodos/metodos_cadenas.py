cadena1= 'mas lo mejor es siempre estar amando'
cadena2= 'por siempre'

#mayus
mayus = cadena1.upper()
#minusc
minus = cadena2.lower()
#primera en mayuscula
pri_mayus= cadena2.capitalize()
#buscar un valor que le pidamos
busqueda_find = cadena1.find('a')
print(busqueda_find)
#Buscamos una cadena en otra
busqueda_index= cadena2.index('siempre')
#si es numerico
es_numerico= cadena1.isnumeric()
#verificar si es alfa númerico
es_alpha= cadena1.isalpha()
#contar cuantas veces aparece
contar= cadena2.count('a')
#cuantos caracteres tiene una cadena
contar_caracteres= len(cadena1)
#verificar con que empieza una cadena
empieza_con= cadena1.startswith('ma')
#verificar con que termina una cadena
termina_con= cadena1.endswith('o')
# si el valor 1 se encuentra en la cadena original reemplaza el valor 1 por el valor 2 
cadena_nueva= cadena1.replace('amando','mamando')
#crea una lista en el valor que le pasamossepara las cadenas
cadena_separada= cadena2.split(',')

print(cadena_separada[0])
                      