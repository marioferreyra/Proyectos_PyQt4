# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


ALPHABET_MIN = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_MAY = ALPHABET_MIN.upper()


class CipherVigenere(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("cipher_vigenere.ui", self)

        self.mainText.setText("")
        self.resultText.setText("")

        # Conexions
        self.btnAction.clicked.connect(self.action)

    def action(self):
        if self.radioEncrypt.isChecked():
            self.cipher(self.mainText.toPlainText(), self.lineKey.text())
        if self.radioDecrypt.isChecked():
            self.decipher(self.mainText.toPlainText(), self.lineKey.text())

    def cipher(self, plain_text, key):
        cipher_text = ""

        i = 0
        for letter in plain_text:
            x = ALPHABET_MIN.find(letter)
            if x == -1:
                x = ALPHABET_MAY.find(letter)
                if x == -1:
                    cipher_text += letter
                else:
                    k = ALPHABET_MIN.find(key[i % len(key)])
                    mod = (x + k) % len(ALPHABET_MAY)  # E(x,k) = x + k mod 26
                    cipher_text += ALPHABET_MAY[mod]
                    i += 1
            else:
                k = ALPHABET_MIN.find(key[i % len(key)])
                mod = (x + k) % len(ALPHABET_MIN)  # E(x,k) = x + k mod 26
                cipher_text += ALPHABET_MIN[mod]
                i += 1

        self.resultText.setText(cipher_text)

    def decipher(self, cipher_text, key):
        plain_text = ""

        i = 0
        for letter in cipher_text:
            x = ALPHABET_MIN.find(letter)
            if x == -1:
                x = ALPHABET_MAY.find(letter)
                if x == -1:
                    plain_text += letter
                else:
                    k = ALPHABET_MIN.find(key[i % len(key)])
                    mod = (x - k) % len(ALPHABET_MAY)  # D(x,k) = x - k mod 26
                    plain_text += ALPHABET_MAY[mod]
                    i += 1
            else:
                k = ALPHABET_MIN.find(key[i % len(key)])
                mod = (x - k) % len(ALPHABET_MIN)  # D(x,k) = x - k mod 26
                plain_text += ALPHABET_MIN[mod]
                i += 1

        self.resultText.setText(plain_text)


if __name__ == "__main__":
    import sys

    app = QApplication([])
    myapp = CipherVigenere()
    myapp.show()

    sys.exit(app.exec_())
