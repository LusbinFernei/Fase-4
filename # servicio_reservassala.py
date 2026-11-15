# servicio_reservassala.py

# --------------------------------------------------
# PROYECTO SOFTWARE FJ - GRUPO 230
# RESPONSABLE: OSCAR GÓMEZ ARENAS
# --------------------------------------------------

from abc import abstractmethod  # Importa abstractmethod para definir métodos abstractos.
from entidad import Entidad  # Importa la clase Entidad 


# --------------------------------------------------
# CLASE SERVICIO
# --------------------------------------------------

class Servicio(Entidad):  # Hereda de Entidad y representa la clase base de los servicios.

    def __init__(self, id, nombre, tipo_servicio, costo_base, disponible=True):  # Inicializa los datos del servicio.

        super().__init__(id, nombre)  # Hereda el identificador y el nombre desde Entidad.

        self.tipo_servicio = tipo_servicio  # Guarda el tipo de servicio.
        self.costo_base = costo_base  # Guarda el costo base del servicio.
        self.disponible = disponible  # Indica si el servicio está disponible.

    @abstractmethod
    def calcular_costo(self, duracion):  # Define el método para calcular el costo según la duración.
        pass  # Deja la implementación para las clases hijas.

    @abstractmethod
    def describir_servicio(self):  # Define el método para describir el servicio.
        pass  # Deja la implementación para las clases hijas.

    @abstractmethod
    def validar_parametros(self):  # Define el método para validar los datos del servicio.
        pass  # Deja la implementación para las clases hijas.

    @abstractmethod
    def mostrar_informacion(self):  # Define el método para mostrar la información del servicio.
        pass  # Deja la implementación para las clases hijas.


# --------------------------------------------------
# CLASE RESERVASALA
# --------------------------------------------------

class ReservaSala(Servicio):  # Hereda los atributos y métodos de la clase Servicio.

    def __init__(self, id, nombre, tipo_sala, costo_base, capacidad_asientos):  # Inicializa los datos de la sala.

        super().__init__(id, nombre, "Reserva de Sala", costo_base, True)  # Envía los datos al constructor de Servicio.

        self.tipo_sala = tipo_sala  # Guarda el tipo de sala.
        self.capacidad_asientos = capacidad_asientos  # Guarda la capacidad de personas de la sala.

        self.validar_parametros()  # Ejecuta la validación de los parámetros de la sala.

    def validar_parametros(self):  # Implementa el método de validación heredado de Servicio.

        return True  # Retorna True para indicar que los parámetros son válidos.

    def calcular_costo(self, duracion):  # Calcula el costo de acuerdo con la duración de la reserva.

        return self.costo_base * duracion  # Multiplica el costo base por las horas reservadas.

    def describir_servicio(self):  # Genera una descripción de las características de la sala.

        return (
            f"Sala tipo {self.tipo_sala} "  # Incluye el tipo de sala en la descripción.
            f"con capacidad para "  # Agrega el texto que indica la capacidad.
            f"{self.capacidad_asientos} personas."  # Incluye la cantidad de personas permitidas.
        )

    def mostrar_informacion(self):  # Muestra los datos principales de la sala.

        print("\n===== INFORMACIÓN DE LA SALA =====")  # Imprime el título de la información.
        print(f"Código: {self.obtener_id()}")  # Muestra el identificador heredado de Entidad.
        print(f"Nombre: {self.obtener_nombre()}")  # Muestra el nombre heredado de Entidad.
        print(f"Tipo de sala: {self.tipo_sala}")  # Muestra el tipo de sala.
        print(f"Capacidad: {self.capacidad_asientos} personas")  # Muestra la capacidad de la sala.
        print(f"Costo base: ${self.costo_base}")  # Muestra el costo base.
        print(f"Disponible: {self.disponible}")  # Muestra la disponibilidad de la sala.
        print(self.describir_servicio())  # Muestra la descripción del servicio.
