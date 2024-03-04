#definir clase paciente
class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self,cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return None
        
    def ingresarPaciente(self,pac):
         # Primero verifica que el paciente no exista antes de añadirlo
        if self.verificarPaciente(pac.verCedula) == True:
            return None
        else:
            self.__lista_pacientes.append(pac)
            return True
    
    def verDatosPaciente(self, c):
        if self.verificarPaciente(c) == False:
            return None
        for p in self.__lista_pacientes:
            #retorne la cedula y la comparo con la ingresada por teclado
            if c == p.verCedula():
                return p #si encuentro el paciente lo retorno
            
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

    # Creamos un metodo dentro de la clase para poder acceder a la lista de pacientes
        def verLista(self):
            lista = self.__lista_pacientes
            return lista
        
def main():
    sis = Sistema() 
        # lineas usadas para la prueba de la busqueda por nombre
    # pena = Paciente()
    # pena.asignarNombre("Juan Esteban Pena ")
    # pena.asignarCedula(1085902252)
    # pena.asignarGenero("M")
    # pena.asignarServicio("s")
    # sis.ingresarPaciente(pena)

    # pena = Paciente()
    # pena.asignarNombre("Juan Pena ")
    # pena.asignarCedula(1085902257)
    # pena.asignarGenero("M")
    # pena.asignarServicio("s")
    # sis.ingresarPaciente(pena)
    
    # tban = Paciente()
    # tban.asignarNombre("Esteban Daniel Pena Rojas")
    # tban.asignarCedula(1085902256)
    # tban.asignarGenero("M")
    # tban.asignarServicio("s")
    # sis.ingresarPaciente(tban
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            opcion = int(input("\nDigite \n0 para salir, \n1 para ingresar nuevo paciente, \n2 para ver un paciente\n\t--> "))
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 




        #ver pacientes 
        elif opcion == 2:
                        # creamos un bucle para la selección de opciones del sub-menú ver paciente
            while True:
                opcion = int(input("\nSeleccione el tipo de busqueda \n0 Para cancelar busqueda, \n1 Para busqueda por cedula, \n2 Para busqueda por nombre\n\t--> "))
                    # Busqueda por cedula
                if opcion==1:
                    #1. solicito la cedula que quiero buscar
                    c = int(input("Ingrese la cedula a buscar: ")) 
                    #le pido al sistema que me devuelva en la variable p al paciente que tenga
                    #la cedula c en la lista
                    p = sis.verDatosPaciente(c) 
                    #2. si encuentro al paciente imprimo los datos
                    if p != None:
                        print("Nombre: " + p.verNombre()) 
                        print("Cedula: " + str(p.verCedula())) 
                        print("Genero: " + p.verGenero()) 
                        print("Servicio: " + p.verServicio()) 
                    else:
                        print("No existe un paciente con esa cedula") 
                # Busqueda por nombre
                elif opcion==2:


                    
                    nombre = str(input("Ingrese el nombre del paciente: ")) #1. solicito el nombre que quiero buscar
                    nombres_separados = nombre_para_busqueda(nombre)        #Creo una lista iterable de los nombres del paciente
                    lista = sis.verLista()                                  #Asigno a "lista" la lista de pacientes del Sistema
                    lista_coincidencias = []                                #Creo una lista vacia para guardar las coincidencias del nombre

                    for nombre_I in nombres_separados:                                  #itearamos sobre cada nombre ingresado
                        for objeto in lista:                                            #iteramos para cada nombre sobre los objetos de la lista de pacientes
                            nombre_C_lista = nombre_para_busqueda(objeto.verNombre())   #convertimos el nombre de cada paciente en una lista iterable "nombre_C_lista"
                            for nombre_C in nombre_C_lista:                             #iteramos cada nombres de la lista de pacientes 
                                if nombre_I == nombre_C:                                #comparamos para identificar una coincidencia en alguno de los nombres o apellidos
                                    if objeto not in lista_coincidencias:               #verificamos que no se haya encontrado aún
                                        lista_coincidencias.append(objeto)              #en caso de ser una coincidencia nueva, se añade a la lista
                                        break                                           #break para dejar de iterar sobre los nombres del paciente tras añadirlo y pasar al siguiente

                    print(f"Se encontró(aron) {len(lista_coincidencias)} coincidencia(s)")   #se informa la cantidad de pacientes con coincidencia en el nombre consultado

                    for p in lista_coincidencias:                                       #se muestra la informacion de cada paciente encontradod

                        print("Nombre: " + p.verNombre()) 
                        print("Cedula: " + str(p.verCedula())) 
                        print("Genero: " + p.verGenero()) 
                        print("Servicio: " + p.verServicio() +"\n") 


                elif opcion!=0:
                    continue
                else:
                    break

        elif opcion !=0:
            continue 
        else:
            break 

def nombre_para_busqueda(nombre):       #creamos una funcion nueva para transformar un string a una lista separando 
    nombre_normal = nombre.lower()      #normalizamos la cadena a minusculas
    lista = nombre_normal.split()       #separamos la cadena por espacios y se asigna a una lista
    return lista                        #se retorna la lista


#aca el python descubre cual es la funcion principal
if _name_ == "main":
    main()