import random
import time


class Flor:
    def __init__(self):
        self.nombre_flor = 'abcdefghijklmnopqrstuvwxyz'
        self.especie_flor = list(self.nombre_flor)
        self.tamano_flor = ''


class IngresoStock(Flor):
    def __init__(self):
        super().__init__()
        self.cantidad_flor = 0
        self.lista_flores = []

    def set_flor(self):
        for a in range(100):
            for i in range(300):
                nombre = random.choice(self.especie_flor)
                tamano = random.choice(['S', 'L'])
                #agregar_flor = [nombre, tamano]
                self.lista_flores.append(nombre+tamano)
                '''valor = random.uniform(0.1, 2)
                time.sleep(valor)'''
            print('cargando flores....\n')
            '''for a in self.lista_flores:
                print(a)

                time.sleep(random.uniform(0.1, 2))
            time.sleep(200)'''


class ConfiguracionRamo(IngresoStock):
    def __init__(self):
        super().__init__()
        texto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.nombre_ramo = list(texto)
        self.tamano_ramo = random.choice(['S', 'L'])

    def crear_ramo(self, objeto_flor):
        self.ramo_temporal = []
        self.largo_ramo = random.randint(15, 35)
        cantidad = 0
        while True:
            for i in range(random.randint(2, 6)):
                self.cantidad_flor = random.randint(1, 15)
                self.ramo_temporal.append(
                    random.choice(objeto_flor.lista_flores[0]))
                self.ramo_temporal.append(self.cantidad_flor)
                cantidad += self.cantidad_flor
            if cantidad <= self.largo_ramo:
                break

        print(cantidad)
        print(self.ramo_temporal)


f1 = IngresoStock()
f1.set_flor()

f2 = ConfiguracionRamo()
f2.crear_ramo(f1)
