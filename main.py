from dni import *
import sys, var, events

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

    '''
    conexion de eventos con los objetos
    '''
    var.ui.btnSalir.cliked.connect(events.Eventos.Salir)
    var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

if __name__ =='__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    sys.exit(app.exec())