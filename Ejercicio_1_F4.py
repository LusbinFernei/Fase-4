#Estudiantes: ANDREA LIZARAZO PRADA_LUSBIN FERNEI BARAJAS CABALLERO_MAVERIK ANDRES CALDERON URIBE_OSCAR GOMEZ ARENAS_JOJHAN DAVID LIZARAZO RIOS
#Grupo: 230
#Programa: Ingenieria de sitemas
#Codigo fuente: autoria propia

#Inicio del programa  
  
#Programa Software FJ
from datetime import timedelta#Se importa la libreria necesaria para faciclitar la operaciones de comparacion

class  SistemaAdministrador:#Se cre la clase que administrara los datos recividos

    def __init__(self):#Se define el meotodo constructor
        #Atributos del metodo constructor
        self.clientes = []#Se crea la lista que alamacenara los objetos  clientes
        self.servicios = []#Se crea la lista que alamacenara los objetos  seervicios
        self.reservas = []#Se crea la lista que almacenara los objetos reservas

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
        cliente_ya_registrado = self.buscar_cliente(id_cliente) # Busca si ya existe un cliente con ese número de identificación y lo guarda en la variable 
        if cliente_ya_registrado is not None:# Si el resultado de buscar_cliente es diferente a None el cliente ya esta registra
            print("El cliente ya se encuentra registrado.") # Muestra un mensaje informando que ya existe
        else:#En caso contrario
            nuevo_cliente = Cliente(#Crea el cliente con el metodo constructor de la clase Cliente
            id_cliente,#Numero de cedula
            nombre,#Nombre de la persona
            telefono,#Numero celular
            correo,#Correo personal
            direccion,#Direccion de residencia
            edad#Edad
        )
        self.clientes.append(nuevo_cliente)# Agrega el nuevo cliente en la lista de clientes
        print("Cliente registrado exitosamente.") #Imprime el mensaje confirmando el registro exitoso del cliente en la varible clientes

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
        cliente = self.buscar_cliente(id_cliente)# Busca el cliente utilizando el numero de identificación ingresado
        servicio = self.buscar_servicio(id_servicio)#Busca el codigo del servicio
        if cliente is None: # Si el cliente no esta registrado
            print("El cliente no se encuentra registrado.")#Imprime el siguiente mensaje
        elif servicio is None:#Si el codigo de servico no existe
            print("El servicio no se encuentra registrado.")#Imprime el siguiente mensaje
        else:# Si el cliente y el servicio estan registrados se continua con la reserva
            fecha_hora_fin = fecha_hora_inicio + timedelta(hours=duracion)# Calcula la fecha y hora de finalización de la nueva reserva
            for reserva in self.reservas:#Recorre las reservas existentes
                if reserva.servicio.obtener_id() == id_servicio:  # Verifica que la reserva no se esta haciendo sobre el mismo tipo de servicio y a la misma hora
                    inicio_existente = reserva.fecha_hora_inicio #Si existe una reserva con el ingresa obtine la hora de inicio y la guarda el dato en la varible
                fin_existente = (#Variable para guarda la hora y fecha donde termina el serivico ya existente
                    reserva.fecha_hora_inicio +#se toma la hora de inicio
                    timedelta(hours=reserva.duracion)#Se suma con el tiempo de duracion, calculando asi la hora de terminacion del servicio
                ) 
                if (fecha_hora_inicio < fin_existente and#Compara la hora de incio del nuevo servicio con la hora de terminacion del servicio en curso
                    fecha_hora_fin > inicio_existente):#Compara la hora de terminacion del nuevo servicio y la hora de inicio del servicio en curso
                    print("El servicio ya se encuentra reservado en ese horario.")#Si amnbas condiciones se cumplen se imprime el siguiente mensaje
                    return#Termina de ejecutarse el metodo por conflicto de horarios
                nueva_reserva = Reserva(#Si la condicion no se cumple se crea el objeto Reserva y se guarda en la varible utilizando el metodo constructor de la clase Reserva
                    codigo_reserva, #Codigo de la reserva
                    cliente,#Cliente
                    servicio,#Tipo de servicio
                    fecha_hora_inicio,#Fecha y hora de inicio
                    duracion,#Duracion en horas
                    "Confirmada"#Estado de la reserva
                   )
                self.reservas.append(nueva_reserva)# Guarda la reserva en la lista
                print("Reserva creada exitosamente.") # Confirma la creación de la reserva
    def cancelar_reserva(self, codigo_reserva):#Metodo para cancelar la reserva
        reserva = self.buscar_reserva(codigo_reserva)# Busca la reserva por su código
        if reserva is None:#Si la reserva no exite
            print("La reserva no se encuentra registrada.")#Imprime el siguiente mensaje
        else:#Si la reserva exite
            reserva.cancelar()# Llama al método cancelar de la clase Reserva
            print("Reserva cancelada exitosamente.")#Imprime el siguiente mensaje
