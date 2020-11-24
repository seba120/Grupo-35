import uuid
import random

####### Condominio ########################


class Condominio:
    def __init__(self):
        self.direccion = ""
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

    def set_administrador(self , nombre_administrador):
        self.nombre_administrador = nombre_administrador
        self.lista_administrador = self.lista_administrador.append(self.nombre_administrador)
        return self.lista_administrador

    def get_administrador(self):
        print(self.lista_administrador)

    # agrega guardia por parametro
    def add_guardias(self, guardia):
        if len(self.lista_guardias) >= 4:
            print('No es posible agregar mas guardias')
        else:
            self.guardia = guardia
            self.lista_guardias.append(self.guardia)
        return self.lista_guardias

    # elimina guardia entregado por parametro
    def del_guardias(self, guardia):
        self.guardia = guardia
        self.lista_guardias.remove(self.guardia)
        return self.lista_guardias

    # muestra los guardias del condominio
    def get_guardias(self):
        for i in range(len(self.lista_guardias)):
            print(edificio.lista_guardias[i].nombre,
                  edificio.lista_guardias[i].apellido)

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
# se crea edificio
edificio = Condominio()
# se crean guardias
guardia1 = Guardia('Juan', 'Perez')
guardia2 = Guardia('Lalo', 'Landas')
guardia3 = Guardia('Beto A.', 'Saber')
guardia4 = Guardia('Tulio', 'De Las Mercedes')
guardia5 = Guardia('Este no ', 'Alcanza')

# se agregan guardias
edificio.add_guardias(guardia1)
edificio.add_guardias(guardia2)
edificio.add_guardias(guardia3)
edificio.add_guardias(guardia4)
# al agregar este guardia enviara mensaje de error y no lo agregara
edificio.add_guardias(guardia5)
# imprimo guardias guardados
edificio.get_guardias()

# se elimina guardia1
edificio.del_guardias(guardia1)
# se vuelven a imprimir guardias del listado
print()
edificio.get_guardias()
# ahora si agregamos el guardia luego de eliminar a uno
edificio.add_guardias(guardia5)
# vuelvo a imprimir la lista
print()
edificio.get_guardias()

print()
edificio.set_direccion("puente alto 1")
print(edificio.get_direccion())

print()
edificio.set_administrador("Administrador2")
edificio.get_administrador()
