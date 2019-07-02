# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4 import uic
from temperaturas import *


class Conversor(QWidget):
    """
    Ventana del conversor, con un lineEdit para ingresar la temperatura y un
    comboBox para elegir la escala de temperatura y labels que muestran el
    resultado de la conversion.
    """
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("conversor.ui", self)

        self.grados_celsius.hide()
        self.grados_kelvin.hide()
        self.grados_fahrenheit.hide()

        # Conexion
        self.boton_calcular.clicked.connect(self.calcular)
        self.boton_salir.clicked.connect(self.close)

    def calcular(self):
        """
        Calcula la conversion de temperaturas.
        """
        temperatura = float(self.temperatura.text())
        escala = str(self.combo.currentText())

        if escala == "Grados Celsius":
            self.grados_celsius.hide()
            self.grados_kelvin.setText("%.4f Grados Kelvin" % celsiusToKelvin(temperatura))
            self.grados_fahrenheit.setText("%.4f Grados Fahrenheit" % celsiusToFahrenheit(temperatura))
            self.grados_kelvin.show()
            self.grados_fahrenheit.show()
        elif escala == "Grados Kelvin":
            self.grados_kelvin.hide()
            self.grados_celsius.setText("%.4f Grados Celsius" % kelvinToCelsius(temperatura))
            self.grados_fahrenheit.setText("%.4f Grados Fahrenheit" % kelvinToFahrenheit(temperatura))
            self.grados_celsius.show()
            self.grados_fahrenheit.show()
        elif escala == "Grados Fahrenheit":
            self.grados_fahrenheit.hide()
            self.grados_celsius.setText("%.4f Grados Celsius" % fahrenheitToCelsius(temperatura))
            self.grados_kelvin.setText("%.4f Grados Kelvin" % fahrenheitToKelvin(temperatura))
            self.grados_celsius.show()
            self.grados_kelvin.show()


if __name__ == "__main__":
    import sys

    app = QApplication([])
    myapp = Conversor()
    myapp.show()

    sys.exit(app.exec_())
