import random
import time
import limpiador as c


class Flor:
    def __init__(self):
        texto_flor = 'abcdefghijklmnopqrstuvwxyz'
        self.lista_flores = list(texto_flor)
        self.tamanios = ['S', 'L']


class Ramo:
    def __init__(self):
        texto_ramo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.nombre_ramo = list(texto_ramo)
        self.tamano_ramo = ['S', 'L']


class PlantaProduccion(Flor, Ramo):
    def __init__(self):
        Flor.__init__(self)
        Ramo.__init__(self)
        self.lista_flores_ramo = []
        self.listado_item_flor = []
        self.contador_flores_ramo = 0
        self.lista_ramo_solicitado = []
        self.faltantes_en_ramo = 0
        self.flores_usadas = []
        self.__inventario_ramos = []
        self.__inventario_flores = []

    def diseno_ramo(self):
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

        self.lista_ramo_solicitado.append(random.choice(self.nombre_ramo))
        self.lista_ramo_solicitado.append(random.choice(self.tamano_ramo))

        for a in self.listado_item_flor:
            self.lista_ramo_solicitado.append(a)

        if self.largo_ramo > self.contador_flores_ramo:
            self.faltantes_en_ramo = self.largo_ramo - self.contador_flores_ramo
            self.lista_ramo_solicitado.append(self.largo_ramo)
        else:
            self.lista_ramo_solicitado.append(self.contador_flores_ramo)

        self.ramo_concatenado = ''.join(map(str, self.lista_ramo_solicitado))
        return self.ramo_concatenado

    def crear_ramo(self):
        print('\nSolicitando las flores para el ramo....\n')
        for i in self.lista_flores_ramo:
            cantidad = i[0]
            flor = i[1]
            for j in range(cantidad):
                time.sleep(0.3)
                print(flor+self.lista_ramo_solicitado[1])
                self.flores_usadas.append(flor+self.lista_ramo_solicitado[1])

        if self.faltantes_en_ramo > 0:
            self.flor_random = random.choice(self.lista_flores)
            print('\nCompletando flores faltantes...\n')
            for a in range(self.faltantes_en_ramo):
                time.sleep(0.5)
                self.flores_usadas.append(
                    self.flor_random+self.lista_ramo_solicitado[1])
                print(self.flores_usadas[-1])

    def ramo_terminado(self):
        self.ramo_listo = self.lista_ramo_solicitado
        self.ramo_listo.pop()
        if self.faltantes_en_ramo > 0:
            self.ramo_listo.append(self.faltantes_en_ramo)
            self.ramo_listo.append(self.flor_random)
        self.ramo_listo_concatenado = ''.join(map(str, self.ramo_listo))
        return self.ramo_listo_concatenado

    def limpiar_listas(self):
        self.lista_ramo_solicitado = []
        self.listado_item_flor = []

    def bodega_flores(self):
        self.__inventario_flores.append(self.flores_usadas)
        return self.__inventario_flores

    def get_bodega_flores(self):
        print('Inventario de flores utilizadas')
        for i in self.__inventario_flores:
            print(i)

    def bodega_ramos(self):
        self.__inventario_ramos.append(self.ramo_listo_concatenado)
        return self.__inventario_ramos

    def get_bodega_ramos(self):
        print('Inventario de ramos creados')
        for i in self.__inventario_ramos:
            print(i)


# Ejecucion del programa
c.clear()
print('Bienvenido a FlorLinda Valdivia')
time.sleep(2)
print('\nCargando datos ...')
time.sleep(5)
c.clear()
planta = PlantaProduccion()
no_valido = 'Valor ingresado no es valido'
while True:
    try:
        accion = int(input(
            '\n1 : Solicitar un ramo de flores\n0 : Salir\n'))
        if accion == 1:
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
            while True:
                try:
                    accion2 = int(input(
                        '\n1 : Ver flores utilizadas\n2 : Ver ramos creados\n3 : Volver al menu principal\n'))
                    if accion2 == 1:
                        planta.get_bodega_flores()
                    elif accion2 == 2:
                        planta.get_bodega_ramos()
                    elif accion2 == 3:
                        break
                    else:
                        print(no_valido)
                        continue
                except Exception as e:
                    c.clear()
                    print(no_valido)
        elif accion == 0:
            break
        else:
            c.clear()
            print(no_valido)
            continue
    except Exception as e:
        c.clear()
        print(no_valido)
