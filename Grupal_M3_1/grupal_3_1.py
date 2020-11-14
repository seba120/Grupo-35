###################Clase Cliente#######################

class Cliente:
    def __init__(self, nombre_cliente, id_cliente , saldo_cliente):
        self.nombre_cliente = nombre_cliente
        self.id_cliente = id_cliente
        self.saldo_cliente = saldo_cliente

    #Metodo Clase Cliente
    def girar(self , cantidad_giro):
        self.cantidad_giro = cantidad_giro
        self.saldo_cliente = self.saldo_cliente - self.cantidad_giro
        return self.cantidad_giro

    def abonar(self , cantidad_abono):
        self.cantidad_abono = cantidad_abono
        self.saldo_cliente = self.saldo_cliente + self.cantidad_abono
        return self.cantidad_abono

    def mostrar_saldo (self):
        return "El saldo de {} es: {}".format(self.nombre_cliente , self.saldo_cliente) 

seba = Cliente("seba" , 1 , 1000000)
print("Usted giró:" , seba.girar(300000) , ". El saldo de su cuenta es:" , seba.saldo_cliente , "." )

print(seba.mostrar_saldo())

################Clase Financiera#####################

"""
class Financiera:
    def __init__(self):
        self.nombre = nombre
        self.id = id
        self.saldo_institucional = saldo_institucional
        self.clientes = clientes

    def agregar_cliente():
        return True

    def eliminar_cliente():
        return True

    def transferir():
        return True

    def giros_totales():
        return True

    def abonos_totales():
        return True

    def mostrar_saldo_institucional():
        return True
"""