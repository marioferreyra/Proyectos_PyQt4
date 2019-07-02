# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from time import strftime


class Reloj(QWidget):
    """
    Reloj con checkbox's para ver o ocultar los segundos.
    """
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("clock.ui", self)

        self.timer = QTimer()

        # Conexion
        self.timer.timeout.connect(self.update)

        self.timer.start(1000)

    def update(self):
        """
        Se encarga de actualizar la hora del LCD, verificando si debe mostrar
        o no los segundos.
        """
        if self.radioShow.isChecked():
            self.mylcd.setDigitCount(8)
            hora = strftime("%H"+":"+"%M"+":"+"%S")
        elif self.radioHide.isChecked():
            self.mylcd.setDigitCount(5)
            hora = strftime("%H"+":"+"%M")
        
        self.mylcd.display(hora)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myapp = Reloj()
    myapp.show()

    sys.exit(app.exec_())
