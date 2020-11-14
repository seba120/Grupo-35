from Finanzas import Cliente
from Finanzas import Financiera

cliente_1 = [Cliente("Alfredo" , 1 , 1000000)]
cliente_2 = [Cliente("Maria" , 2 , 1000000)]
cliente_3 = [Cliente("Patricia" , 3 , 1000000)]
cliente_4 = [Cliente("Mario" , 4 , 1000000)]
cliente_5 = [Cliente("Katherine" , 5 , 1000000)]
cliente_6 = [Cliente("Fernando" , 6 , 1000000)]
cliente_7 = [Cliente("Fabiola" , 7 , 1000000)]
cliente_8 = [Cliente("Constanza" , 8 , 1000000)]


lista_financiera1 = [cliente_1 , cliente_2 , cliente_3 , cliente_4]
lista_financiera2 = [cliente_5 , cliente_6 , cliente_7 , cliente_8]

financiera1 = Financiera( "financiera_1" , "IDF1" , 100000000 , lista_financiera1)
financiera2 = Financiera( "financiera_2" , "IDF2" , 100000000 , lista_financiera2)



