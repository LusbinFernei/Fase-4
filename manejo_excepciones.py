
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