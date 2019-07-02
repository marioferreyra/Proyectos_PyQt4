# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

ONE_SECOND = 1000 # 1000 ms = 1 s

class Cronometro(QWidget):
    """
    Ventana que muestra un cronometro, con el tiempo, botones para iniciar,
    pausar, resetear y mostrar el tiempo parcial.
    """
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("cronometro.ui", self)

        self.tick = 0 # Segundos transcurridos
        self.split_number = 1
        self.timer = QTimer()
        
        self.label.setText("00:00:00")
        
        # Conexion
        self.timer.timeout.connect(self.setTime)
        self.btnStart.clicked.connect(self.start)
        self.btnReset.clicked.connect(self.reset)
        self.btnSplit.clicked.connect(self.split)
        self.btnExit.clicked.connect(self.close)

    def start(self):
        """
        Comienza el cronometro.
        """
        if not self.isTimerActive():
            self.timer.start(ONE_SECOND)
            self.btnStart.setText("Stop")
        else:
            self.timer.stop()
            self.btnStart.setText("Start")

    def reset(self):
        """
        Reinicia el cronometro.
        """
        self.timer.stop()
        self.tick = 0
        self.start()

    def split(self):
        """
        Obtiene el tiempo parcial transcurrido.
        """
        self.list_split.addItem(str(self.split_number) + " --> " + self.label.text())
        self.split_number += 1

    def isTimerActive(self):
        """
        Retorna True si el temporizador (timer) esta activo.
        """
        return self.timer.isActive()

    def setTime(self):
        """
        Establece el tiempo en el formato HH:MM:SS en el texto mostrado.
        """
        self.tick += 1

        hour = self.tick / 3600
        minutes = (self.tick % 3600) / 60
        seconds = (self.tick % 3600) % 60
        self.label.setText("%02d:%02d:%02d" % (hour, minutes, seconds))


if __name__ == "__main__":
    import sys

    app = QApplication([])
    myapp = Cronometro()
    myapp.show()

    sys.exit(app.exec_())
