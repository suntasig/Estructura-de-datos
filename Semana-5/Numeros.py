# Solicitamos al usuario que introduzca los números ganadores
# Creamos una lista vacía para almacenar los números
numeros_ganadores = []

# Indicamos cuántos números se necesitan para la lotería (por ejemplo, 6)
cantidad_numeros = 6

# Usamos un bucle para solicitar los números uno por uno
print(f"Introduce los {cantidad_numeros} números ganadores de la lotería:")
for i in range(cantidad_numeros):
    while True:
        try:
            # Pedimos al usuario un número y lo convertimos a entero
            numero = int(input(f"Número {i + 1}: "))

            # Validamos que el número esté dentro del rango permitido (1 a 49, por ejemplo)
            if 1 <= numero <= 49:
                # Añadimos el número a la lista
                numeros_ganadores.append(numero)
                break  # Salimos del bucle interno si la entrada es válida
            else:
                print("El número debe estar entre 1 y 49. Intenta de nuevo.")
        except ValueError:
            # Manejo de errores si el usuario no introduce un número válido
            print("Entrada no válida. Por favor, introduce un número entero.")

# Ordenamos la lista de números ganadores de menor a mayor
numeros_ganadores.sort()

# Mostramos los números ordenados por pantalla
print("\nLos números ganadores de la lotería, ordenados de menor a mayor, son:")
print(numeros_ganadores)
