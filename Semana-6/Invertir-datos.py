class Nodo:
    """
    Clase que representa un nodo de la lista enlazada.
    Contiene un valor y una referencia al siguiente nodo.
    """
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato del nodo
        self.siguiente = None  # Referencia al siguiente nodo, inicialmente es None

class ListaEnlazada:
    """
    Clase que representa una lista enlazada.
    Contiene un metodo para invertir la lista.
    """
    def __init__(self):
        self.cabeza = None  # Inicialmente la lista está vacía

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo  # Si la lista está vacía, el nuevo nodo es la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorremos hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Enlazamos el último nodo con el nuevo nodo

    def imprimir(self):
        """
        Imprime los elementos de la lista enlazada.
        """
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print('None')

    def invertir(self):
        """
        Invierte la lista enlazada modificando las referencias de los nodos.
        """
        previo = None  # Inicialmente no hay nodo previo
        actual = self.cabeza  # Empezamos desde la cabeza de la lista
        while actual:
            siguiente = actual.siguiente  # Guardamos referencia al siguiente nodo
            actual.siguiente = previo  # Invertimos la dirección del enlace
            previo = actual  # Movemos el puntero previo al nodo actual
            actual = siguiente  # Avanzamos al siguiente nodo
        self.cabeza = previo  # La nueva cabeza de la lista es el último nodo original

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

print("Lista original:")
lista.imprimir()

lista.invertir()
print("Lista invertida:")
lista.imprimir()
