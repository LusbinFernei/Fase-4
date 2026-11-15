"""
Aqui esta mi parte del proyecto, en este archivo se encuentran las clases y funciones para el alquiler de equipos y asesorías especializadas.
"""
# Tarifas (de prueba) y clase para alquiler de equipos.
TARIFAS_EQUIPOS = {
    "Sonido": 29900,
    "Audiovisual": 59900,
    "Construccion": 39900
    }

def obtener_tarifa_equipo(tipo_equipo):
    
    tarifa = TARIFAS_EQUIPOS.get(tipo_equipo)
    
    if tipo_equipo not in TARIFAS_EQUIPOS:
            raise KeyError("Tipo de equipo no definido")

    return tarifa

# Representa el servicio de alquiler de equipos.
class AlquilerEquipo:
    # Inicializa el equipo y verifica que su tarifa sea coherente.
    def __init__(self, id, nombre, tipo_equipo, costo_base, disponible=True):
        self.id = id
        self.nombre = nombre
        self.tipo_equipo = tipo_equipo
        tarifa_calculada = obtener_tarifa_equipo(tipo_equipo)

        if costo_base != tarifa_calculada:
            raise ValueError("El costo base no coincide con el tipo de equipo")

        self.costo_base = costo_base
        self.disponible = disponible
        self.costo_base_hora = tarifa_calculada
    
    # Calcula el costo del alquiler según la cantidad de horas.
    def calcular_costo(self, horas):
        if not isinstance(horas, (int, float)):
            raise TypeError("Las horas deben ser un número")

        if horas <= 0:
            raise ValueError("El número de horas debe ser mayor que cero")

        return self.costo_base_hora * horas

    # Verifica que el equipo esté disponible para alquilarse.
    def validar_parametros(self):
        if not self.disponible:
            raise ValueError("El equipo no está disponible para alquiler")
        return True

    # Devuelve una descripción del servicio y su tarifa.
    def describir_servicio(self):
        return f"Alquiler de equipo {self.tipo_equipo} a ${self.costo_base_hora} por hora."
    
    # Muestra la información principal del equipo.
    def mostrar_informacion(self):
        print(f"Tipo de equipo: {self.tipo_equipo}")
        print(f"Disponible: {self.disponible}")
        print(f"Costo por hora: ${self.costo_base_hora}")
        print(self.describir_servicio())

"""Tarifas (de prueba) y clase para asesorías especializadas."""
TARIFAS_ASESORIAS = {
"Juridica": 100000,
"Tributaria": 150000,
"Financiera": 100000,
"Marketing": 120000,
"Tecnologica": 160000,
}

def obtener_tarifa_asesoria(tipo_asesoria):

    tarifa = TARIFAS_ASESORIAS.get(tipo_asesoria)
    
    if tipo_asesoria not in TARIFAS_ASESORIAS:
        raise KeyError("Tipo de asesoría no definido")

    return tarifa

# Representa el servicio de asesoría especializada.
class AsesoriaEspecializada:
    # Inicializa la asesoría y verifica que su tarifa sea coherente.
    def __init__(self, id, nombre, tipo_asesoria, costo_base, disponible=True):
        self.id = id
        self.nombre = nombre
        self.tipo_asesoria = tipo_asesoria
        
        tarifa_calculada = obtener_tarifa_asesoria(tipo_asesoria)

        if costo_base != tarifa_calculada:
            raise ValueError("El costo base no coincide con el tipo de asesoría")

        self.costo_base = costo_base
        self.disponible = disponible
        self.costo_base_hora = tarifa_calculada

    # Calcula el costo de la asesoría según la cantidad de horas.
    def calcular_costo(self, horas):
        if not isinstance(horas, (int, float)):
            raise TypeError("Las horas deben ser un número")

        if horas <= 0:
            raise ValueError("El número de horas debe ser mayor que cero")

        return self.costo_base_hora * horas
    # Verifica que la asesoría esté disponible.
    def validar_parametros(self):
        if not self.disponible:
            raise ValueError("La asesoría no está disponible")
        return True
    # Devuelve una descripción del servicio y su tarifa.
    def describir_servicio(self):
        return f"Asesoría especializada en {self.tipo_asesoria} a ${self.costo_base_hora} por hora."
    # Muestra la información principal de la asesoría.
    def mostrar_informacion(self):
        print(f"Tipo de asesoría: {self.tipo_asesoria}")
        print(f"Disponible: {self.disponible}")
        print(f"Costo por hora: ${self.costo_base_hora}")
        print(self.describir_servicio())