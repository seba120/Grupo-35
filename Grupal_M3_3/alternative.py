import random


class Terreno:
    def __init__(self):
        self.localidad = ['Ciudad', 'Suburvios', 'Rural']
        self.__dimension_terreno = 0
        self.servicios_cercanos = []
        self.cantidad_areas_verdes = 0


class Condominio:
    def __init__(self):
        self.direccion = ''
        self.administrador = ''
        self.lista_guardias = []
        self.__num_unidades_habitacionales = 0
        self.__lista_unidades_habitacionales = []
        self.__cuenta_corriente = ''
        self.__gasto_comun = 0
        self.nombre_condominio = ''
        self.empresa_constructora = ''
        self.ano_construccion = 0

    def set_direccion(self, calle, numero, comuna):
        self.region = ['XV', 'I', 'II', 'III', 'IV', 'V', 'VI',
                       'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'RM', 'XIV']
        self.direccion = [calle, numero, comuna, random.choice(self.region)]
        self.formato_direccion = ', '.join(map(str, self.direccion))

    def get_direccion(self):
        formato_get_direccion = 'La direccion  es {}'.format(
            self.formato_direccion)
        return formato_get_direccion

    def set_administrador(self, nombre_administrador):
        self.administrador = nombre_administrador

    def get_administrador(self):
        formato_get_administrador = 'El administrador de la comunidad {}, es Don {}'.format(
            self.nombre_condominio, self.administrador)
        return formato_get_administrador

    def add_guardia(self, guardia):
        self.lista_guardias.append(guardia.nombre_guardia)
        return self.lista_guardias

    def del_guardia(self, guardia):
        self.lista_guardias.remove(guardia)
        return self.lista_guardias

    def get_guardias(self):
        return self.lista_guardias


class CondominioVertcal(Terreno, Condominio):
    def __init__(self):
        Terreno.__init__()
        Condominio.__init__()
        self.pisos = 0
        self.numeracion = 0
        self.cantidad_ascensores = 0
        self.estacionamientos = ['Si', 'No']
        self.piscina = ['Si', 'No']
        self.habitaciones = 0


class CondominioHorizontal:
    def __init__(self):
        Terreno.__init__()
        Condominio.__init__()
        self.numeracion = 0
        self.modelo_casa = ['Mediterraneo', 'Alerce', 'Castaño', 'Basica']
        self.disposicion_casa = ['Esquina', 'Pareada', 'Aislada']
        self.pisos = 0
        self.habitaciones = 0
        self.metros_cuadrados = 0


class CuentaCorriente:
    def __init__(self):
        self.numero_cuenta = ''
        self.banco = ''
        self.saldo_cuenta = 0


class Guardia:
    def __init__(self):
        self.nombre_guardia = ''
        self.sueldo_guardia = 0
        self.empresas_guardias = 'Prosegur'
        self.turno_guardia = ['Dia', 'Noche']
        self.contador_turno = 1

    def set_guardia(self, nombre_guardia):
        self.nombre_guardia = nombre_guardia

    def set_turno(self):
        if (self.contador_turno % 2) == 0:
            self.turno = self.turno_guardia[0]
        else:
            self.turno = self.turno_guardia[1]
        return self.turno

    def set_sueldo(self):
        sueldo_base = random.randint(400000, 600000)
        horas_extra = random.randint(0, 40)
        valor_hora = (sueldo_base / 40)/4
        sueldo_bruto = sueldo_base + horas_extra * valor_hora
        descuentos = sueldo_bruto * 0.19
        self.sueldo_guardia = sueldo_bruto - descuentos


class UnidadHabitacional:
    pass
