import random #Importe de libreria random para randomizar la creación de ramos de flores 
import time #Importe de libreria time para ralentizar la ejecución del script
import limpiador as c #Importe de archivo limpiaodor.py para limpiar las secuencias del script que fueron ejecutadas


class Flor: #Se crea la clase flor
    def __init__(self): #Se crea el método init con atributos definidos mas abajo:
        texto_flor = 'abcdefghijklmnopqrstuvwxyz' #tipos de flores asociadas a una letra de diccionario
        self.lista_flores = list(texto_flor) #la lista de flores disponibles se almacena en una lista "texto flor"
        self.tamanios = ['S', 'L'] #solo existiran dos tamaños de flor: S y L


class Ramo: #se crea la clase ramo
    def __init__(self): #creación método init 
        texto_ramo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #diccionario en mayuscula para diferenciarlo del diccionario que almacena la lista de flores
        self.nombre_ramo = list(texto_ramo) #lista que almacenará los ramos fabricados
        self.tamano_ramo = ['S', 'L'] #tamaños disponibles de ramo: S y L


class PlantaProduccion(Flor, Ramo): #Creación de la clase planta de producción, que procesará las flores para transformarlas en ramos.
    def __init__(self): #Creación del método init
        Flor.__init__(self) 
        Ramo.__init__(self)
        self.lista_flores_ramo = [] #atributo para creacion de elementos de la lista de flores
        self.listado_item_flor = [] #
        self.contador_flores_ramo = 0 #atributo creado para establecer el conteo de ramo de flores desde 0 hacia arriba
        self.lista_ramo_solicitado = [] #atributo de ramo que fue solicitado por la empresa
        self.faltantes_en_ramo = 0 #atributo que definirá el conteo de flores faltantes para crear un ramo
        self.flores_usadas = [] #atributo que revisa y permitirá iterar los tipos de flores usadas para un ramo
        self.__inventario_ramos = [] #atributo que creará en una lista el número de ramos en stock de bodega
        self.__inventario_flores = [] #atributo que creará en una lista el número de flores en stock de bodega

    def diseno_ramo(self): #se crea el método que dará forma a la creación del ramo
        # cantidad items que tiene el ramo de forma random
        for i in range(random.randint(2, 4)):
            # largo maximo del ramo
            self.largo_ramo = random.randint(15, 30)
            # cantidad flores por item
            self.cantidad_flor = random.randint(1, 15)
            # crea una lista con la cantidad y el tipo de flor
            self.item_flor = [self.cantidad_flor,
                              random.choice(self.lista_flores)]
            # agrega a la lista del ramo la lista con cantidad y tipo de flor
            self.lista_flores_ramo.append(self.item_flor)
            # da una nomenclatura de cantidad y tipo flor sin espacios
            self.nomenclatura_item = ''.join(map(str, self.item_flor))
            # agrega la nomenclatura_item a un listado de item flor
            self.listado_item_flor.append(self.nomenclatura_item)
            # suma las flores de el item al contador
            self.contador_flores_ramo += self.cantidad_flor

        self.lista_ramo_solicitado.append(random.choice(self.nombre_ramo)) #determina que la creación de la lista ramo solicitado será mediante append y además randomizada
        self.lista_ramo_solicitado.append(random.choice(self.tamano_ramo)) 

        for a in self.listado_item_flor: #para un conjunto de elementos asignados en "a" en la lista item flor...
            self.lista_ramo_solicitado.append(a) 

        if self.largo_ramo > self.contador_flores_ramo: #si el largo del ramo es mayor que el contador de flores de ramo...
            self.faltantes_en_ramo = self.largo_ramo - self.contador_flores_ramo #las flores faltantes para crear un ramo será igual al largo del ramo
            self.lista_ramo_solicitado.append(self.largo_ramo) #añade elementos a la lista de ramos solicitados de acuerdo al atributo largo de ramo
        else: #si el largo del ramo no es mayor al contador flores ramo...
            self.lista_ramo_solicitado.append(self.contador_flores_ramo)#añade elementos a la lista de ramo solicitados de acuerdo al contador de flores de ramo

        self.ramo_concatenado = ''.join(map(str, self.lista_ramo_solicitado)) #se crea el método ramos concatenados con la ayuda del .join, que transforma los elementos de una lista que se encuentren separados, en una lista separada por comas para cada elemento. el .map toma las características de una función y los aplica a todos los elementos de la lista.
        return self.ramo_concatenado #se solicita que la función otorgue como return o resultado un ramo concatenado

    def crear_ramo(self): #método para crear ramo
        print('\nSolicitando las flores para el ramo....\n') #antes de la ejecución de la función, se imprime el mensaje en comillas
        for i in self.lista_flores_ramo: #para el elemento recien creado llamado "i" de lista_flores_ramo
            cantidad = i[0] #se define que cantidad es i junto con el elemento que está dentro, con número inicial 0 y que cambiará mas adelante para darle funcionalidad
            flor = i[1] 
            for j in range(cantidad): #para el elemento recién creado "j" que agrupa el rango "cantidad"...
                time.sleep(0.3) #se asigna un tiempo de reposo del script de 0.3 segundos
                print(flor+self.lista_ramo_solicitado[1]) #se imprime "flor"  más el listado de ramos solicitado
                self.flores_usadas.append(flor+self.lista_ramo_solicitado[1]) #se ejecuta la función de flores usadas para poder actualizar la cantidad de flores en el script interno

        if self.faltantes_en_ramo > 0: #si quedan flores por agregar en el ramo...
            self.flor_random = random.choice(self.lista_flores) #se entrega aleatoriamente algunas de la lista_flores
            print('\nCompletando flores faltantes...\n') #se imprime el mensaje en string, avisando que se está completando el ramo de flores
            for a in range(self.faltantes_en_ramo): #para "a" que agrupa los elementos de flores faltantes para crear un ramo, se aplica lo siguiente:
                time.sleep(0.5) #se crea una detención del script 
                self.flores_usadas.append( 
                    self.flor_random+self.lista_ramo_solicitado[1]) #la lista de flores usadas se rellena con las flores random utilizadas mas arriba, junto con la lista de ramos de flores solicitadas
                print(self.flores_usadas[-1]) #se imprime la cantidad de flores usadas

    def ramo_terminado(self): #se crea el método para finalizar un ramo y así sacarlo de la planta
        self.ramo_listo = self.lista_ramo_solicitado #atributo de ramo listo será igual a la lista creada más arriba
        self.ramo_listo.pop() #metodo .pop para eliminar elementos de la lista ramo_listo
        if self.faltantes_en_ramo > 0: #si aún se necesitan flores para crear un ramo...
            self.ramo_listo.append(self.faltantes_en_ramo) 
            self.ramo_listo.append(self.flor_random)
        self.ramo_listo_concatenado = ''.join(map(str, self.ramo_listo)) #se concatenan los elementos de la lista separados por una coma y luego se le asignan los métodos de la función ramo_listo a cada uno de los elementos de la lista.
        return self.ramo_listo_concatenado #cuando se ejecute la función ramo_terminado retornará lo que de el self.ramo_listo_concatenado

    def limpiar_listas(self): #se crea el método limpiar listas para limpiar la lista de los ramos que fueron solicitados y el item flor diseñado para la creación de ramos
        self.lista_ramo_solicitado = []
        self.listado_item_flor = []

    def bodega_flores(self): #método bodega_flores para verificar el stock de flores dentro de la bodega
        self.__inventario_flores.append(self.flores_usadas)
        return self.__inventario_flores #retorna la cantidad de flores en el inventario de la bodega

    def get_bodega_flores(self): #metodo get para llamar u obtener la cantidad de flores en la bodega
        print('Inventario de flores utilizadas') #imprime un mensaje para el script
        for i in self.__inventario_flores: #para el elemento i que contiene el inventario de flores...
            print(i) #imprime el elemento "i", que almacena el inventario de flores

    def bodega_ramos(self): #metodo bodega_ramos para crear el stock de ramos en bodega en base a la cantidad de ramos creados previamente concatenados
        self.__inventario_ramos.append(self.ramo_listo_concatenado)
        return self.__inventario_ramos

    def get_bodega_ramos(self): #obtención de stock de bodega en base al atributo inventario ramo creado previamente. Este se llama a través de la creación del elemento "i" que agrupa los elementos del método de la siguiente línea:
        print('Inventario de ramos creados')
        for i in self.__inventario_ramos:
            print(i)


