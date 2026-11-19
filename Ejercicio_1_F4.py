#Estudiantes: ANDREA LIZARAZO PRADA_LUSBIN FERNEI BARAJAS CABALLERO_MAVERIK ANDRES CALDERON URIBE_OSCAR GOMEZ ARENAS_JOJHAN DAVID LIZARAZO RIOS
#Grupo: 230
#Programa: Ingenieria de sitemas
#Codigo fuente: autoria propia

#Inicio del programa  
  
#Programa Software FJ
from datetime import datetime
from datetime import timedelta#Se importa las libreria necesaria para faciclitar la operaciones de comparacion con las fechas y horas

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
# Este código define dos clases de servicios: AlquilerEquipo y AsesoriaEspecializada, ambas heredan de la clase base Servicio. 

"""
CLASE: Alquiler de Equipo
"""
# Esta clase representa un servicio de alquiler de equipo, que hereda de la clase base Servicio.
# Incluye atributos específicos como el tipo de equipo y métodos para validar parámetros, calcular costos, describir el servicio y mostrar información detallada del servicio.
class AlquilerEquipo(Servicio):
    # Constructor de la clase AlquilerEquipo, donde se inicializan los atributos específicos del servicio de alquiler de equipo.
    def __init__( # Este método inicializa los atributos de la clase AlquilerEquipo, incluyendo el tipo de equipo y el costo base del servicio.
        self, # representa al objeto actual de la clase AlquilerEquipo.
        id, # identificador unico del servicio de alquiler de equipo.
        nombre, # nombre del servicio de alquiler de equipo.
        tipo_equipo, # tipo de equipo que se va a alquilar.
        costo_base # costo base del servicio de alquiler de equipo.
    ):
        # llamada al constructor de la clase base Servicio para inicializar los atributos heredados.
        super().__init__(
            id, # envia el identificador único del servicio de alquiler de equipo a la clase base Servicio.
            nombre, # envia el nombre del servicio de alquiler de equipo a la clase base Servicio.
            "Alquiler de Equipo", # envia el tipo de servicio a la clase base Servicio.
            costo_base, # envia el costo base del servicio de alquiler de equipo a la clase base Servicio.
            True # envia la disponibilidad del servicio de alquiler de equipo a la clase base Servicio.
        )
        # guarda el tipo de equipo en un atributo específico de la clase AlquilerEquipo.
        # Se usa self. para que el dato quede asociado al objeto y pueda ser accedido desde otros métodos de la clase.
        self.tipo_equipo = tipo_equipo
        # llama al método validar_parametros para asegurarse de que los parámetros proporcionados sean válidos.
        self.validar_parametros()
    # Este método valida los parámetros proporcionados al crear una instancia de AlquilerEquipo. 
    # En este caso, devuelve True, pero se puede modificar para incluir validaciones específicas según sea necesario.
    def validar_parametros(self):
        return True
    # Este método calcula el costo total del servicio de alquiler de equipo en función de la duración del alquiler. Multiplica el costo base por la duración proporcionada.
    def calcular_costo(self, duracion):
        return self.costo_base * duracion
    # Este método devuelve una descripción del servicio de alquiler de equipo, incluyendo el tipo de equipo que se está alquilando.
    def describir_servicio(self):
        return (
            f"Equipo tipo "
            f"{self.tipo_equipo}"
        )
    # Este método muestra información detallada sobre el servicio de alquiler de equipo, incluyendo el identificador, nombre, tipo de equipo, costo base, disponibilidad y una descripción del servicio.
    def mostrar_informacion(self):
        print("\n===== ALQUILER DE EQUIPO =====") # Imprime un encabezado para indicar que se está mostrando información sobre el servicio de alquiler de equipo.
        print(f"Identificador: {self.obtener_id()}") # Imprime el identificador único del servicio de alquiler de equipo utilizando el método obtener_id() heredado de la clase base Servicio.
        print(f"Nombre: {self.obtener_nombre()}") # Imprime el nombre del servicio de alquiler de equipo utilizando el método obtener_nombre() heredado de la clase base Servicio.
        print(f"Tipo de equipo: {self.tipo_equipo}") # Imprime el tipo de equipo que se está alquilando, accediendo al atributo tipo_equipo de la clase AlquilerEquipo.
        print(f"Costo base: ${self.costo_base}") # Imprime el costo base del servicio de alquiler de equipo, accediendo al atributo costo_base de la clase AlquilerEquipo.
        print(f"Disponible: {self.disponible}") # Imprime la disponibilidad del servicio de alquiler de equipo, accediendo al atributo disponible de la clase AlquilerEquipo.
        print(self.describir_servicio()) # Imprime la descripción del servicio de alquiler de equipo utilizando el método describir_servicio() de la clase AlquilerEquipo.

