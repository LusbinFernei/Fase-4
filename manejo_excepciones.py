
# Importa el módulo logging para registrar errores y eventos.
import logging

# Configura el archivo donde se guardarán los registros del sistema.
logging.basicConfig(
    filename="errores.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Define una excepción personalizada para errores de clientes.
class ErrorCliente(Exception):
    pass


# Define una excepción personalizada para errores de reservas.
class ErrorReserva(Exception):
    pass


# Define una excepción personalizada para errores de servicios.
class ErrorServicio(Exception):
    pass


# Define una función para mostrar y registrar los errores.
def registrar_error(error):
    # Muestra el error en la terminal.
    print(f"Se presentó un error: {error}")

    # Guarda el error en el archivo de registros.
    logging.error("%s", error)


# Define una función para registrar eventos importantes.
def registrar_evento(mensaje):
    # Muestra el evento en la terminal.
    print(f"Evento del sistema: {mensaje}")

    # Guarda el evento en el archivo de registros.
    logging.info("%s", mensaje)


# Define una función para validar que un dato no esté vacío.
def validar_dato(dato, nombre_campo):
    # Comprueba si el dato está vacío o contiene espacios.
    if not dato or not str(dato).strip():

        # Genera una excepción si el campo está vacío.
        raise ValueError(
            f"El campo {nombre_campo} no puede estar vacío."
        )

    # Retorna el dato cuando supera la validación.
    return dato


# Define una función para ejecutar operaciones controlando errores.
def ejecutar_con_manejo(operacion):
    # Intenta ejecutar la operación recibida.
    try:
        # Ejecuta la operación y guarda su resultado.
        resultado = operacion()

    # Captura cualquier error producido durante la operación.
    except Exception as error:
        # Registra el error ocurrido.
        registrar_error(error)

        # Retorna None cuando la operación falla.
        return None

    # Se ejecuta cuando no ocurre ningún error.
    else:
        # Retorna el resultado de la operación.
        return resultado

    # Se ejecuta siempre, haya error o no.
    finally:
        # Informa que terminó el proceso.
        print("Finalizó el proceso.")


# Define una función que demuestra el encadenamiento de excepciones.
def comprobar_encadenamiento():
    # Intenta convertir un texto en un número.
    try:
        # Esta conversión genera un ValueError.
        int("texto incorrecto")

    # Captura el error original.
    except ValueError as error:
        # Genera una excepción personalizada conservando la causa original.
        raise ErrorCliente(
            "No fue posible procesar los datos del cliente."
        ) from error


# Define las pruebas para comprobar el funcionamiento del módulo.
def ejecutar_pruebas():
    # Registra un evento de inicio de las pruebas.
    registrar_evento("Inicio de las pruebas del módulo.")

    # Prueba la validación de un campo vacío.
    try:
        # Intenta validar un nombre vacío.
        validar_dato("", "Nombre del cliente")

    # Captura el error de validación.
    except ValueError as error:
        # Registra el error encontrado.
        registrar_error(error)

    # Prueba la excepción personalizada para clientes.
    try:
        # Genera un error de cliente.
        raise ErrorCliente("No se pudo registrar el cliente.")

    # Captura el error del cliente.
    except ErrorCliente as error:
        # Registra el error.
        registrar_error(error)

    # Prueba la excepción personalizada para reservas.
    try:
        # Genera un error de reserva.
        raise ErrorReserva("No se pudo generar la reserva.")

    # Captura el error de la reserva.
    except ErrorReserva as error:
        # Registra el error.
        registrar_error(error)

    # Prueba la excepción personalizada para servicios.
    try:
        # Genera un error de servicio.
        raise ErrorServicio("El servicio no está disponible.")

    # Captura el error del servicio.
    except ErrorServicio as error:
        # Registra el error.
        registrar_error(error)

    # Prueba el encadenamiento de excepciones.
    try:
        # Ejecuta la función que genera el encadenamiento.
        comprobar_encadenamiento()

    # Captura la excepción personalizada.
    except ErrorCliente as error:
        # Registra el error y su causa original.
        registrar_error(error)
        registrar_error(f"Causa original: {error.__cause__}")

    # Define una función de prueba que produce un error.
    def prueba_operacion():
        # Intenta convertir un texto incorrecto en número.
        return int("texto incorrecto")

    # Ejecuta la operación mediante el control de excepciones.
    ejecutar_con_manejo(prueba_operacion)

    # Registra que las pruebas han terminado.
    registrar_evento("Finalización de las pruebas del módulo.")


# Ejecuta las pruebas solamente cuando se abre este archivo directamente.
if __name__ == "__main__":
    # Llama a la función que contiene las pruebas.
    ejecutar_pruebas()
