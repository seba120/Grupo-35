from Finanzas import Cliente
from Finanzas import Financiera


cliente_1 = Cliente("Alfredo", 1000000)
cliente_2 = Cliente("Maria", 1000000)
cliente_3 = Cliente("Patricia", 1000000)
cliente_4 = Cliente("Mario", 1000000)
cliente_5 = Cliente("Katherine", 1000000)
cliente_6 = Cliente("Fernando", 1000000)
cliente_7 = Cliente("Fabiola", 1000000)
cliente_8 = Cliente("Constanza", 1000000)

financiera_1 = Financiera('Eurolatina', 100000000)
financiera_2 = Financiera('Conosur', 100000000)

financiera_1.agregar_cliente(cliente_1.id_cliente)
financiera_1.agregar_cliente(cliente_2.id_cliente)
financiera_1.agregar_cliente(cliente_3.id_cliente)
financiera_1.agregar_cliente(cliente_4.id_cliente)

financiera_2.agregar_cliente(cliente_5.id_cliente)
financiera_2.agregar_cliente(cliente_6.id_cliente)
financiera_2.agregar_cliente(cliente_7.id_cliente)
financiera_2.agregar_cliente(cliente_8.id_cliente)


print(financiera_1.clientes)
financiera_1.eliminar_cliente(cliente_1.id_cliente)
print(financiera_1.clientes)