"""
CLASE: Asesoría Especializada
"""
# Esta clase representa un servicio de asesoría especializada, que hereda de la clase base Servicio. 
# Incluye atributos específicos como el tipo de asesoría y métodos para validar parámetros, calcular costos, describir el servicio y mostrar información detallada del servicio.
class AsesoriaEspecializada(Servicio):
    # Constructor de la clase AsesoriaEspecializada, donde se inicializan los atributos específicos del servicio de asesoría especializada.
    def __init__( # Este método inicializa los atributos de la clase AsesoriaEspecializada, incluyendo el tipo de asesoría y el costo base del servicio.
        self, # representa al objeto actual de la clase AsesoriaEspecializada.
        id, # identificador único del servicio de asesoría especializada.
        nombre, # nombre del servicio de asesoría especializada.
        tipo_asesoria, # tipo de asesoría que se va a ofrecer.
        costo_base # costo base del servicio de asesoría especializada.
    ):
        # llamada al constructor de la clase base Servicio para inicializar los atributos heredados.
        super().__init__(
            id, # envia el identificador único del servicio de asesoría especializada a la clase base Servicio.
            nombre, # envia el nombre del servicio de asesoría especializada a la clase base Servicio.
            "Asesoría Especializada", # envia el tipo de servicio a la clase base Servicio.
            costo_base, # envia el costo base del servicio de asesoría especializada a la clase base Servicio.
            True # envia la disponibilidad del servicio de asesoría especializada a la clase base Servicio.
        )
        # guarda el tipo de asesoría en un atributo específico de la clase AsesoriaEspecializada.
        self.tipo_asesoria = tipo_asesoria
        # llama al método validar_parametros para asegurarse de que los parámetros proporcionados sean válidos.
        self.validar_parametros()
    # Este método valida los parámetros proporcionados al crear una instancia de AsesoriaEspecializada. 
    # En este caso, devuelve True, pero se puede modificar para incluir validaciones específicas según sea necesario.
    def validar_parametros(self):
        return True
    # Este método calcula el costo total del servicio de asesoría especializada en función de la duración de la asesoría. Multiplica el costo base por la duración proporcionada.
    def calcular_costo(self, duracion):
        return self.costo_base * duracion
    # Este método devuelve una descripción del servicio de asesoría especializada, incluyendo el tipo de asesoría que se está ofreciendo.
    def describir_servicio(self):
        return (
            f"Asesoría especializada en "
            f"{self.tipo_asesoria}"

        )
    # Este método muestra información detallada sobre el servicio de asesoría especializada, incluyendo el identificador, nombre, tipo de asesoría, costo base, disponibilidad y una descripción del servicio.
    def mostrar_informacion(self):
        print("\n===== ASESORÍA ESPECIALIZADA =====") # Imprime un encabezado para indicar que se está mostrando información sobre el servicio de asesoría especializada.
        print(f"Identificador: {self.obtener_id()}") # Imprime el identificador único del servicio de asesoría especializada utilizando el método obtener_id() heredado de la clase base Servicio.
        print(f"Nombre: {self.obtener_nombre()}") # Imprime el nombre del servicio de asesoría especializada utilizando el método obtener_nombre() heredado de la clase base Servicio.
        print(f"Tipo de asesoría: {self.tipo_asesoria}") # Imprime el tipo de asesoría que se está ofreciendo, accediendo al atributo tipo_asesoria de la clase AsesoriaEspecializada.
        print(f"Costo base: ${self.costo_base}") # Imprime el costo base del servicio de asesoría especializada, accediendo al atributo costo_base de la clase AsesoriaEspecializada.
        print(f"Disponible: {self.disponible}") # Imprime la disponibilidad del servicio de asesoría especializada, accediendo al atributo disponible de la clase AsesoriaEspecializada.
        print(self.describir_servicio()) # Imprime la descripción del servicio de asesoría especializada utilizando el método describir_servicio() de la clase AsesoriaEspecializada.


