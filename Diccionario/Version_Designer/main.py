# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


class AddDialog(QDialog):
    """
    Ventana de dialogo para el ingreso de una palabra y una definicion.
    """
    newSignal = pyqtSignal(str, str)
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("addDialog.ui", self)

        self.linePalabra.setText("")
        self.lineDefinicion.setText("")

        # Conexiones
        self.btnCancel.clicked.connect(self.close)
        self.btnOk.clicked.connect(self.sendWord)

    def sendWord(self):
        self.newSignal.emit(self.linePalabra.text(), self.lineDefinicion.text())
        self.close()


class Diccionario(QDialog):
    """
    Ventana del diccionario con una tabla y botones con distintas
    funcionalidades.
    """
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dictionary.ui", self)

        self.diccionario = dict()

        # Widget de agregar palabra
        self.add_dialog = AddDialog()
        self.add_dialog.newSignal.connect(self.dictAdd)

        # Conexiones
        self.btnLength.clicked.connect(self.dictLength)
        self.btnSearch.clicked.connect(self.dictSearch)
        self.btnAdd.clicked.connect(self.openDialogAdd)
        self.btnDelete.clicked.connect(self.dictDelete)
        self.btnEmpty.clicked.connect(self.dictEmpty)
        self.btnSave.clicked.connect(self.dictSave)
        self.btnLoad.clicked.connect(self.dictLoad)

        # Tabla
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(QString("Palabra|Definicion").split("|"))

        self.agregarElementos()

        self.tableUpdate()

    def openDialogAdd(self):
        self.add_dialog.show()

    def agregarElementos(self):
        self.diccionario["caniche"] = "Rocco"
        self.diccionario["bestia"] = "Otto"
        self.diccionario["dalmata"] = "Ciro"
        self.diccionario["tortuga"] = "Frankling"

    def tableUpdate(self):
        """
        Actualiza el la tabla con el los elementos actuales del diccionario.
        """
        fila = 0
        self.tableWidget.setRowCount(len(self.diccionario))
        for p, d in self.diccionario.items():
            self.tableWidget.setItem(fila, 0, QTableWidgetItem(p))
            self.tableWidget.setItem(fila, 1, QTableWidgetItem(d))
            fila += 1

    def dictLength(self):
        """
        Devuelve el tamaño del diccionario.
        """
        self.length.setText("El tamaño del diccionario es: " + str(len(self.diccionario)))

    def dictSearch(self):
        """
        Busca una palabra en el diccionario y si esta devuelve la palabra con
        su definicion
        """
        palabra, ok = QInputDialog.getText(self, "Buscar", "Escribe la palabra que desea buscar:")
        if ok and len(palabra) != 0:
            palabra = str(palabra)
            if palabra in self.diccionario:
                self.length.setText("La definicion de '%s' es: '%s'" % (palabra, self.diccionario[palabra]))
            else:
                self.length.setText("La palabra '%s' no exite en el diccionario" % palabra)

    def dictAdd(self, palabra, definicion):
        """
        Agrega una palabra al diccionario, si es que esta no esta ya en él.
        """
        palabra = str(palabra) # Si no casteo no busca las palabras ingresadas
        definicion = str(definicion) # Si no casteo no busca las palabras ingresadas
        if len(palabra) != 0 and len(definicion) != 0:
            if palabra in self.diccionario:
                self.length.setText("La palabra '%s' ya existe en el diccionario" % palabra)
            else:
                self.diccionario[palabra] = definicion
                self.tableUpdate()
                self.length.setText("La palabra y su definicion fueron agregadas con exito")

    def dictDelete(self):
        """
        Borra una palabra del diccionario, si es que esta esta en él.
        """
        palabra, ok = QInputDialog.getText(self, "Borrar", "Escribe la palabra que desea borrar:")
        if ok and (len(palabra) != 0):
            palabra = str(palabra)
            if palabra in self.diccionario:
                del self.diccionario[palabra]
                self.tableUpdate()
                self.length.setText("La palabra '%s' fue eliminada del diccionario" % palabra)
            else:
                self.length.setText("La palabra '%s' no exite en el diccionario" % palabra)

    def dictEmpty(self):
        """
        Vacia el diccionario, es decir, elimina todo su contenido.
        """
        self.diccionario.clear()
        self.tableUpdate()
        self.length.setText("El diccionario fue vaciado con exito")

    def dictSave(self):
        """
        Guarda el diccionario actual en un archivo con el siguiente formato:
        palabra : definicion
        """
        filename = QFileDialog.getSaveFileName(self, "Guardar diccionario")
        if filename:
            with open(filename, "w") as f:
                for c, v in self.diccionario.items():
                    a = "%s : %s\n" % (c, v)
                    f.write(a)
            self.length.setText("El diccionario fue guardado con exito")
            f.close()

    def dictLoad(self):
        """
        Carga un diccionario desde un archivo con el siguiente formato:
        palabra : definicion
        """
        filename = QFileDialog.getOpenFileName(self, "Cargar diccionario")
        self.diccionario.clear()
        if filename:
            with open(filename, "r") as f:
                for line in f:
                    key, separator, value = line.split()
                    self.diccionario[key] = value
                self.tableUpdate()
            self.length.setText("El diccionario fue cargado con exito")
            f.close()


if __name__ == "__main__":
    import sys

    app = QApplication([])
    myapp = Diccionario()
    myapp.show()

    sys.exit(app.exec_())
