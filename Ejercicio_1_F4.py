#Estudiantes: ANDREA LIZARAZO PRADA_LUSBIN FERNEI BARAJAS CABALLERO_MAVERIK ANDRES CALDERON URIBE_OSCAR GOMEZ ARENAS_JOJHAN DAVID LIZARAZO RIOS
#Grupo: 230
#Programa: Ingenieria de sitemas
#Codigo fuente: autoria propia

#Inicio del programa  
  
#Programa Software FJ
# Importa ABC (Abstract Base Class) para crear clases abstractas
# y abstractmethod para marcar métodos que las hijas deben implementar
from abc import ABC, abstractmethod

import logging  # Importa el módulo para registrar errores y eventos del sistema.


# --------------------------------------------------
# CONFIGURACIÓN DEL ARCHIVO LOG
# --------------------------------------------------
import os  # Permite trabajar con las rutas de los archivos.
# Configura el archivo donde se guardarán los registros del sistema.
# Obtiene la ubicación donde está guardado el programa Python.
ruta_programa = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta completa donde se guardará el archivo LOG.
ruta_log = os.path.join(ruta_programa, "errores.log")

# Configura el archivo donde se guardarán los registros del sistema.
logging.basicConfig(
    filename=ruta_log,  # Guarda el archivo LOG junto al programa Python.
    level=logging.INFO,  # Permite registrar eventos y errores.
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
# Muestra en la consola la ubicación del archivo LOG.
print("Archivo de registros ubicado en:")
print(ruta_log)

# --------------------------------------------------
# EXCEPCIONES PERSONALIZADAS
# --------------------------------------------------

# Define una excepción personalizada para errores de clientes.
class ErrorCliente(Exception):
    pass


# Define una excepción personalizada para errores de reservas.
class ErrorReserva(Exception):
    pass


# Define una excepción personalizada para errores de servicios.
class ErrorServicio(Exception):
    pass


# --------------------------------------------------
# FUNCIONES PARA EL MANEJO DE ERRORES
# --------------------------------------------------

# Define una función para mostrar y registrar los errores.
def registrar_error(error):

    # Muestra el error en la terminal.
    print(f"\nSe presentó un error: {error}")

    # Guarda el error en el archivo de registros.
    logging.error("%s", error)


# Define una función para registrar eventos importantes.
def registrar_evento(mensaje):

    # Muestra el evento en la terminal.
    print(f"\nEvento del sistema: {mensaje}")

    # Guarda el evento en el archivo de registros.
    logging.info("%s", mensaje)


# Define una función para validar que un dato no esté vacío.
def validar_dato(dato, nombre_campo):

    # Comprueba si el dato está vacío o contiene solamente espacios.
    if not dato or not str(dato).strip():

        # Genera una excepción si el campo está vacío.
        raise ValueError(
            f"El campo {nombre_campo} no puede estar vacío."
        )

    # Retorna el dato cuando supera la validación.
    return dato
# Define la clase Entidad; al heredar de ABC se vuelve abstracta
# y no se pueden crear objetos directamente de ella
class Entidad(ABC):
    # Clase base abstracta para las entidades del sistema
 
    # Constructor: se ejecuta al crear un objeto y recibe el id y el nombre
    def __init__(self, id, nombre):
        # Guarda el id (documento del cliente o código del servicio);
        # el guion bajo indica que es un atributo protegido (uso interno)
        self._id = id
        # Guarda el nombre del cliente o el nombre asociado al servicio
        self._nombre = nombre
 
    # Método getter: permite consultar el id desde fuera de la clase
    def obtener_id(self):
        # Devuelve el valor guardado en el atributo _id
        return self._id
 
    # Método getter: permite consultar el nombre desde fuera de la clase
    def obtener_nombre(self):
        # Devuelve el valor guardado en el atributo _nombre
        return self._nombre
 
    # Decorador que marca el método como abstracto: cada clase hija
    # está obligada a escribir su propia versión
    @abstractmethod
    def mostrar_informacion(self):
        # No hace nada aquí; solo define que el método debe existir en las hijas
        pass
 
 
# Define la clase Cliente, que hereda todo lo de Entidad (id, nombre y getters)
class Cliente(Entidad):
 
    # Constructor de Cliente: recibe los datos del cliente
    # (se escribe un parámetro por línea para que sea más legible)
    def __init__(
        self,
        id,                  # Número de documento de identidad
        nombre,              # Nombre del cliente
        numero_telefono,     # Número telefónico de contacto
        correo_electronico,  # Dirección de correo electrónico
        direccion_servicio,  # Dirección donde se requiere el servicio
        edad                 # Edad, para validar que sea mayor de edad
    ):
 
        # Llama al constructor de la clase padre (Entidad) para que guarde
        # el id y el nombre; así no se repite código
        super().__init__(id, nombre)
 
        # Guarda el teléfono como atributo protegido del cliente
        self._numero_telefono = numero_telefono
        # Guarda el correo electrónico del cliente
        self._correo_electronico = correo_electronico
        # Guarda la dirección donde se prestará el servicio
        self._direccion_servicio = direccion_servicio
        # Guarda la edad del cliente
        self._edad = edad
 
    #-------------------se agrega el metodo validar cliente------------------------------------------------------------#
    # Método que junta todas las validaciones del cliente; si alguna falla
    # lanza una excepción, y si todas pasan devuelve True
    def validar_cliente(self):
 
        # Comprueba que el nombre no esté vacío.
        # "not" invierte el resultado: entra al if cuando validar_nombre() devuelve False
        if not self.validar_nombre():
            # Detiene el método y lanza la excepción ErrorCliente con este mensaje
            raise ErrorCliente("El nombre del cliente es obligatorio.")
 
        # Comprueba que el cliente sea mayor de edad.
        # Entra al if cuando validar_edad() devuelve False
        if not self.validar_edad():
            # Lanza ErrorCliente indicando que no cumple la edad mínima
            raise ErrorCliente("El cliente debe ser mayor de 18 años.")
 
        # Comprueba que el correo tenga el símbolo @.
        # Entra al if cuando validar_correo() devuelve False
        if not self.validar_correo():
            # Lanza ErrorCliente indicando que el correo no es válido
            raise ErrorCliente("El correo electrónico no es válido debe contener @.")
 
        # Comprueba que el teléfono tenga mínimo 7 caracteres.
        # Entra al if cuando validar_telefono() devuelve False
        if not self.validar_telefono():
            # Lanza ErrorCliente indicando que el teléfono es muy corto
            raise ErrorCliente("El teléfono debe tener mínimo 7 dígitos.")
 
        # Si ninguna validación falló, el cliente es válido y se devuelve True
        return True
    #--------------------------------------------------------------------------------#
 
    # Método que valida el nombre; devuelve True o False
    def validar_nombre(self):
        # strip() quita los espacios al inicio y al final;
        # es válido si después de quitarlos queda al menos un carácter
        return len(self._nombre.strip()) > 0
 
    # Método que valida la edad; devuelve True o False
    def validar_edad(self):
        # Es válido solo si la edad es 18 o más (mayoría de edad)
        return self._edad >= 18
 
    # Método que valida el correo; devuelve True o False
    def validar_correo(self):
        # Es válido si el texto contiene el símbolo "@"
        return "@" in self._correo_electronico
 
    # Método que valida el teléfono; devuelve True o False
    def validar_telefono(self):
        # Es válido si el teléfono tiene 7 o más caracteres
        return len(self._numero_telefono) >= 7
 
    # Implementa el método abstracto heredado de Entidad
    # (cada clase lo muestra a su manera: polimorfismo)
    def mostrar_informacion(self):
        # Imprime un salto de línea y el título de la sección
        print("\n===== CLIENTE =====")
        # Imprime el id usando el getter heredado de Entidad
        print(f"Identificación: {self.obtener_id()}")
        # Imprime el nombre usando el getter heredado de Entidad
        print(f"Nombre: {self.obtener_nombre()}")
        # Imprime el teléfono guardado en el objeto
        print(f"Teléfono: {self._numero_telefono}")
        # Imprime el correo guardado en el objeto
        print(f"Correo: {self._correo_electronico}")
        # Imprime la dirección del servicio guardada en el objeto
        print(f"Dirección: {self._direccion_servicio}")
        # Imprime la edad guardada en el objeto
        print(f"Edad: {self._edad}")
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