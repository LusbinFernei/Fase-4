
from datetime import datetime
from datetime import timedelta#Se importa las libreria necesaria para faciclitar la operaciones de comparacion con las fechas y horas

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
print(menu())