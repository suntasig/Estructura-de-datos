# Creamos una lista que contiene los números del 1 al 10
numeros = list(range(1, 11))  # La función range genera números del 1 al 10

# Invertimos el orden de los números en la lista
numeros_invertidos = numeros[::-1]  # Usamos slicing para invertir la lista

# Convertimos los números en una cadena separada por comas
resultado = ", ".join(map(str, numeros_invertidos))
# map(str, ...) convierte cada número en texto para usar join

# Mostramos el resultado por pantalla
print("Los números del 1 al 10 en orden inverso son:")
print(resultado)
