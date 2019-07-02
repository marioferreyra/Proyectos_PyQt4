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

        # Conexiones
        self.boton_salir.clicked.connect(self.close)
        self.calor.textChanged.connect(self.calcular)
        self.combo.currentIndexChanged.connect(self.calcular)

        self.temperaturaInicial()

    def temperaturaInicial(self):
        """
        Setea todas las escalas a 0 grados.
        """
        self.grados_celsius.setText("%.4f Grados Celsius" % float(0))
        self.grados_kelvin.setText("%.4f Grados Kelvin" % float(0))
        self.grados_fahrenheit.setText("%.4f Grados Fahrenheit" % float(0))

    def calcular(self):
        """
        Calcula la conversion de temperaturas.
        """
        if len(self.calor.text()) == 0:
            self.temperaturaInicial()
        else:
            temperatura = float(self.calor.text())

            escala = str(self.combo.currentText())

            if escala == "Grados Celsius":
                self.grados_celsius.setText("%.4f Grados Celsius" % temperatura)
                self.grados_kelvin.setText("%.4f Grados Kelvin" % celsiusToKelvin(temperatura))
                self.grados_fahrenheit.setText("%.4f Grados Fahrenheit" % celsiusToFahrenheit(temperatura))
            elif escala == "Grados Kelvin":
                self.grados_celsius.setText("%.4f Grados Celsius" % kelvinToCelsius(temperatura))
                self.grados_kelvin.setText("%.4f Grados Kelvin" % temperatura)
                self.grados_fahrenheit.setText("%.4f Grados Fahrenheit" % kelvinToFahrenheit(temperatura))
            elif escala == "Grados Fahrenheit":
                self.grados_celsius.setText("%.4f Grados Celsius" % fahrenheitToCelsius(temperatura))
                self.grados_kelvin.setText("%.4f Grados Kelvin" % temperatura)
                self.grados_fahrenheit.setText("%.4f Grados Fahrenheit" % kelvinToFahrenheit(temperatura))


if __name__ == "__main__":
    import sys

    app = QApplication([])
    myapp = Conversor()
    myapp.show()

    sys.exit(app.exec_())
