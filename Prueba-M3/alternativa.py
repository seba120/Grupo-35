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
        self.inicial_flor = random.choice(self.especie_flor)
        self.tamano_flor = random.choice(['S', 'L'])
        # agregar_flor = [nombre, tamano]
        self.lista_flores.append(self.inicial_flor+self.tamano_flor)
        # time.sleep(random.uniform(0.1, 2))


class ConfiguracionRamo(IngresoStock):
    def __init__(self):
        super().__init__()
        texto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.nombre_ramo = list(texto)
        self.tamano_ramo = random.choice(['S', 'L'])

    def crear_ramo(self, objeto_flor):
        self.ramo_temporal = []
        self.nomenclatura = []
        self.largo_ramo = random.randint(15, 30)
        cantidad = 0
        faltantes = 0
        for i in range(random.randint(2, 4)):
            self.cantidad_flor = random.randint(1, 15)
            self.ramo_temporal.append(
                random.choice(objeto_flor.especie_flor))
            self.ramo_temporal.append(self.cantidad_flor)
            cantidad += self.cantidad_flor
        if cantidad < self.largo_ramo:
            faltantes = self.largo_ramo - cantidad
        self.nomenclatura.append(random.choice(self.nombre_ramo))
        self.nomenclatura.append(self.tamano_ramo)
        for a in self.ramo_temporal:
            self.nomenclatura.append(a)
        if self.largo_ramo < cantidad:
            self.nomenclatura.append(cantidad)
        else:
            self.nomenclatura.append(self.largo_ramo)

        print(objeto_flor.lista_flores)
        print(self.largo_ramo)
        print(faltantes)
        print(cantidad)
        print(self.ramo_temporal)
        print(self.nomenclatura)
        print(''.join(map(str, self.nomenclatura)))


f1 = IngresoStock()


f2 = ConfiguracionRamo()
f2.crear_ramo(f1)
f1.set_flor()
exit()
