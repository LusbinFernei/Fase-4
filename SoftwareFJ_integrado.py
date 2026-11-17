
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import logging

# Configuración del registro de errores

logging.basicConfig(
    filename="errores.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Excepciones personalizadas

class ErrorCliente(Exception):
    pass

class ErrorReserva(Exception):
    pass

class ErrorServicio(Exception):
    pass

# Funciones para el manejo de excepciones

def registrar_error(error):
    print(f"Se presentó un error: {error}")
    logging.error("%s", error)

def registrar_evento(mensaje):
    print(mensaje)
    logging.info("%s", mensaje)

def validar_dato(dato, nombre_campo):
    if dato is None or str(dato).strip() == "":
        raise ValueError(
            f"El campo {nombre_campo} no puede estar vacío."
        )

def ejecutar_con_manejo(operacion):
    try:
        resultado = operacion()
    except Exception as error:
        registrar_error(error)
    else:
        return resultado
    finally:
        print("Finalizó el proceso.")

def comprobar_encadenamiento():
    try:
        try:
            raise ValueError("Error inicial de validación.")
        except ValueError as error:
            raise ErrorCliente(
                "No fue posible completar la operación."
            ) from error
    except ErrorCliente as error:
        registrar_error(error)

# Clase base Entidad

class Entidad(ABC):

    def __init__(self, identificacion, nombre):
        validar_dato(identificacion, "identificación")
        validar_dato(nombre, "nombre")

        self._id = identificacion
        self._nombre = nombre

    def obtener_id(self):
        return self._id

    def obtener_nombre(self):
        return self._nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Clase Cliente

class Cliente(Entidad):

    def __init__(
        self,
        identificacion,
        nombre,
        telefono,
        correo,
        direccion,
        edad
    ):
        super().__init__(identificacion, nombre)

        validar_dato(telefono, "teléfono")
        validar_dato(correo, "correo electrónico")
        validar_dato(direccion, "dirección")

        if edad < 18:
            raise ErrorCliente(
                "El cliente debe ser mayor de edad."
            )

        if "@" not in correo:
            raise ErrorCliente(
                "El correo electrónico no es válido."
            )

        if len(str(telefono)) < 7:
            raise ErrorCliente(
                "El teléfono debe tener al menos 7 dígitos."
            )

        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Identificación: {self._id}")
        print(f"Nombre: {self._nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Dirección: {self.direccion}")
        print(f"Edad: {self.edad}")

# Clase base Servicio

class Servicio(Entidad, ABC):

    def __init__(self, codigo, nombre, precio):
        super().__init__(codigo, nombre)

        if precio <= 0:
            raise ErrorServicio(
                "El precio del servicio debe ser mayor que cero."
            )

        self.precio = precio

    @abstractmethod
    def calcular_costo(self, duracion=1):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    def mostrar_informacion(self):
        print(f"Código: {self._id}")
        print(f"Servicio: {self._nombre}")
        print(f"Precio: ${self.precio:,.0f}")
        print(self.describir_servicio())

# Clase ReservaSala

class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, precio, capacidad):
        super().__init__(codigo, nombre, precio)

        if capacidad <= 0:
            raise ErrorServicio(
                "La capacidad debe ser mayor que cero."
            )

        self.capacidad = capacidad

    def calcular_costo(self, duracion=1):
        return self.precio * duracion

    def describir_servicio(self):
        return f"Capacidad de la sala: {self.capacidad} personas."

    def validar_parametros(self):
        return self.precio > 0 and self.capacidad > 0

# Clase AlquilerEquipo

class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio, tipo_equipo):
        super().__init__(codigo, nombre, precio)

        validar_dato(tipo_equipo, "tipo de equipo")
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion=1):
        return self.precio * duracion

    def describir_servicio(self):
        return f"Tipo de equipo: {self.tipo_equipo}."

    def validar_parametros(self):
        return self.precio > 0 and bool(self.tipo_equipo)

# Clase AsesoriaEspecializada

class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio, especialidad):
        super().__init__(codigo, nombre, precio)

        validar_dato(especialidad, "especialidad")
        self.especialidad = especialidad

    def calcular_costo(self, duracion=1):
        return self.precio * duracion

    def describir_servicio(self):
        return f"Especialidad: {self.especialidad}."

    def validar_parametros(self):
        return self.precio > 0 and bool(self.especialidad)

# Clase Reserva