class Reserva:#Se cre la clase Reserva, la cual administrara los metodo relacionados con las reserva

    def __init__(#Metodo constructor
        self,#Se instancia para poder accder a los atributo de la clase
        codigo_reserva,
        cliente,
        servicio,
        fecha_hora_inicio,
        duracion,
        estado
    ):

        self.codigo_reserva = codigo_reserva#Se guarda el codigo de reserva
        self.cliente = cliente#Se guarda el numero de documento del cliente
        self.servicio = servicio#Se guarda el codigo del servicio
        self.fecha_hora_inicio = fecha_hora_inicio#Se guarda la fecha ingresada por el usaurio
        self.duracion = duracion #Se guarda la duracion en horas ingresada
        self.estado = estado#Se guarda el estado de confirmada

    def confirmar(self):#Se crea el metodo para confrimar la reserva
        self.estado = "Confirmada"#La guarda como confirmada

    def cancelar(self):#Se crea el metodo que cancela una reserva
        self.estado = "Cancelada"#La guarda como cancelada

    def procesar(self):#metodo para procesar la reserva
        self.estado = "Procesada"#La guarda como procesada

    def calcular_total(self):#Metodo para calcular el total a pagar
        return self.servicio.calcular_costo(#Retorna el metodo calcular costo
            self.duracion#Retorna las horas ingresadas por el usuario para calcular el costo
        )

    def mostrar_informacion(self):#Metodo para mostrar la informacion de las reservas creadas

        print("\n===== RESERVA =====")#imprime el titulo de la clase

        print(
            f"Código de reserva: "#Imprime el codigo de la reservsa
            f"{self.codigo_reserva}"#Utilza el codigo ingresado por el usuario
        )

        print(#Imprime al cliente
            f"Cliente: "
            f"{self.cliente.obtener_nombre()}"#Utiliza el nombre ingresado por el  usuario ultilizando el metodo obtener  nombre
        )

        print(
            f"Servicio: "#Imprime el nombre del servicio
            f"{self.servicio.obtener_nombre()}"#Utiliza el servicio seleccionado por el  usuario ultilizando el metodo obtener  nombre
        )
        

        print(
            f"Fecha y hora inicio: "#Impreme la fecha en la que inicia la reserva
            f"{self.fecha_hora_inicio.strftime('%d/%m/%Y %H:%M')}"#Utiliza la fecha ingresada por el usuario
        )

        print(#Imprime la duracion del servicio
            f"Duración: "#Texto que se imprime junto a la duración
            f"{self.duracion} horas"#UTILIZA LA DURACION INGRESADA POR EL USUARIO
        )

        print(#Imprime el estado del servicio
            f"Estado: "#Texto que se imprime junto al estado
            f"{self.estado}"#Utiliza el estado"confirmada""cancelada""procesada"
        )

        print(#Imprime le total a pagar
            f"Total: "#Texto que se imprime junto al total a pagar
            f"${self.calcular_total()}"#Lama al metodo para mostrar el total a pagar
        )

