# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4 import uic
import math
import __future__  # Para que 'eval' pueda hacer calculos con float


class Calculadora(QWidget):
    """
    Ventana que muestra una calculadora.
    """
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("calculadora.ui", self)

        # Conexiones de los botones
        self.btn0.clicked.connect(lambda: self.agregar("0"))
        self.btn1.clicked.connect(lambda: self.agregar("1"))
        self.btn2.clicked.connect(lambda: self.agregar("2"))
        self.btn3.clicked.connect(lambda: self.agregar("3"))
        self.btn4.clicked.connect(lambda: self.agregar("4"))
        self.btn5.clicked.connect(lambda: self.agregar("5"))
        self.btn6.clicked.connect(lambda: self.agregar("6"))
        self.btn7.clicked.connect(lambda: self.agregar("7"))
        self.btn8.clicked.connect(lambda: self.agregar("8"))
        self.btn9.clicked.connect(lambda: self.agregar("9"))
        self.btnPunto.clicked.connect(lambda: self.agregar("."))
        self.btnSuma.clicked.connect(lambda: self.agregar("+"))
        self.btnResta.clicked.connect(lambda: self.agregar("-"))
        self.btnMulti.clicked.connect(lambda: self.agregar("*"))
        self.btnDiv.clicked.connect(lambda: self.agregar("/"))
        self.btnCuadrado.clicked.connect(lambda: self.parcial("Cuadrado"))
        self.btnRaiz.clicked.connect(lambda: self.parcial("Raiz"))
        self.btnParOpen.clicked.connect(lambda: self.agregar("("))
        self.btnParClose.clicked.connect(lambda: self.agregar(")"))
        self.btnAC.clicked.connect(lambda: self.expre.clear())
        self.btnDEL.clicked.connect(self.delete)
        self.btnIgual.clicked.connect(self.evaluar)

    def delete(self):
        """
        Borra el ultimo caracter de la cadena.
        """
        anterior = self.expre.text()[:-1]
        self.expre.setText(anterior)

    def parcial(self, operacion):
        """
        Calcula el cuadrado o la raiz de la expresion.
        """
        x = self.expre.text()
        try:
            tmp = eval(str(x))
        except NameError:
            pass
        else:
            if type(tmp) in [int, float]:
                if operacion == "Cuadrado":
                    res = math.pow(float(tmp), 2)
                elif operacion == "Raiz":
                    res = math.sqrt(float(tmp))
                if type(res) in [int, float]:
                    self.expre.setText(str(res))

    def agregar(self, cosa):
        """
        Agrega caracteres a la cadena para su posterior evaluacion.
        """
        actual = self.expre.text()
        self.expre.setText(actual + cosa)

    def evaluar(self):
        """
        Evalua la cadena/expresion y setea el QLineText con ese valor.
        """
        x = self.expre.text()
        try:
            # resultado = eval(str(x))
            resultado = eval(compile(str(x),
                                     '<string>',
                                     'eval',
                                     __future__.division.compiler_flag))
        except NameError:
            pass
        else:
            if type(resultado) in [int, float]:
                self.expre.setText(str(resultado))


if __name__ == "__main__":
    import sys

    app = QApplication([])
    myapp = Calculadora()
    myapp.show()

    sys.exit(app.exec_())
