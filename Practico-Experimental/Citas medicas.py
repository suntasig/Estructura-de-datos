from datetime import datetime


class Paciente:
    """
    Representa a un paciente con datos básicos.
    """
    def __init__(self, id_paciente, nombre, apellido, cedula):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def __str__(self):
        return f"{self.id_paciente}: {self.nombre} {self.apellido} - Cédula: {self.cedula}"


class Turno:
    """
    Representa un turno médico asignado a un paciente.
    """
    def __init__(self, id_turno, paciente, fecha_hora, especialidad):
        self.id_turno = id_turno
        self.paciente = paciente
        self.fecha_hora = fecha_hora
        self.especialidad = especialidad

    def __str__(self):
        fecha_formateada = self.fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"Turno #{self.id_turno} | {fecha_formateada} | Especialidad: {self.especialidad} | Paciente: {self.paciente.nombre} {self.paciente.apellido}"


class Agenda:
    """
    Administra la lista de turnos de la clínica.
    """
    def __init__(self):
        self.turnos = []
        self.contador_turnos = 1

    def agregar_turno(self, paciente, fecha_hora, especialidad):
        """
        Agrega un nuevo turno a la agenda.
        """
        turno = Turno(self.contador_turnos, paciente, fecha_hora, especialidad)
        self.turnos.append(turno)
        self.contador_turnos += 1
        print("Turno registrado con éxito.")

    def mostrar_turnos(self):
        """
        Muestra todos los turnos registrados en la agenda.
        """
        print("\n--- Agenda de Turnos ---")
        if not self.turnos:
            print("No hay turnos registrados.")
            return

        for turno in self.turnos:
            print(turno)

    def consultar_por_especialidad(self, especialidad):
        """
        Filtra y muestra turnos según una especialidad específica.
        """
        print(f"\n--- Turnos para la especialidad: {especialidad} ---")
        turnos_filtrados = [t for t in self.turnos if t.especialidad.lower() == especialidad.lower()]

        if not turnos_filtrados:
            print("No hay turnos registrados para esta especialidad.")
            return

        for turno in turnos_filtrados:
            print(turno)


# Programa principal
if __name__ == "__main__":
    # Crear la agenda
    agenda = Agenda()

    # Crear pacientes
    paciente1 = Paciente(1, "Luis", "Pérez", "1234567890")
    paciente2 = Paciente(2, "Ana", "García", "0987654321")
    paciente3 = Paciente(3, "Kleber","Suntasig","0502530744")

    # Agregar turnos
    agenda.agregar_turno(paciente1, datetime(2025, 1, 15, 9, 0), "Cardiología")
    agenda.agregar_turno(paciente2, datetime(2025, 1, 16, 10, 30), "Dermatología")
    agenda.agregar_turno(paciente3, datetime(2025, 1, 16, 11, 15), "Cardiología")

    # Mostrar todos los turnos
    agenda.mostrar_turnos()

    # Consultar turnos por especialidad
    agenda.consultar_por_especialidad("Cardiología")

    print("\nEjecución completada.")
