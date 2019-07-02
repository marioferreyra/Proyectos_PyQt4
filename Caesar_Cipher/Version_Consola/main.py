# -*- coding: utf-8 -*-

ALPHABET_MIN = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_MAY = ALPHABET_MIN.upper()


def cipher(plain_text, key):
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

    return cipher_text


def decipher(cipher_text, key):
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

    return plain_text


if __name__ == "__main__":
    print("### Mode Cipher ###")
    plain_text = raw_input("Plain Text: ")
    key = int(raw_input("Key: "))
    print("--> Cipher Text: {}".format(cipher(plain_text, key)))

    print("\n### Mode Decipher ###")
    cipher_text = raw_input("Cipher Text: ")
    key = int(raw_input("Key: "))
    print("--> Plain Text: {}".format(decipher(cipher_text, key)))
