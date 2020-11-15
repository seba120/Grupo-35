import uuid
import random
###################Clase Cliente#######################


class Cliente:  # Se crea la clase cliente
    # se define como parámetros iniciales nombre de cliente, id de cliente y saldo.
    def __init__(self, nombre_cliente):
        # Se define que nombre cliente se asignará a futuro.
        self.nombre_cliente = nombre_cliente
        # Se define que el id de cliente sees asignado por el modulo uuid que
        # genera un id unico y con uuid4 el cual genera un id aleatoreo.
        self.id_cliente = uuid.uuid4()
        # Se define que el saldo de cliente se asignará a futuro.
        self.saldo_cliente = random.randint(1, 1000000)
        self.linea_credito = 1000000
        self.saldo_maximo = self.saldo_cliente + self.linea_credito

    # Metodo Clase Cliente
    def girar(self, cantidad_giro):  # Se define el parámetro cantidad de giro
        # Se define que cantidad de giro se asignará a futuro.
        self.cantidad_giro = cantidad_giro
        print('\n--- GIRO Cliente: {} ---\nSolicitando un giro de ${:,} a su cuenta.'.format(
            self.nombre_cliente, self.cantidad_giro).replace(',', '.'))
        # Se define que el saldo cliente que se solicite a futuro será el saldo menos la cantidad girada.
        if self.cantidad_giro > self.saldo_maximo or self.cantidad_giro < 0:
            print(
                '---No es posible realizar la operacion')
        elif self.cantidad_giro > self.saldo_cliente:
            self.faltante = self.cantidad_giro - self.saldo_cliente
            print('Su saldo en cuenta es: ${:,}'.format(
                self.saldo_cliente).replace(',', '.'))
            print('Se cubriran ${:,} desde su linea de credito'.format(
                self.faltante).replace(',', '.'))
            self.saldo_cliente = 0
            self.linea_credito = self.linea_credito - self.faltante
            print('-------------------')
            print('{} ha girado ${:,} desde su cuenta.'.format(
                self.nombre_cliente, self.cantidad_giro).replace(',', '.'))
        else:
            self.saldo_cliente = self.saldo_cliente - self.cantidad_giro
            print('-------------------')
            print('{} ha girado ${:,} desde su cuenta.'.format(
                self.nombre_cliente, self.cantidad_giro).replace(',', '.'))
        print('Saldo actual en cuenta: ${:,}\nSaldo actual linea de credito: ${:,}'.format(
            self.saldo_cliente, self.linea_credito).replace(',', '.'))
        print('---------------------\n')

    # se define la función abonar con el parámetro a definir de cantidad de abono.

    def abonar(self, cantidad_abono):
        # se define que cantidad de abono será asignado a futuro.
        self.cantidad_abono = cantidad_abono
        # se define que el saldo del cliente será dicho monto mas la cantidad abonada.
        self.saldo_cliente = self.saldo_cliente + self.cantidad_abono
        # la función arrojará como resultado la cantidad abonada.
        return self.cantidad_abono

    # función para mostrar saldo sin parámetros por asignar.
    def mostrar_saldo(self):
        # se define que el resultado de la función será un str predefinido con dos self a llamar: nombre de cliente + saldo de cliente.
        return '\n--- Cuenta de {} ---\nSaldo en cuenta: ${:,}\nLinea de credito disponible: {:,}\n---------------------------\n'.format(self.nombre_cliente, self.saldo_cliente, self.linea_credito).replace(',', '.')


################Clase Financiera#####################


class Financiera:
    def __init__(self, nombre_financiera):
        self.nombre_financiera = nombre_financiera
        self.id_financiera = uuid.uuid4()
        self.saldo_institucional = 100000000
        self.clientes = []
        #self.giros = giros
        #self.abonos = abonos

    def agregar_cliente(self, id_cliente):
        self.id_cliente = id_cliente
        return self.clientes.append(self.id_cliente)

    def eliminar_cliente(self, id_cliente):
        self.id_cliente = id_cliente
        return self.clientes.remove(self.id_cliente)

    def transferir():
        return True

    def giros_totales(self):
        return 'Los giros totales de los clientes de financiera {}, son {} hasta el momento'.format(self.nombre_financiera, self.giros)

    def abonos_totales(self):
        return 'Los giros abonos de los clientes de financiera {}, son {} hasta el momento'.format(self.nombre_financiera, self.abonos)

    def mostrar_saldo_institucional(self):
        return 'El saldo institucional actual de financiera {} es de: ${:,}'.format(self.nombre_financiera, self.saldo_institucional).replace(",", ".")
