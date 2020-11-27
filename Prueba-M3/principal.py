import random
import time


class EspecieFlor:
    def __init__(self):
        texto_flor = 'abcdefghijklmnopqrstuvwxyz'
        self.lista_flores = list(texto_flor)


class TamanoFlor():
    def __init__(self):
        self.tamanio_s = 'S'
        self.tamanio_l = 'L'


class Flor(EspecieFlor, TamanoFlor):
    def __init__(self):
        EspecieFlor.__init__(self)
        TamanoFlor.__init__(self)


class NombeRamo():
    def __init__(self):
        texto_ramo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.nombre_ramo = list(texto_ramo)


class TamanoRamo():
    def __init__(self):
        self.tamanio_ramo = ['S', 'L']


class Ramo(NombeRamo, TamanoRamo):
    def __init__(self):
        NombeRamo.__init__(self)
        TamanoRamo.__init__(self)
        self.lista_flores_ramo = []
        self.nomenclatura_ramo = []
        self.items_flor = []
        self.union_items = []
        self.largo_ramo = 0
        self.conteo_flores_ramo = 0
        self.faltantes_en_ramo = 0
        self.cantidad_flor = 0
        self.flores_usadas = []

    def diseño_ramo(self, objeto_flor):
        print('\nRamo solicitado: ')
        for i in range(random.randint(2, 4)):
            self.largo_ramo = random.randint(15, 30)
            self.cantidad_flor = random.randint(1, 15)
            self.items_flor = [self.cantidad_flor,
                               random.choice(objeto_flor.lista_flores)]
            self.lista_flores_ramo.append(self.items_flor)
            self.item_temporal = ''.join(map(str, self.items_flor))
            self.union_items.append(self.item_temporal)
            self.conteo_flores_ramo += self.cantidad_flor

        if self.largo_ramo > self.conteo_flores_ramo:
            self.faltantes_en_ramo = self.largo_ramo - self.conteo_flores_ramo
        self.nomenclatura_ramo.append(random.choice(self.nombre_ramo))
        self.nomenclatura_ramo.append(random.choice(self.tamanio_ramo))

        for a in self.union_items:
            self.nomenclatura_ramo.append(a)

        if self.largo_ramo < self.conteo_flores_ramo:
            self.nomenclatura_ramo.append(self.conteo_flores_ramo)
        else:
            self.nomenclatura_ramo.append(self.largo_ramo)
        solicitud_concatenada = ''.join(map(str, self.nomenclatura_ramo))
        return solicitud_concatenada

    def crear_ramo(self, objeto_flor):
        print('\nSolicitando flores...\n')
        for i in self.lista_flores_ramo:
            cantidad = i[0]
            flor = i[1]
            for e in range(cantidad):
                time.sleep(0.3)
                print(flor+self.nomenclatura_ramo[1])
                self.flores_usadas.append(
                    flor+self.nomenclatura_ramo[1])

        if self.faltantes_en_ramo > 0:
            self.flor_random = random.choice(objeto_flor.lista_flores)
            print('\nCompletando ramo...\n')
            for a in range(self.faltantes_en_ramo):
                time.sleep(0.5)
                self.flores_usadas.append(
                    self.flor_random+self.nomenclatura_ramo[1])
                print(self.flores_usadas[-1])

    def ramo_terminado(self):
        print('\nRamo terminado: ')
        self.ramo_listo = self.nomenclatura_ramo
        self.ramo_listo.pop()
        if self.faltantes_en_ramo > 0:
            self.ramo_listo.append(self.faltantes_en_ramo)
            self.ramo_listo.append(self.flor_random)
        ramo_listo_concatenado = ''.join(map(str, self.ramo_listo))
        return ramo_listo_concatenado


class PlantaProduccion:
    def __init__(self):
        self.terminar = False

    def pedir_ramo(self, objeto_ramo):
        objeto_ramo.crear_ramo()


class Bodega:
    pass


f1 = Flor()
r1 = Ramo()
print(r1.diseño_ramo(f1))
r1.crear_ramo(f1)
print(r1.ramo_terminado())
print()
