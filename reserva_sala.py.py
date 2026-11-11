
# Importamos la clase Servicio desde el archivo servicio.py.
# ReservaSala hereda los atributos y metodos de esta clase.
from servicio import Servicio


# --------------------------------------------------
# CLASE RESERVASALA
# --------------------------------------------------
# Creamos la clase ReservaSala.
# Hereda de Servicio y tambien recibe los atributos
# _id y _nombre de la clase Entidad.

class ReservaSala(Servicio):

# --------------------------------------------------
# METODO CONSTRUCTOR
# --------------------------------------------------
# Recibe el identificador, el nombre de la sala,
# la tarifa por hora y la capacidad de personas.

    def __init__(self, id, nombre, tarifa_hora, capacidad):

# Llamamos al constructor de la clase padre Servicio.
# Este envia el id y el nombre a la clase Entidad.
        super().__init__(id, nombre)

# Guardamos la tarifa por cada hora de servicio.
        self.tarifa_hora = tarifa_hora

# Guardamos la capacidad maxima de personas de la sala.
        self.capacidad = capacidad

# Validamos los datos recibidos.
        self.validar_parametros()

# --------------------------------------------------
# METODO PARA VALIDAR LOS PARAMETROS
# --------------------------------------------------
# Verifica que la tarifa y la capacidad sean correctas.

    def validar_parametros(self):

# Comprobamos que la tarifa sea un numero.
        if isinstance(self.tarifa_hora, bool) or not isinstance(self.tarifa_hora, (int, float)):
            raise ValueError("La tarifa por hora debe ser numerica.")

# La tarifa debe ser mayor que cero.
        if self.tarifa_hora <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

# Comprobamos que la capacidad sea un numero entero.
        if isinstance(self.capacidad, bool) or not isinstance(self.capacidad, int):
            raise ValueError("La capacidad debe ser un numero entero.")

# La capacidad debe ser mayor que cero.
        if self.capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")

        return True

# --------------------------------------------------
# METODO PARA CALCULAR EL COSTO
# --------------------------------------------------
# Multiplica la tarifa por la cantidad de horas.

    def calcular_costo(self, duracion):

# Comprobamos que la duracion sea numerica.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duracion debe ser numerica.")

# La duracion debe ser mayor que cero.
        if duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

# Calculamos el costo total del servicio.
        costo = self.tarifa_hora * duracion

        return costo

# --------------------------------------------------
# METODO PARA DESCRIBIR EL SERVICIO
# --------------------------------------------------
# Retorna una descripcion de la sala.

    def describir_servicio(self):

        descripcion = (
            f"Servicio de reserva de sala: {self.obtener_nombre()}. "
            f"Capacidad: {self.capacidad} personas."
        )

        return descripcion

# --------------------------------------------------
# METODO PARA MOSTRAR INFORMACION
# --------------------------------------------------
# Presenta los datos principales de la sala.

    def mostrar_informacion(self):

        print("\n===== INFORMACION DE LA SALA =====")
        print(f"Codigo: {self.obtener_id()}")
        print(f"Nombre: {self.obtener_nombre()}")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"Tarifa por hora: ${self.tarifa_hora:,.2f}")
        print(self.describir_servicio())