# Ejecucion del programa
c.clear() #limpia el terminal de la misma forma que si uno escribiese "clear" en el términal
print('Bienvenido a FlorLinda Valdivia') #todos los elementos en "" son strings que se imprimen a la hora de ejecutar el script.
time.sleep(2) #todos los elementos con time.sleep son para dar un stop al script de acuerdo a los segundos asignados en parentesis
print('\nCargando datos ...')
time.sleep(5)
c.clear()
planta = PlantaProduccion() 
no_valido = 'Valor ingresado no es valido'
while True: #cuando el valor ingresado sea válido
    try:
        accion = int(input(
            '\n1 : Solicitar un ramo de flores\n0 : Salir\n')) #se ejecuta una serie de opciones en la pantalla donde el usuari determina si se solicita un ramo o desea salir del script
        if accion == 1: #si el usuario solicita un ramo de flores, se ejecutan los siguientes comandos para crear un ramo de flores de acuerdo a lo solicitado y de forma aleatoria
            planta.limpiar_listas() 
            c.clear()
            print('Se solicito el ramo:')
            print(planta.diseno_ramo())
            time.sleep(3)
            planta.crear_ramo()
            time.sleep(5)
            c.clear()
            print('\nRamo listo:')
            print(planta.ramo_terminado())
            planta.bodega_ramos()
            planta.bodega_flores()
            print()
            while True: #si se ejecutó el script con la opción 1: 
                try: 
                    accion2 = int(input( #se muestra en el terminal los siguientes comandos
                        '\n1 : Ver flores utilizadas\n2 : Ver ramos creados\n3 : Volver al menu principal\n'))
                    if accion2 == 1:
                        planta.get_bodega_flores() #muestra las flores que fueron utilizadas de la bodega
                    elif accion2 == 2:
                        planta.get_bodega_ramos() #se obtiene los ramos creados en el sistema y almacenados en la bodega
                    elif accion2 == 3:
                        break #se detiene el script y se regresa al script anterior
                    else: #en el caso que no se ejecute ninguno de los comandos permitidos, se regresa al mismo script
                        print(no_valido)
                        continue
                except Exception as e: #en el caso de que no se digiten comandos validos o exista algún defecto, se mostrará el mensaje no_valido
                    c.clear()
                    print(no_valido)
        elif accion == 0: #si se presiona el boton 0  se regresa al script anterior
            break
        else: #si no se ejecuta ninguno de los if o elif de arriba, se arroja un mensaje de error
            c.clear()
            print(no_valido)
            continue
    except Exception as e: #si no se ejecuta ninguno de los scripts de la línea respectiva, se arroja un mensaje de error.
        c.clear()
        print(no_valido)
