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