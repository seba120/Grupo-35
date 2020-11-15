from Finanzas import Cliente
from Finanzas import Financiera


cliente_1 = Cliente("Sebastían")
cliente_2 = Cliente("Maria")
cliente_3 = Cliente("Jaime")
cliente_4 = Cliente("Mario")
cliente_5 = Cliente("Katherine")
cliente_6 = Cliente("Alfonso")
cliente_7 = Cliente("Fabiola")
cliente_8 = Cliente("Victoria")

print(cliente_1.mostrar_saldo())
cliente_1.girar(3000000)
cliente_1.girar(1100000)
print(cliente_1.mostrar_saldo())


financiera_1 = Financiera('Eurolatina')
financiera_2 = Financiera('Conosur')

financiera_1.agregar_cliente(cliente_1.id_cliente)
financiera_1.agregar_cliente(cliente_2.id_cliente)
financiera_1.agregar_cliente(cliente_3.id_cliente)
financiera_1.agregar_cliente(cliente_4.id_cliente)

financiera_2.agregar_cliente(cliente_5.id_cliente)
financiera_2.agregar_cliente(cliente_6.id_cliente)
financiera_2.agregar_cliente(cliente_7.id_cliente)
financiera_2.agregar_cliente(cliente_8.id_cliente)

print(financiera_1.mostrar_saldo_institucional())
print(financiera_2.mostrar_saldo_institucional())

print(financiera_1.clientes)
financiera_1.eliminar_cliente(cliente_1.id_cliente)
print(financiera_1.clientes)
