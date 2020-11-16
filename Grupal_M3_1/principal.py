from Finanzas import Cliente
from Finanzas import Financiera
import time
import limpiador as l

l.clear()
# 1. Crear 2 financieras de la clase Financiera con nombre y saldo inicial de $100Millones.
financiera_1 = Financiera('Eurolatina')
financiera_2 = Financiera('Conosur')

# 2. Crear 4 clientes por cada financiera.
cliente_1 = Cliente("Sebastían")
cliente_2 = Cliente("Maria")
cliente_3 = Cliente("Jaime")
cliente_4 = Cliente("Mario")

financiera_1.agregar_cliente(cliente_1)
financiera_1.agregar_cliente(cliente_2)
financiera_1.agregar_cliente(cliente_3)
financiera_1.agregar_cliente(cliente_4)

##################################

cliente_5 = Cliente("Katherine")
cliente_6 = Cliente("Alfonso")
cliente_7 = Cliente("Fabiola")
cliente_8 = Cliente("Victoria")

financiera_2.agregar_cliente(cliente_5)
financiera_2.agregar_cliente(cliente_6)
financiera_2.agregar_cliente(cliente_7)
financiera_2.agregar_cliente(cliente_8)

# 3. Realizar 3 operaciones por cada cliente de distinto tipo (giro, abono).
cliente_1.mostrar_saldo()
time.sleep(0.5)
cliente_1.girar(30000)
time.sleep(0.5)
cliente_1.abonar(100000)
time.sleep(0.5)
cliente_1.girar(300000)
time.sleep(5)
l.clear()

cliente_2.mostrar_saldo()
time.sleep(0.5)
cliente_2.abonar(400000)
time.sleep(0.5)
cliente_2.abonar(60000)
time.sleep(0.5)
cliente_2.girar(1500000)
time.sleep(5)
l.clear()

cliente_3.mostrar_saldo()
time.sleep(0.5)
cliente_3.abonar(8000)
time.sleep(0.5)
cliente_3.abonar(10000)
time.sleep(0.5)
cliente_3.girar(150000)
time.sleep(5)
l.clear()

cliente_4.mostrar_saldo()
time.sleep(0.5)
cliente_4.girar(18500)
time.sleep(0.5)
cliente_4.girar(110000)
time.sleep(0.5)
cliente_4.abonar(200000)
time.sleep(5)
l.clear()

cliente_5.mostrar_saldo()
time.sleep(0.5)
cliente_5.abonar(10000)
time.sleep(0.5)
cliente_5.abonar(15000)
time.sleep(0.5)
cliente_5.girar(150000)
time.sleep(5)
l.clear()

cliente_6.mostrar_saldo()
time.sleep(0.5)
cliente_6.abonar(15500)
time.sleep(0.5)
cliente_6.girar(200000)
time.sleep(0.5)
cliente_6.girar(20300)
time.sleep(5)
l.clear()

cliente_7.mostrar_saldo()
time.sleep(0.5)
cliente_7.girar(40000)
time.sleep(0.5)
cliente_7.abonar(600000)
time.sleep(0.5)
cliente_7.girar(75800)
time.sleep(5)
l.clear()

cliente_8.mostrar_saldo()
time.sleep(0.5)
cliente_8.abonar(800000)
time.sleep(0.5)
cliente_8.girar(60000)
time.sleep(0.5)
cliente_8.girar(70000)
time.sleep(5)
l.clear()

# 4. Realizar giros en dos clientes que demuestren que el saldo no puede ser menor a - 1000000.

cliente_2.mostrar_saldo()
time.sleep(0.5)
cliente_2.girar(4000000)
time.sleep(5)
l.clear()
cliente_5.mostrar_saldo()
time.sleep(0.5)
cliente_5.girar(7000000)
time.sleep(5)
l.clear()

# 5. Realizar 4 transferencias entre clientes.

financiera_1.transferir(7000, cliente_3, cliente_1)
time.sleep(5)
l.clear()
financiera_2.transferir(150000, cliente_7, cliente_8)
time.sleep(5)
l.clear()
financiera_1.transferir(85000, cliente_2, cliente_4)
time.sleep(5)
l.clear()
financiera_2.transferir(300, cliente_6, cliente_5)
time.sleep(5)
l.clear()
