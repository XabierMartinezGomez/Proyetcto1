import sys

class Eventos():
    def Salir(self):
        '''Modulo para cerrar el programa :return:'''
        try:
            sys.exit()
        except Exception as error:
            print('Error %s' %str(error))