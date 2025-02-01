import queue  # Importa la librería queue para manejar la cola de asistentes.
import threading  # Permite la ejecución de múltiples hilos en paralelo.
import time  # Se usa para simular el tiempo de registro de asistentes.


class Asiento:
    def __init__(self, numero):
        """Inicializa un asiento con un número y estado de ocupación."""
        self.numero = numero
        self.ocupado = False

    def asignar(self):
        """Marca el asiento como ocupado."""
        self.ocupado = True

    def __str__(self):
        """Devuelve una representación en cadena del asiento, indicando si está ocupado o disponible."""
        return f"Asiento {self.numero} {'(Ocupado)' if self.ocupado else '(Disponible)'}"


class Auditorio:
    def __init__(self, total_asientos=100):
        """Inicializa el auditorio con una cola de asistentes y una lista de asientos disponibles."""
        self.cola_ingreso = queue.Queue()  # Cola FIFO para gestionar el orden de los asistentes.
        self.asientos_disponibles = [Asiento(i) for i in range(1, total_asientos + 1)]  # Lista de asientos.

    def registrar_asistente(self, nombre):
        """Añade un asistente a la cola de ingreso."""
        self.cola_ingreso.put(nombre)

    def asignar_asientos(self):
        """Asigna los asientos a los asistentes en el orden de llegada."""
        while not self.cola_ingreso.empty() and self.asientos_disponibles:
            asistente = self.cola_ingreso.get()  # Se obtiene el primer asistente en la cola.
            asiento = self.asientos_disponibles.pop(0)  # Se asigna el primer asiento disponible.
            asiento.asignar()
            print(f"Se ha asignado el {asiento} a {asistente}")


# Simulación de dos personas registrando asistentes
def registrar_personas(auditorio, prefijo, cantidad):
    """Simula el registro de asistentes realizado por dos personas en paralelo."""
    for i in range(1, cantidad + 1):
        auditorio.registrar_asistente(f"{prefijo} {i}")  # Registra un asistente con un identificador.
        time.sleep(0.1)  # Simula un pequeño retraso en el registro.


if __name__ == "__main__":
    auditorio = Auditorio(100)  # Crea un auditorio con 100 asientos.

    # Se crean dos hilos para simular el registro simultáneo de asistentes.
    t1 = threading.Thread(target=registrar_personas, args=(auditorio, "Persona A", 50))
    t2 = threading.Thread(target=registrar_personas, args=(auditorio, "Persona B", 50))

    t1.start()
    t2.start()
    t1.join()  # Se espera a que el primer hilo termine.
    t2.join()  # Se espera a que el segundo hilo termine.

    auditorio.asignar_asientos()  # Se asignan los asientos a los asistentes en orden de llegada.
