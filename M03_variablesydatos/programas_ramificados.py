num_1 = int(input('Escoge un entero: '))    # Preguntamos por un primer número.
num_2 = int(input('Escoge otro entero: '))  # Luego preguntamos por un segundo número.

if num_1 > num_2:       # Si el primer número es mayor que el segundo.
    print('El primer número es mayor que el segundo.')  # Imprimimos esta expresión.
elif num_1 < num_2:     # En caso de que el segundo sea mayor.
    print('El segundo número es mayor que el primero.') # Imprimiremos esta expresión.
else:   # En caso de que no cumpla ninguna condición.
    print('Los 2 números son iguales.')

    