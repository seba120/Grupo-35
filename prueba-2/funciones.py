import time  # importa el modulo time
import limpiador as l  # importa el modulo limpiador para limpiar la consola

# se inicializa lista vacia para almacenar los valores ingresados por usuario
listado_de_valores = []


# funcion que pedira el valor al usuario
def pedir_valor():
    valor = 0  # se inicializa variable valor en 0
    while True:  # sentencia se ejecuta hasta que se produzca un break
        try:  # se intenta capturar un numero en la variable valor
            valor = int(input('Ingrese un valor entre 0 y 999.999: '))
# si se ingresa otro tipo de dato distinto a int enviara mensaje de error y volvera a iterar el while
        except Exception:
            print('\nEl valor ingresado no es valido\n')
            time.sleep(1)
            l.clear()
            continue
        if valor < 1000000:  # si el valor ingresado es menor a 1.000.000 saldra del bucle con break
            break
        else:  # si el valor es mayor a 1.000.000 dara mensaje de error y volvera a iterar
            print('\nEl valor ingresado no es valido\n')
            time.sleep(1)  # esperara 1 segundo y limpiara la consola
            l.clear()
# cuando salga del bucle el valor se agregara a listado_de_valores para ser impreso al
# final de la ejecucion del programa
    listado_de_valores.append(valor)
    valor_str = str(valor)  # el valor ingresado se pasa de int a str
# ya con valor str se pasa a una lista que contiene sus elementos por separado
# ejemplo: '13456' = ['1','3','4','5','6']
    lista = list(valor_str)
    while len(lista) < 6:  # en el caso que el valor ingresado tenga un largo de elementos menor a 6
        # se agreagara una posicion al inicio con el valor '0'
        lista[-100:-50] = ['0']
    return lista


# metodo que convierte los elementos igresados clave:valor en una lista
def diccionario(**kwargs):
    for cla, val in kwargs.items():
        # imprimira los elementos uno por uno con el siguiente formato:
        print(cla, ':', val, end='   ')
    return kwargs   # clave:valor     clave: valor   etc...


# funcion que imprime abaco en pantalla
def pintar_abaco():
    a1 = ['  +-+  ', '  | |  ', ' XXXXX ']  # valores de print
    b1 = a1  # cada uno de los siguientes elementos tendra el mismo valor que a1
    c1 = a1
    d1 = a1
    e1 = a1
    f1 = a1
    # valores sera una lista con los elementos que entrega la funcion pedir valores
    valores = pedir_valor()
    print()  # que retorna la lista creada en base al valor ingresado por usuario
    # imprime la fila superior de los 6 abacos
    print(a1[0], b1[0], c1[0], d1[0], e1[0], f1[0])
# for con un contador en reversa para ir pintando cada nivel de cada abaco
    for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
        # en cada uno de los siguientes if y else los valores de a2,b2,c2,d2,e2 y f2
        # se pìntaran de acuerdo al nivel que este iterando i hasta completar las 9 iteraciones
        if int(valores[0]) < i:  # ejemplo si en la ieracion 9 a2 = 1 imprime | |
            a2 = 1  # en caso contrario si vale 2 imprime XXXXX
        else:
            a2 = 2
        if int(valores[1]) < i:
            b2 = 1
        else:
            b2 = 2
        if int(valores[2]) < i:
            c2 = 1
        else:
            c2 = 2
        if int(valores[3]) < i:
            d2 = 1
        else:
            d2 = 2
        if int(valores[4]) < i:
            e2 = 1
        else:
            e2 = 2
        if int(valores[5]) < i:
            f2 = 1
        else:
            f2 = 2
# en cada iteracion de 9 a 1 completara una linea de cada ilera del abaco
        print(a1[a2], b1[b2], c1[c2], d1[d2], e1[e2], f1[f2])
    # imprime la base del abaco con +-+
    print(a1[0], b1[0], c1[0], d1[0], e1[0], f1[0])
    # imprime los valores bajo cada ilera del abaco
    print('100.000  10.000  1.000    100      10      1')
    print()  # salto de linea
# se llama a la funcion diccionario y se le pasan como argumentos los valores de la
# lista creada con el valor ingresado por usuario, searandolo por unidad, decena, centena etc.
    diccionario(CM=valores[0], DM=valores[1],
                UM=valores[2], C=valores[3], D=valores[4], U=valores[5])
    print()


# funcion para iniciar el juego
def abaco():
    while True:  # se repetira el loop hasta que se produzca un brake
        l.clear()  # parte limpiando la consola con la importacion de clear desde script limpiador.py
        pintar_abaco()  # llama a funcion pintar abaco
        salir = input(  # una vez realzada la primera iteracion del abaco, pregunta si desea continuar
            '\nPara terminar escriba "salir" o presione Enter para continuar: ')  # a traves de un input
# en caso que el usuario escriba la palabra salir la convierte a mayusculas en
        if salir.upper() == 'SALIR':  # caso que el usuario active las mayusculas del teclado
            l.clear()  # limpiara la consola y enviara un brake para salir del loop
            break
        # en caso que el usuario presione enter o ingrese cualquier otro caracter
        time.sleep(1.5)
        l.clear()  # el proograma limpiara la consola luego de 1.5 segundos y comenzara otra iteración
# una vez que el usuario indique salir se imprimira el siguiente mensaje
    print('Los valores ingresados en el abaco fueron los siguientes: \n')
# sentencia for para imprimir cada valor alojado en el listado_de_valores
    for i in listado_de_valores:
        # da formato de . para separar por miles cada valor y lo guarda en item
        item = '{:,}'.format(i).replace(",", ".")
        # imprime el valor con formato guardado en item y le da nuevamente
        print(format(item, '>20'))
    print()  # formato pero esta vez para alinear cada item a la derecha
