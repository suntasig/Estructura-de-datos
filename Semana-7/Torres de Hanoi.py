def torres_de_hanoi(n, origen, auxiliar, destino):
    """
    Resuelve el problema de las Torres de Hanoi de forma recursiva.

    :param n: Número de discos a mover.
    :param origen: Nombre de la torre de origen.
    :param auxiliar: Nombre de la torre auxiliar.
    :param destino: Nombre de la torre de destino.
    """
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")  # Caso base: mover un único disco
    else:
        # Mover n-1 discos desde el origen al auxiliar usando el destino como auxiliar
        torres_de_hanoi(n - 1, origen, destino, auxiliar)
        # Mover el disco restante al destino
        print(f"Mover disco de {origen} a {destino}")
        # Mover los n-1 discos desde el auxiliar al destino usando el origen como auxiliar
        torres_de_hanoi(n - 1, auxiliar, origen, destino)

# Ejemplo de uso
if __name__ == "__main__":
    numero_de_discos = 3  # Cambiar este valor para probar con más discos
    torres_de_hanoi(numero_de_discos, "Origen", "Auxiliar", "Destino")
