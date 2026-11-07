#Estudiantes: ANDREA LIZARAZO PRADA_LUSBIN FERNEI BARAJAS CABALLERO_MAVERIK ANDRES CALDERON URIBE_OSCAR GOMEZ ARENAS_JOJHAN DAVID LIZARAZO RIOS
#Grupo: 230
#Programa: Ingenieria de sitemas
#Codigo fuente: autoria propia

#Inicio del programa  
  
#Programa Software FJ

class  SistemaAdministrador:#Se cre la clase que administrara los datos recividos

    def __init__(self):#Se define el meotodo constructor
        #Atributos del metodo constructor
        self.clientes = []#Se crea la lista que alamacenara los objetos  clientes
        self.servicios = []#Se crea la lista que alamacenara los objetos  seervicios
        self.reservas = []#Se crea la lista que almacenara los objetos reservas