################### Clase Cliente #######################

class Cliente:
    def __init__(self, saldo_cliente):
        self.nombre = nombre
        self.rut = rut
        self.saldo = saldo_cliente

    def girar(self, cantidad):
        #realiza un giro en la cuenta
        self.saldo -= cantidad
        return self.saldo

    def abonar(self, cantidad):
        # realiza un abono en la cuenta
        self.saldo += cantidad
        return self.saldo

    def mostrar_saldo(self):
        # retorana el balance del saldo
        return self.saldo


################ Clase Financiera #####################


class Financiera:
    def __init__(self):
        self.nombre = nombre
        self.rut = rut
        self.saldo_institucional = saldo_institucional
        self.clientes = clientes


    def agregar_cliente():
        return True
    def eliminar_cliente():
        return True
    def transferir():
        return True

    def giros_totales(self):
        return True

    def abonos_totales(self):
        return True

    def mostrar_saldo_institucional():
        return True