class  SistemaAdministrador:#Se cre la clase que administrara los datos recividos

    def __init__(self):#Se define el meotodo constructor
        #Atributos del metodo constructor
        self.clientes = []#Se crea la lista que alamacenara los objetos  clientes
        self.servicios = []#Se crea la lista que alamacenara los objetos  seervicios
        self.reservas = []#Se crea la lista que almacenara los objetos reservas

        self.cargar_servicios()#Carga la lista de los servicios ofrecidos
    def cargar_servicios(self):#Metodo para cargar los servicios que se ofrecen
        self.servicios.append(#Agrega los objetos a lista
            ReservaSala(#Se crea el objeto apartir del metodo constructo de la clase
                "RS001",
                "Sala Pequeña",
                "Pequeña",
                399900,
                50
            )
        )

        self.servicios.append(
            ReservaSala( 
                "RS002",
                "Sala Mediana",
                "Mediana",
                699900,
                100
            )
        )

        self.servicios.append(
            ReservaSala(
                "RS003",
                "Sala Grande",
                "Grande",
                999900,
                150
            )
        )

    
    # ASESORIAS
  

        self.servicios.append(#Se agrga el pbjeto a la lista
            AsesoriaEspecializada(#Se crea el objeto apartir del metodo constructo de la clase
                "AE001",
                "Asesoría Jurídica",
                "Jurídica",
                100000
            )
        )

        self.servicios.append(
            AsesoriaEspecializada(
                "AE002",
                "Asesoría Tributaria",
                "Tributaria",
                150000
            )
        )

        self.servicios.append(
            AsesoriaEspecializada(
                "AE003",
                "Asesoría Financiera",
                "Financiera",
                100000
            )
        )

        self.servicios.append(
            AsesoriaEspecializada(
                "AE004",
                "Asesoría Marketing",
                "Marketing",
                120000
            )
        )

        self.servicios.append(
            AsesoriaEspecializada(
                "AE005",
                "Asesoría Tecnológica",
                "Tecnológica",
                160000
            )
        )

    # EQUIPOS
    

        self.servicios.append(#Se agrega el objeto a la lista
            AlquilerEquipo(#Se crea el objeto apartir del metodo constructo de la clase
                "EQ001",
                "Equipo de Sonido",
                "Sonido",
                29900
            )
        )

        self.servicios.append(
            AlquilerEquipo(
                "EQ002",
                "Equipo Audiovisual",
                "Audiovisual",
                59900
            )
        )

        self.servicios.append(
            AlquilerEquipo(
                "EQ003",
                "Equipo de Construcción",
                "Construcción",
                39900
            )
        )

    def buscar_cliente (self, id_cliente):#Metodo para buscar a un cliente y validar si ya esta registrado o no
        
    
        for cliente in self.clientes:#Se recorre la lista de clientes

            if cliente.obtener_id() == id_cliente:#Busca un numero de identificacion igual al ingresado
                return cliente#Si conincide retorma al objeto
        return None
    
    def buscar_servicio(self, id_servicio):# Método para buscar un servicio por su identificación
        for servicio in self.servicios:# Recorre la lista de servicios
            if servicio.obtener_id() == id_servicio:# Compara el id del servicio con el id ingresado
                return servicio#Si conincide retorma al objeto
        return None#Si no lo encuentra retorna none

    def buscar_reserva(self, codigo_reserva): # Método para buscar una reserva por su código
        for reserva in self.reservas: # Recorre la lista de reservas
            if reserva.codigo_reserva == codigo_reserva:# Compara el código de la reserva con el código ingresado
                return reserva # Retorna el objeto reserva si lo encuentra
        return None  # Retorna None si no encuentra coincidencias
    

    def registrar_cliente(self, id_cliente, nombre, telefono, correo, direccion, edad):#Metodo para registrar a un cliente nuevo
        validar_dato(id_cliente, "Identificación")#verifica que el campo no este vacio utilizando el metodo validar dato
        validar_dato(nombre, "Nombre")#verifica que el campo no este vacio utilizando el metodo validar dato
        validar_dato(telefono, "Teléfono")#verifica que el campo no este vacio utilizando el metodo validar dato
        validar_dato(correo, "Correo")#verifica que el campo no este vacio utilizando el metodo validar dato
        validar_dato(direccion, "Dirección")#verifica que el campo no este vacio utilizando el metodo validar dato

         
        if self.buscar_cliente(id_cliente) is not None:# verifica si el cliente ya está registrado recorriendo la lista de identificaciones
            raise ErrorCliente("El cliente ya se encuentra registrado.")#Imprime la exepcion  cuando la identificación coincide
        
    
        nuevo_cliente = Cliente(#Crea el cliente con el metodo constructor de la clase Cliente
            id_cliente,#Numero de cedula
            nombre,#Nombre de la persona
            telefono,#Numero celular
            correo,#Correo personal
            direccion,#Direccion de residencia
            edad#Edad
        )
        
        nuevo_cliente.validar_cliente() #verifica que los datos del cliente sean correctos utilizando el metodo validar

        self.clientes.append(nuevo_cliente)# Agrega el nuevo cliente en la lista de clientes
         # Registra el evento exitoso.
        registrar_evento("Cliente registrado exitosamente.")#Ejecuta el metodo registrar_evento imprimiendo el mensaje

    def mostrar_clientes(self):#Metodo para mostrar la informacion de los clientes y a los clientes registrados
        if len(self.clientes) == 0:# Verifica si existen clientes registrados confirmando si la lista esta vacia utilizando len para contar el numero de elementos y compararlos con el "0"
            print("No hay clientes registrados.")  # Muestra un mensaje si la lista está vacía == 0
        else:# Si la lista no esta vacia
            for cliente in self.clientes:# Recorre la lista de clientes
                cliente.mostrar_informacion() #Muestra la información asociada a cada cliente registrado

    
    def mostrar_servicios(self):#Muestra los servicios existentes
        if len(self.servicios) == 0: # Verifica si existen servicios registrados confirmando si la lista esta vacia utilizando len para contar el numero de elementos y compararlos con el "0"
            print("No hay servicios registrados.") # Muestra un mensaje si no hay servicios cargados
        else:#En caso contrario
            print("\n===== SERVICIOS DISPONIBLES =====") # Muestra un título para organizar la salida
            for servicio in self.servicios:# Recorre la lista de servicios
                servicio.mostrar_informacion() # Muestra la información de los servicios regitrados

    def mostrar_reservas(self):#Metodo para registrar las reservas
        if len(self.reservas) == 0: # Verifica si existen reservas creadas confirmando si la lista esta vacia utilizando len para contar el numero de elementos y compararlos con el "0"
            print("No hay reservas registradas actualmente.")# Muestra un mensaje si la lista está vacía
        else:#En caso contrario
         print("\n===== RESERVAS REGISTRADAS =====")# Muestra un título para organizar la salida
         for reserva in self.reservas:# Recorre la lista de reservas para imprimirlas
             reserva.mostrar_informacion() # Muestra la información de cada reserva
    

    def crear_reserva(self,#Metodo para crear una reserva usando el constructor de la clase Reserva
        codigo_reserva,
        id_cliente,
        id_servicio,
        fecha_hora_inicio,
        duracion):
             
        validar_dato(codigo_reserva, "Código de reserva")#Verifica que los datos obligatorios no estén vacíos utilizando el metodo validar
        validar_dato(id_cliente, "Identificación del cliente")#Verifica que los datos obligatorios no estén vacíos utilizando el metodo validar
        validar_dato(id_servicio, "Código del servicio")#Verifica que los datos obligatorios no estén vacíos utilizando el metodo validar
        
        
       
        if duracion <= 0:#verifica que la duración sea mayor a 0
            raise ErrorReserva("La duración debe ser mayor que cero.")#Lanza la exepcion Error y imprime el mensaje
        
        if self.buscar_reserva(codigo_reserva) is not None:#Verifica que el código de reserva no esté repetido.
            raise ErrorReserva("El código de reserva ya existe.")#Lanza la exepcion Error y imprime el mensaje
            
      
        cliente = self.buscar_cliente(id_cliente) # recorre las identificaciones para verificar que no se encuentre ya registrada

        if cliente is None:#Recorre las lista de cliente buscando una identificacion que coinsida
            raise ErrorCliente("El cliente no se encuentra registrado.")#Lanza la exepcion error y imprime el mensaje

        servicio = self.buscar_servicio(id_servicio)# Ejecuta el metodo buscar servicio y verifica que se encuentre en la lista

        if servicio is None:#Si el codigo de servico no existe
            raise ErrorServicio("El servicio no se encuentra registrado.")#Lanza la exepcion error y imprime el mensaje
        
        # Si el cliente y el servicio estan registrados se continua con la reserva
        fecha_hora_fin = fecha_hora_inicio + timedelta(hours=duracion)# Calcula la fecha y hora de finalización de la nueva reserva
        for reserva in self.reservas:#Recorre las reservas existentes
            if reserva.servicio.obtener_id() == id_servicio:  # Verifica que la reserva no se esta haciendo sobre el mismo tipo de servicio y a la misma hora
                inicio_existente = reserva.fecha_hora_inicio #Si existe una reserva con el ingresa obtine la hora de inicio y la guarda el dato en la varible
                fin_existente = (#Variable para guarda la hora y fecha donde termina el serivico ya existente
                    inicio_existente +#se toma la hora de inicio
                    timedelta(hours=reserva.duracion)#Se suma con el tiempo de duracion, calculando asi la hora de terminacion del servicio
                ) 
                if (fecha_hora_inicio < fin_existente and#Compara la hora de incio del nuevo servicio con la hora de terminacion del servicio en curso
                    fecha_hora_fin > inicio_existente):#Compara la hora de terminacion del nuevo servicio y la hora de inicio del servicio en curso
                    raise ErrorReserva(#Lanza la execio error y imprime el mensaje
                        "El servicio ya se encuentra reservado "
                        "en ese horario."
                    )
            nueva_reserva = Reserva(#Si la condicion no se cumple se crea el objeto Reserva y se guarda en la varible utilizando el metodo constructor de la clase Reserva
                    codigo_reserva, #Codigo de la reserva
                    cliente,#Cliente
                    servicio,#Tipo de servicio
                    fecha_hora_inicio,#Fecha y hora de inicio
                    duracion,#Duracion en horas
                    "Confirmada"#Estado de la reserva
                   )
            self.reservas.append(nueva_reserva)# Guarda la reserva en la lista
           
            registrar_evento("Reserva creada exitosamente.")#Ejecuta el metodo regitrar y imprime el mensaje

    def cancelar_reserva(self, codigo_reserva):#Metodo para cancelar la reserva
          
        validar_dato(codigo_reserva, "Código de reserva")#Ejecuta validar para comprobar que el dato no este vacio
        reserva = self.buscar_reserva(codigo_reserva)# Busca la reserva por su código

        if reserva is None:#Si la reserva no exite
            raise ErrorReserva(#Lanza la exepcion error y imprime el mensaje
                            "La reserva no se encuentra registrada."
            )

        if reserva.estado == "Cancelada":#Si la reserva ya fue cancelada, compara el estado con el texto cancelada y sin coindise se ejecuta el raice
            raise ErrorReserva(#Lanza la exepcion y imprime el mensaje
                "La reserva ya fue cancelada"
            )       
        # Si no se lanza la exepcion
        reserva.cancelar()# Llama al método cancelar de la clase Reserva
       
        registrar_evento("Reserva cancelada exitosamente.")#Ejecuta el metodo registrar y imprime le mensaje


