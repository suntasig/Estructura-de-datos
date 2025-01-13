# Importamos el módulo string para obtener el abecedario en minúsculas
import string

# Creamos una lista con las letras del abecedario
abecedario = list(string.ascii_lowercase)

# Usamos una comprensión de listas para filtrar las letras

resultado = [
    letra for indice, letra in enumerate(abecedario)
    if (indice + 1) % 3 != 0
]

# Mostramos la lista resultante por pantalla
print("El abecedario después de eliminar las letras en posiciones múltiplos de 3 es:")
print(resultado)
