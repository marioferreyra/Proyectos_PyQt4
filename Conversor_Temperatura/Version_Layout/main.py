# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from temperaturas import *


class Conversor(QWidget):
    """
    Ventana del conversor, con un lineEdit para ingresar la temperatura y un
    comboBox para elegir la escala de temperatura y labels que muestran el
    resultado de la conversion.
    """
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Conversor de temperaturas")
        self.resize(400, 200) # Tamaño inicial de la ventana
        self.move(500, 500) # Mover ventana a una posicion de la pantalla
        self.setWindowIcon(QIcon("./../img/icon.jpeg"))
        # Widget's
        self.label = QLabel("Ingrese la temperatura y seleccione una escala", self)
        self.grados_celsius = QLabel("")
        self.grados_kelvin = QLabel("")
        self.grados_fahrenheit = QLabel("")
        self.grados_celsius.hide()
        self.grados_kelvin.hide()
        self.grados_fahrenheit.hide()

        self.combo = QComboBox() # ComboBox de temperaturas

        escalas = ["Grados Celsius", "Grados Kelvin", "Grados Fahrenheit"]

        for escala in escalas:
            self.combo.addItem(escala)

        self.temperatura = QLineEdit()

        self.boton_calcular = QPushButton("Calcular") # Calcula temperaturas
        self.boton_salir = QPushButton("Salir") # Sale del programa

        # Layout's
        self.vbox = QVBoxLayout(self) # Layout Vertica
        self.hbox = QHBoxLayout(self) # Layout Horizontal

        self.setLayout(self.vbox)

        # Metemos los Widget's en los Layout's
        self.vbox.addWidget(self.label)

        self.hbox.addWidget(self.temperatura)
        self.hbox.addWidget(self.combo)

        self.vbox.addLayout(self.hbox)

        self.vbox.addWidget(self.boton_calcular)
        self.vbox.addWidget(self.grados_celsius)
        self.vbox.addWidget(self.grados_kelvin)
        self.vbox.addWidget(self.grados_fahrenheit)
        self.vbox.addWidget(self.boton_salir)

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
