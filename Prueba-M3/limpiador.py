import os  # importa modulo os
import sys  # importa modulo sys
# ambos modulos son para interaccion con el sistema operativo


# funcion clear para limpiar consola
def clear():
    # cada caso del if corresponde a un sistema operativo distinto windows,mac y linux
    if sys.platform.startswith('win'):
        # corresponde a la funcion de limpiar consola en cmd de windows
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        # corresponde a la funcion limpiar consola en terminal de mac
        os.system('clear')
    elif sys.platform.startswith('linux'):
        # corresponde a la funcion limpiar consola en terminal de linux
        os.system('clear')
