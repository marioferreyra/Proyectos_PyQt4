# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


ALPHABET_MIN = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_MAY = ALPHABET_MIN.upper()


class CipherCesar(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("cipher_cesar.ui", self)

        self.mainText.setText("")
        self.resultText.setText("")

        # Conexions
        self.btnAction.clicked.connect(self.action)

    def action(self):
        if self.radioEncrypt.isChecked():
            self.cipher(self.mainText.toPlainText(), self.spinKey.value())

        if self.radioDecrypt.isChecked():
            self.decipher(self.mainText.toPlainText(), self.spinKey.value())

    def cipher(self, plain_text, key):
        cipher_text = ""

        for letter in plain_text:
            x = ALPHABET_MIN.find(letter)  # Si no esta en alphabet devuelve -1
            if x == -1:
                x = ALPHABET_MAY.find(letter)  # Si no esta en alphabet devuelve -1
                if x == -1:
                    cipher_text += letter
                else:
                    mod = (x + key) % len(ALPHABET_MAY)  # E(x,k) = x + k mod 26
                    cipher_text += ALPHABET_MAY[mod]
            else:
                mod = (x + key) % len(ALPHABET_MIN)  # E(x,k) = x + k mod 26
                cipher_text += ALPHABET_MIN[mod]

        self.resultText.setText(cipher_text)

    def decipher(self, cipher_text, key):
        plain_text = ""

        for letter in cipher_text:
            x = ALPHABET_MIN.find(letter)  # Si no esta en alphabet devuelve -1
            if x == -1:
                x = ALPHABET_MAY.find(letter)  # Si no esta en alphabet devuelve -1
                if x == -1:
                    plain_text += letter
                else:
                    mod = (x - key) % len(ALPHABET_MAY)  # D(x,k) = x - k mod 26
                    plain_text += ALPHABET_MAY[mod]
            else:
                mod = (x - key) % len(ALPHABET_MIN)  # D(x,k) = x - k mod 26
                plain_text += ALPHABET_MIN[mod]

        self.resultText.setText(plain_text)


if __name__ == "__main__":
    import sys

    app = QApplication([])
    myapp = CipherCesar()
    myapp.show()

    sys.exit(app.exec_())