def menu():#Metodo para mostrar el menu de opciones
    sistema = SistemaAdministrador()# Se crea el objeto principal del sistema con listas de objetos clase clientes,servicios y reservas
    while True:#Bucle para mantener abierto el menu
        print("\n===== SoftwareFJ =====")#imprime el titulo de menu
        #Se imprimen las opsiones para ejecutar
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Mostrar servicios")
        print("4. Crear reserva")
        print("5. Cancelar reserva")
        print("6. Mostrar reservas")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")#Se guarda el numero ingresado en la variable
        if opcion == "7":#Si la opcion es 7 se cierra el menu
            print("Programa finalizado.")#Se imprime el mensaje de finalizado
            break#Para que el bucle se finalize
        elif opcion == "1":# Si la opción seleccionada es registrar 
            try:
                id_cliente = input("Ingrese el número de identificación: ")#Solicita el numero de documento y guarda en la variable
                nombre = input("Ingrese el nombre del cliente: ")#Solicita el nombre y guarda en la variable
                telefono = input("Ingrese el número telefónico: ")#Solicita el numero telefonico y guarda en la variable
                correo = input("Ingrese el correo electrónico: ")#Solicita el correo y guarda en la variable
                direccion = input("Ingrese la dirección: ")#Solicita la direccion y guarda en la variable
                edad = int(input("Ingrese la edad: "))#Solicita la y guarda en la variable como dato numerico
            
                sistema.registrar_cliente( # Envía los datos al método registrar_cliente()
                    id_cliente,
                    nombre,
                    telefono,
                    correo,
                    direccion,
                    edad
                    )
            except ValueError as error:#Cuando el tipo de dato no es correcto
                registrar_error(error)#captura el error y lo guar en el archivo logs

            except ErrorCliente as error:#Se ejecuta la exepcion perzonalizada cuando el error esta relacionado con el cliente
                registrar_error(error)#Ejecuta el metodo regitrar y guarda el error.
            finally:#Termina el registro aun cuando se presentan errores, pero no permite el registro exitoso si se presentan exepciones
                print("Finalizó el proceso de registro.")
            
        elif opcion == "2":# Si la opción seleccionada es la 2
            sistema.mostrar_clientes() # Llama al método que muestra todos los clientes registrados
        elif opcion == "3":# Si la opción seleccionada es la 3
            sistema.mostrar_servicios() # Llama al método que muestra todos los servicios disponibles
        elif opcion == "4":# Si la opción seleccionada es 4
            try:#Ecierra  el codigo para manejar los errores
               codigo_reserva = input("Ingrese el código de la reserva: ") # Se solicita el código de la reserva y se guarda en variable
               id_cliente = input("Ingrese la identificación del cliente: ") # Solicita la identificación del cliente  y se guarda en variable
               id_servicio = input("Ingrese el código del servicio: ")# Solicita el código del servicio y se guarda en variable
               fecha = input("Ingrese la fecha y hora ejm 01/11/2026 09:11")#Se solicita la hpra y fecha y se guarda en variable
               fecha_hora_inicio = datetime.strptime(# Convierte el texto ingresado a datetime y guarda el valor en variable
               fecha,#Datos proporcianados por el usuario
                "%d/%m/%Y %H:%M"#Indica el formato a transformar dia, mes, año, hora y minuto
               )
               duracion = int(#Se guarda en varible
                input("Ingrese la duración en horas: ")# Solicita la duración del servicio y se convierte en dato numerico
               )
               sistema.crear_reserva( # Llama al método crear_reserva()
                   codigo_reserva,
                   id_cliente,
                   id_servicio,
                   fecha_hora_inicio,
                   duracion
               )
            except ValueError as error:#Cuando el tipo de dato no es correcto
                registrar_error(error)#captura el error y lo guar en el archivo logs

            except ErrorCliente as error:#Se ejecuta la exepcion perzonalizada cuando el error esta relacionado con el cliente
                registrar_error(error)#Ejecuta el metodo regitrar y guarda el error.  

            except ErrorServicio as error:#Se ejecuta la exepcion perzonalizada cuando el error esta relacionado con el servicio
                registrar_error(error)#Ejecuta el metodo regitrar y guarda el error. 
    
            except ErrorReserva as error:#Se ejecuta la exepcion perzonalizada cuando el error esta relacionado con el servicio
                registrar_error(error)#Ejecuta el metodo regitrar y guarda el error.   
            finally:#Finaliza la reserva aun cuando se presentan errores, pero no permite la creacion de esta si se presentan exepciones
                print("Finalizó el proceso de reserva.")
            
        elif opcion == "5":# Si la opción seleccionada es cancelar es 5
            try:
                codigo_reserva = input(# Solicita el código de la reserva que se desea cancelar y se guarda en variable
                "Ingrese el código de la reserva a cancelar: "
                )
                sistema.cancelar_reserva(codigo_reserva) # Llama al método cancelar_reserva()
            except ValueError as error:#Cuando el tipo de dato no es correcto
                registrar_error(error)#captura el error y lo guar en el archivo logs
           
            
            except ErrorReserva as error:#Se ejecuta la exepcion perzonalizada cuando el error esta relacionado con el servicio
                registrar_error(error)#Ejecuta el metodo regitrar y guarda el error. 

            finally:#Finaliza la cancelación aun cuando se presentan errores, pero no permite la cancelacion de esta si se presentan exepciones
                print("Finalizó el proceso de cancelación.")
            
        elif opcion == "6":# Si la opción seleccionada es 6
            sistema.mostrar_reservas()  # Llama al método que muestra todas las reservas registradas
        else:  # Cuando se marca un opcion que no exite
            registrar_error("La opción seleccionada no es válida.")#Guarda el error ejecutando el metodo
menu()