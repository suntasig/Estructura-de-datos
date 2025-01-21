import random


# Clase que representa un nodo de la lista enlazada
class Node:
    def __init__(self, data):
        self.data = data  # Dato almacenado en el nodo
        self.next = None  # Puntero al siguiente nodo


# Clase que representa la lista enlazada
class LinkedList:
    def __init__(self):
        self.head = None  # Inicialmente la lista está vacía

    # Método para agregar un nodo al final de la lista
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # Si la lista está vacía, el nuevo nodo es la cabeza
            return
        current = self.head
        while current.next:
            current = current.next  # Recorre la lista hasta el último nodo
        current.next = new_node  # Agrega el nuevo nodo al final

    # Método para mostrar la lista enlazada
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")  # Indica el final de la lista

    # Método eliminar los nodos que estén fuera del rango especificado
    def filter_range(self, min_val, max_val):
        # Eliminar nodos de la cabeza que estén fuera del rango
        while self.head and (self.head.data < min_val or self.head.data > max_val):
            self.head = self.head.next
        current = self.head
        if not current:
            return
        # Recorrer la lista y eliminar nodos fuera del rango
        while current.next:
            if current.next.data < min_val or current.next.data > max_val:
                current.next = current.next.next  # Elimina el nodo saltándolo
            else:
                current = current.next  # Avanza al siguiente nodo


# Crear lista enlazada con 50 números aleatorios
linked_list = LinkedList()
for _ in range(50):
    linked_list.append(random.randint(1, 999))  # Genera un número aleatorio entre 1 y 999

# Mostrar la lista enlazada original
print("Lista enlazada original:")
linked_list.display()

# Leer el rango de valores desde el teclado
min_val = int(input("Ingrese el valor mínimo: "))
max_val = int(input("Ingrese el valor máximo: "))

# Filtrar valores fuera del rango
linked_list.filter_range(min_val, max_val)

# Mostrar la lista después de filtrar
print("Lista enlazada después de filtrar:")
linked_list.display()
