# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

ONE_SECOND = 1000 # 1000 ms = 1 s

class Temporizador(QWidget):
    """
    Ventana de un temporizador, con opciones para setear el tiempo, iniciar,
    pausar y resetear.
    """
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("temporizador.ui", self)

        self.timer = QTimer()
        self.tick = 0 # Segundos transcurridos

        # Tiempo que se setea
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Estado inicial de los botones
        self.btnStart.setEnabled(False)
        self.btnReset.setEnabled(False)

        # Conexiones
        self.timer.timeout.connect(self.updateLCD)
        self.btnExit.clicked.connect(self.close)
        self.btnSet.clicked.connect(self.setTime)
        self.btnStart.clicked.connect(self.start)
        self.btnReset.clicked.connect(self.reset)

        self.lcd.display("00:00:00")

    def start(self):
        """
        Inicia el Temporizador.
        """
        if not self.isTimerActive():
            self.btnSet.setEnabled(False)
            self.btnReset.setEnabled(False)
            self.timer.start(ONE_SECOND)
            self.btnStart.setText("Stop")
        else:
            self.btnSet.setEnabled(True)
            self.btnReset.setEnabled(True)
            self.timer.stop()
            self.btnStart.setText("Start")

    def reset(self):
        """
        Resetea el Temporizador.
        """
        self.btnStart.setEnabled(True)
        self.btnStart.setText("Start")
        
        self.timer.stop()
        
        self.tick = self.hours*3600 + self.minutes*60 + self.seconds
        self.lcd.display("%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds))

    def updateLCD(self):
        """
        Actualiza el tiempo del LCD.
        Cuando llega a 00:00:00, se muestra un aviso.
        """
        if self.tick != 0:
            self.tick -= 1

            hour = self.tick / 3600
            minute = (self.tick % 3600) / 60
            second = (self.tick % 3600) % 60

            self.lcd.display("%02d:%02d:%02d" % (hour, minute, second))
        else:
            self.timer.stop()
            self.btnSet.setEnabled(True)
            self.btnStart.setEnabled(False)
            self.btnReset.setEnabled(True)
            self.btnStart.setText("Start")
            QMessageBox.warning(self,"Aviso","### ALARM ###")


    def setTime(self):
        """
        Setea el Tiempo establecido en el LCD.
        """
        self.btnStart.setEnabled(True)
        self.btnReset.setEnabled(True)
        
        t = self.time.time()

        self.hours = t.hour()
        self.minutes = t.minute()
        self.seconds = t.second()
        
        self.tick = self.hours*3600 + self.minutes*60 + self.seconds

        self.lcd.display(t.toString())

    def isTimerActive(self):
        """
        Retorna True si el temporizador (timer) esta activo.
        """
        return self.timer.isActive()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myapp = Temporizador()
    myapp.show()

    sys.exit(app.exec_())
