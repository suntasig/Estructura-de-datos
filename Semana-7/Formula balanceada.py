def verificar_balance(expresion):
    # Pila para llevar el registro de los paréntesis abiertos
    pila = []

    # Diccionario para emparejar paréntesis de cierre con los de apertura
    pares = {')': '(', '}': '{', ']': '['}

    #  Recorremos cada carácter de la expresión
    for char in expresion:
        # Si el carácter es uno de los paréntesis de apertura, lo agregamos a la pila
        if char in "({[":
            pila.append(char)
        # Si el carácter es uno de los paréntesis de cierre, verificamos
        elif char in ")}]":
            # Si la pila está vacía o no coincide el último elemento de la pila con el paréntesis de apertura correspondiente, no está balanceado
            if not pila or pila[-1] != pares[char]:
                return "La fórmula NO está balanceada"
            pila.pop()  # Si coincide, eliminamos el paréntesis de apertura de la pila

    # Al final, si la pila está vacía, todos los paréntesis fueron balanceados
    if not pila:
        return "La fórmula está balanceada"
    else:
        return "La fórmula NO está balanceada"


# Ejemplo de uso
expresion = "{7+(8*5)-[(9-7)+(4+1)]}"
resultado = verificar_balance(expresion)
print(resultado)
