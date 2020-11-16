import uuid
import random
###################Clase Cliente#######################


class Cliente:  # Se crea la clase cliente
    # se define como parámetros iniciales nombre de cliente, id de cliente y saldo.
    pass

    def __init__(self, nombre_cliente):
        # Se define que nombre cliente se asignará a futuro.
        self.nombre_cliente = nombre_cliente
        # Se define que el id de cliente sees asignado por el modulo uuid que
        # genera un id unico y con uuid4 el cual genera un id aleatoreo.
        self.id_cliente = uuid.uuid4()
        # Se define que el saldo de cliente se asignará a futuro.
        self.saldo_cliente = random.randint(1, 1000000)
        self.linea_credito = 1000000
        self.contador_giro = 0
        self.contador_abono = 0

    # Metodo Clase Cliente
    def girar(self, cantidad_giro):  # Se define el parámetro cantidad de giro
        # Se define que cantidad de giro se asignará a futuro.
        self.cantidad_giro = cantidad_giro
        self.saldo_maximo = self.saldo_cliente + self.linea_credito
        print('\n--- GIRO  de Cliente: {} ---\nSolicitando un giro de ${:,} de su cuenta.'.format(
            self.nombre_cliente, self.cantidad_giro).replace(',', '.'))
        # Se define que el saldo cliente que se solicite a futuro será el saldo menos la cantidad girada.
        if self.cantidad_giro > self.saldo_maximo:
            print('---No es posible realizar la operación')
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
            self.contador_giro = self.contador_giro + 1
        else:
            self.saldo_cliente = self.saldo_cliente - self.cantidad_giro
            print('-------------------')
            print('{} ha girado ${:,} desde su cuenta.'.format(
                self.nombre_cliente, self.cantidad_giro).replace(',', '.'))
            self.contador_giro = self.contador_giro + 1
        print('Saldo actual en cuenta: ${:,}\nSaldo actual linea de credito: ${:,}'.format(
            self.saldo_cliente, self.linea_credito).replace(',', '.'))
        print('---------------------')

    # se define la función abonar con el parámetro a definir de cantidad de abono.

    def abonar(self, cantidad_abono):
        # se define que cantidad de abono será asignado a futuro.
        self.cantidad_abono = cantidad_abono
        print('\n--- ABONO a Cliente: {} ---\nAbono por un monto de ${:,} a su cuenta.'.format(
            self.nombre_cliente, self.cantidad_abono).replace(',', '.'))
        # se define que el saldo del cliente será dicho monto mas la cantidad abonada.
        if self.cantidad_abono < 1:
            print('---Abono no puede ser inferior a $1')
        elif self.linea_credito < 1000000:
            self.deuda = 1000000 - self.linea_credito
            if self.deuda >= cantidad_abono:
                self.abono = self.cantidad_abono
                self.linea_credito = self.linea_credito + self.abono
                self.excedente = 0
                print('El monto fue abonado a su Linea de credito')
            else:
                self.linea_credito = self.linea_credito + self.deuda
                self.excedente = self.cantidad_abono - self.deuda
            print('-------------------')
            print('Se abonaron: ${:,} a su linea de credito\nSe abonaron: ${:,} a su cuenta'.format(
                self.abono, self.excedente).replace(',', '.'))
            self.contador_abono = self.contador_abono + 1
        else:
            self.saldo_cliente = self.saldo_cliente + self.cantidad_abono
            print('-------------------')
            print('Se abonaron: ${:,} a su cuenta'.format(
                self.cantidad_abono).replace(',', '.'))
            self.contador_abono = self.contador_abono + 1
        print('Saldo actual en cuenta: ${:,}\nSaldo actual linea de credito: ${:,}'.format(
            self.saldo_cliente, self.linea_credito).replace(',', '.'))
        print('---------------------\n')

    # función para mostrar saldo sin parámetros por asignar.

    def mostrar_saldo(self):
        # se define que el resultado de la función será un str predefinido con dos self a llamar: nombre de cliente + saldo de cliente.
        print('\n--- Cuenta de cliente: {} ---\nSaldo en cuenta: ${:,}\nLinea de credito disponible: ${:,}'.format(
            self.nombre_cliente, self.saldo_cliente, self.linea_credito).replace(',', '.'))
        if self.linea_credito < 1000000:
            self.deuda_linea = (self.linea_credito - 1000000)*-1
            print('Deuda en linea de credito: ${:,}'.format(
                self.deuda_linea).replace(',', '.'))
        print('---------------------')


################Clase Financiera#####################


class Financiera:
    pass

    def __init__(self, nombre_financiera):
        self.nombre_financiera = nombre_financiera
        self.id_financiera = uuid.uuid4()
        self.saldo_institucional = 100000000
        self.clientes = []
        self.giros = 0
        self.abonos = 0

    def agregar_cliente(self, cliente):
        self.cliente = cliente
        if (len(self.clientes)*1000000) > (self.saldo_institucional*0.1):
            print('No es posible agrgar mas clientes')
        else:
            self.clientes.append(self.cliente)

    def eliminar_cliente(self, id_cliente):
        self.id_cliente = id_cliente
        return self.clientes.remove(self.id_cliente)

    def transferir(self, monto, origen, destino):
        self.monto = monto
        self.origen = origen
        self.destino = destino
        print('******** Transferencia *********')
        print('Cuenta origen: {}\nCuenta destino: {}\nMonto: ${:,}'.format(
            self.origen.nombre_cliente, self.destino.nombre_cliente, self.monto).replace(',', '.'))
        if self.origen in self.clientes and self.destino in self.clientes:
            self.origen.girar(self.monto)
            self.destino.abonar(self.monto)
        else:
            print('---No es posible realizar la transacción')
        print('*********************************')

    def giros_totales(self):
        if self.origen in self.clientes:
            self.acumulador_giros = self.origen.contador_giro
            self.giros = self.acumulador_giros
        print('Los giros totales de los clientes de financiera {}, son {} hasta el momento'.format(
            self.nombre_financiera, self.giros))

    def abonos_totales(self):
        if self.origen in self.clientes:
            self.acumulador_abonos = self.origen.contador_abono
            self.abonos = self.acumulador_abonos
        print('Los giros abonos de los clientes de financiera {}, son {} hasta el momento'.format(
            self.nombre_financiera, self.abonos))

    def mostrar_saldo_institucional(self):
        return 'El saldo institucional actual de financiera {} es de: ${:,}'.format(self.nombre_financiera, self.saldo_institucional).replace(",", ".")
