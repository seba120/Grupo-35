import uuid
import random

####### Condominio ########################


class Condominio:
    def __init__(self):
        self.direccion = 'direccion'
        self.lista_administrador = []
        self.lista_guardias = []
        self.lista_unidades = []
        self.numero_unidades_habitacionales = len(self.lista_unidades)
        self.cuenta_corriente = uuid.uuid4()

    def set_direccion(self, direccion):
        self.direccion = direccion
        return self.direccion

    def get_direccion(self):
        return self.direccion

    def set_administrador(self):
        return self.administrador

    def get_administrador(self):
        return self.administrador

    def add_guardias(self, guardia):
        self.guardia = guardia
        self.lista_guardias.append(self.guardia)
        return self.lista_guardias

    def del_guardias(self):
        return self.lista_guardias

    def get_guardias(self):
        return self.lista_guardias

    def get_unidades(self):
        return self.lista_unidades


############ Guardia #############################

class Guardia:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.__id = uuid.uuid1()
        self.__sueldo_base = 500000
        self.__horas_extra = random.randint(0, 40)
        self.turno = random.choice(['Dia', 'Noche'])

    def get_id(self):
        return self.__id

    def get_sueldo(self):
        valor_hora = (self.__sueldo_base/40)/4
        total_horas = valor_hora * self.__horas_extra
        self.sueldo = self.__sueldo_base + total_horas
        if self.turno == 'Noche':
            self.sueldo += 50000
        return self.sueldo, self.__horas_extra, self.turno

    def set_sueldo(self, nuevo_base):
        self.__sueldo_base = nuevo_base
        return self.__sueldo_base


############ Unidad_Habitacional ###################
# class UnidadHabitacional:

    ######### Ejecuciones de prueba ##########


edificio = Condominio()

guardia1 = Guardia('Juan', 'Perez')
guardia2 = Guardia('Lalo', 'Landas')


edificio.add_guardias(guardia1)
edificio.add_guardias(guardia2)
for i in range(len(edificio.lista_guardias)):
    print(edificio.lista_guardias[i].nombre,
          edificio.lista_guardias[i].apellido)
