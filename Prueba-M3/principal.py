import random


class Flor:
    def __init__(self):
        self.nombre_flor = 'abcdefghijklmnopqrstuvwxyz'
        self.especie_flor = list(self.nombre_flor)
        self.tamano_flor = ''


class IngresoStock(Flor):
    def __init__(self):
        super().__init__()
        self.cantidad_flor = 0
        self.lista_flores = {}

    def set_flor(self):
        for i in range(2):
            if i == 0:
                self.medida = 'S'
            else:
                self.medida = 'L'
            for i in self.especie_flor:
                cantidad = random.randint(0, 30)
                dicciona = {'medida': self.medida, 'cantidad': cantidad}
                self.lista_flores[i] = dicciona
            print(self.lista_flores)
            print()


f1 = IngresoStock()
f1.set_flor()

print(f1.lista_flores.keys())