class Reserva:

    def __init__(
        self,
        codigo,
        cliente,
        servicio,
        fecha_inicio,
        fecha_fin
    ):
        validar_dato(codigo, "código de reserva")

        if fecha_fin <= fecha_inicio:
            raise ErrorReserva(
                "La fecha final debe ser posterior a la fecha inicial."
            )

        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "Activa"

    def calcular_duracion(self):
        duracion = self.fecha_fin - self.fecha_inicio
        return duracion.total_seconds() / 3600

    def calcular_total(self):
        return self.servicio.calcular_costo(
            self.calcular_duracion()
        )

    def mostrar_informacion(self):
        print(f"Código de reserva: {self.codigo}")
        print(f"Cliente: {self.cliente.obtener_nombre()}")
        print(f"Servicio: {self.servicio.obtener_nombre()}")
        print(
            "Fecha inicial:",
            self.fecha_inicio.strftime("%d/%m/%Y %H:%M")
        )
        print(
            "Fecha final:",
            self.fecha_fin.strftime("%d/%m/%Y %H:%M")
        )
        print(f"Duración: {self.calcular_duracion():.2f} horas")
        print(f"Valor total: ${self.calcular_total():,.0f}")
        print(f"Estado: {self.estado}")

# Clase SistemaAdministrador

class SistemaAdministrador:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.cargar_servicios()

    def cargar_servicios(self):

        self.servicios.append(
            ReservaSala("RS001", "Sala Pequeña", 399900, 50)
        )
        self.servicios.append(
            ReservaSala("RS002", "Sala Mediana", 699900, 100)
        )
        self.servicios.append(
            ReservaSala("RS003", "Sala Grande", 999900, 150)
        )

        self.servicios.append(
            AsesoriaEspecializada(
                "AE001", "Asesoría Jurídica", 100000, "Jurídica"
            )
        )
        self.servicios.append(
            AsesoriaEspecializada(
                "AE002", "Asesoría Tributaria", 150000, "Tributaria"
            )
        )
        self.servicios.append(
            AsesoriaEspecializada(
                "AE003", "Asesoría Financiera", 100000, "Financiera"
            )
        )
        self.servicios.append(
            AsesoriaEspecializada(
                "AE004", "Asesoría Marketing", 120000, "Marketing"
            )
        )
        self.servicios.append(
            AsesoriaEspecializada(
                "AE005", "Asesoría Tecnológica", 160000, "Tecnológica"
            )
        )

        self.servicios.append(
            AlquilerEquipo(
                "EQ001", "Equipo de Sonido", 29900, "Sonido"
            )
        )
        self.servicios.append(
            AlquilerEquipo(
                "EQ002", "Equipo Audiovisual", 59900, "Audiovisual"
            )
        )
        self.servicios.append(
            AlquilerEquipo(
                "EQ003", "Equipo de Construcción", 39900, "Construcción"
            )
        )

    def buscar_cliente(self, identificacion):
        for cliente in self.clientes:
            if cliente.obtener_id() == identificacion:
                return cliente
        return None

    def buscar_servicio(self, codigo):
        for servicio in self.servicios:
            if servicio.obtener_id() == codigo:
                return servicio
        return None

    def buscar_reserva(self, codigo):
        for reserva in self.reservas:
            if reserva.codigo == codigo:
                return reserva
        return None

    def registrar_cliente(
        self,
        identificacion,
        nombre,
        telefono,
        correo,
        direccion,
        edad
    ):
        try:
            if self.buscar_cliente(identificacion):
                raise ErrorCliente(
                    "Ya existe un cliente con esa identificación."
                )

            nuevo_cliente = Cliente(
                identificacion,
                nombre,
                telefono,
                correo,
                direccion,
                edad
            )

            self.clientes.append(nuevo_cliente)

            registrar_evento(
                "Cliente registrado correctamente."
            )

        except (ValueError, ErrorCliente) as error:
            registrar_error(error)

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print("\nLISTA DE CLIENTES")

        for cliente in self.clientes:
            print()
            cliente.mostrar_informacion()

    def mostrar_servicios(self):
        print("\nLISTA DE SERVICIOS")

        for servicio in self.servicios:
            print()
            servicio.mostrar_informacion()

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return

        print("\nLISTA DE RESERVAS")

        for reserva in self.reservas:
            print()
            reserva.mostrar_informacion()

    def crear_reserva(
        self,
        codigo,
        identificacion_cliente,
        codigo_servicio,
        fecha_inicio,
        fecha_fin
    ):
        try:
            if self.buscar_reserva(codigo):
                raise ErrorReserva(
                    "Ya existe una reserva con ese código."
                )

            cliente = self.buscar_cliente(identificacion_cliente)

            if cliente is None:
                raise ErrorCliente(
                    "El cliente no se encuentra registrado."
                )

            servicio = self.buscar_servicio(codigo_servicio)

            if servicio is None:
                raise ErrorServicio(
                    "El servicio seleccionado no existe."
                )

            if fecha_fin <= fecha_inicio:
                raise ErrorReserva(
                    "La fecha final debe ser posterior a la inicial."
                )

            for reserva in self.reservas:
                if reserva.estado == "Activa":
                    if reserva.servicio.obtener_id() == codigo_servicio:
                        if (
                            fecha_inicio < reserva.fecha_fin
                            and fecha_fin > reserva.fecha_inicio
                        ):
                            raise ErrorReserva(
                                "El servicio ya tiene una reserva "
                                "en ese horario."
                            )

            nueva_reserva = Reserva(
                codigo,
                cliente,
                servicio,
                fecha_inicio,
                fecha_fin
            )

            self.reservas.append(nueva_reserva)

            registrar_evento(
                "Reserva creada correctamente."
            )

            print(
                f"Valor total de la reserva: "
                f"${nueva_reserva.calcular_total():,.0f}"
            )

        except (ValueError, ErrorCliente, ErrorServicio, ErrorReserva) as error:
            registrar_error(error)

    def cancelar_reserva(self, codigo):
        try:
            reserva = self.buscar_reserva(codigo)

            if reserva is None:
                raise ErrorReserva(
                    "No se encontró la reserva indicada."
                )

            if reserva.estado == "Cancelada":
                raise ErrorReserva(
                    "La reserva ya se encuentra cancelada."
                )

            reserva.estado = "Cancelada"

            registrar_evento(
                "Reserva cancelada correctamente."
            )

        except ErrorReserva as error:
            registrar_error(error)

