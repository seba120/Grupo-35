import os #importa modulo os
import sys #importa modulo sys
#ambos modulos son para interaccion con el sistema operativo


#funcion clear para limpiar consola
def clear():
#cada caso del if corresponde a un sistema operativo distinto windows,mac y linux
    if sys.platform.startswith('win'):
        os.system('cls') #corresponde a la funcion de limpiar consola en cmd de windows
    elif sys.platform.startswith('darwin'):
        os.system('clear') #corresponde a la funcion limpiar consola en terminal de mac
    elif sys.platform.startswith('linux'):
        os.system('clear') #corresponde a la funcion limpiar consola en terminal de linux
