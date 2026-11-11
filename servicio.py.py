
# Importamos abstractmethod para definir los metodos abstractos.
from abc import abstractmethod

from entidad import Entidad


# --------------------------------------------------
# CLASE SERVICIO
# --------------------------------------------------
# Creamos la clase Servicio.
# Hereda de Entidad para recibir sus atributos y metodos.
# Es abstracta porque contiene metodos que deben implementar
# las clases que hereden de ella.

class Servicio(Entidad):

# --------------------------------------------------
# METODO CONSTRUCTOR
# --------------------------------------------------
# Recibe el identificador y el nombre del servicio.
# Estos datos se envian a la clase padre Entidad.

    def __init__(self, id, nombre):

# Llamamos al constructor de la clase padre.
# Asi reutilizamos los atributos _id y _nombre.
        super().__init__(id, nombre)

# --------------------------------------------------
# METODO ABSTRACTO: CALCULAR COSTO
# --------------------------------------------------
# Obliga a las clases hijas a definir como calcular
# el costo de cada tipo de servicio.

    @abstractmethod
    def calcular_costo(self):
        pass

# --------------------------------------------------
# METODO ABSTRACTO: DESCRIBIR SERVICIO
# --------------------------------------------------
# Obliga a las clases hijas a explicar en que consiste
# el servicio que ofrecen.

    @abstractmethod
    def describir_servicio(self):
        pass

# --------------------------------------------------
# METODO ABSTRACTO: VALIDAR PARAMETROS
# --------------------------------------------------
# Obliga a las clases hijas a comprobar que los datos
# necesarios para cada servicio sean correctos.

    @abstractmethod
    def validar_parametros(self):
        pass

# --------------------------------------------------
# METODO ABSTRACTO: MOSTRAR INFORMACION
# --------------------------------------------------
# Obliga a cada clase hija a mostrar la informacion
# correspondiente a su tipo de servicio.

    @abstractmethod
    def mostrar_informacion(self):
        pass