# Funciones para solicitar datos

def solicitar_fecha(mensaje):
    fecha_texto = input(mensaje)

    try:
        return datetime.strptime(
            fecha_texto,
            "%d/%m/%Y %H:%M"
        )
    except ValueError as error:
        raise ValueError(
            "Formato incorrecto. Use DD/MM/AAAA HH:MM."
        ) from error

def solicitar_edad():
    try:
        edad = int(input("Ingrese la edad del cliente: "))

        if edad < 18:
            raise ErrorCliente(
                "El cliente debe ser mayor de edad."
            )

        return edad

    except ValueError as error:
        raise ValueError(
            "La edad debe ser un número entero."
        ) from error

# Menú principal

def menu():

    sistema = SistemaAdministrador()

    while True:

        print("\nSISTEMA DE ADMINISTRACIÓN SOFTWARE FJ")
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Mostrar servicios")
        print("4. Crear reserva")
        print("5. Mostrar reservas")
        print("6. Cancelar reserva")
        print("7. Probar encadenamiento de excepciones")
        print("8. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:

                identificacion = input(
                    "Ingrese la identificación: "
                )
                nombre = input("Ingrese el nombre: ")
                telefono = input("Ingrese el teléfono: ")
                correo = input("Ingrese el correo electrónico: ")
                direccion = input("Ingrese la dirección: ")
                edad = solicitar_edad()

                sistema.registrar_cliente(
                    identificacion,
                    nombre,
                    telefono,
                    correo,
                    direccion,
                    edad
                )

            elif opcion == 2:
                sistema.mostrar_clientes()

            elif opcion == 3:
                sistema.mostrar_servicios()

            elif opcion == 4:

                codigo = input("Ingrese el código de reserva: ")
                identificacion = input(
                    "Ingrese la identificación del cliente: "
                )
                codigo_servicio = input(
                    "Ingrese el código del servicio: "
                )

                fecha_inicio = solicitar_fecha(
                    "Ingrese la fecha inicial (DD/MM/AAAA HH:MM): "
                )

                fecha_fin = solicitar_fecha(
                    "Ingrese la fecha final (DD/MM/AAAA HH:MM): "
                )

                sistema.crear_reserva(
                    codigo,
                    identificacion,
                    codigo_servicio,
                    fecha_inicio,
                    fecha_fin
                )

            elif opcion == 5:
                sistema.mostrar_reservas()

            elif opcion == 6:

                codigo = input(
                    "Ingrese el código de la reserva que desea cancelar: "
                )

                sistema.cancelar_reserva(codigo)

            elif opcion == 7:
                comprobar_encadenamiento()

            elif opcion == 8:
                print("Gracias por utilizar SoftwareFJ.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as error:
            registrar_error(error)

        except ErrorCliente as error:
            registrar_error(error)

        except ErrorReserva as error:
            registrar_error(error)

        except ErrorServicio as error:
            registrar_error(error)

        except Exception as error:
            registrar_error(error)

# Inicio del programa

if __name__ == "__main__":
    try:
        menu()
    except Exception as error:
        registrar_error(error)
        print("El programa finalizó debido a un error.")