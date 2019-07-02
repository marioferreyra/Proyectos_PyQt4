# -*- coding: utf-8 -*-

ALPHABET_MIN = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_MAY = ALPHABET_MIN.upper()


def cipher(plain_text, key):
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

    return cipher_text


def decipher(cipher_text, key):
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

    return plain_text


if __name__ == '__main__':
    print("### Mode Cipher ###")
    plain_text = raw_input("Plain Text: ")
    key = raw_input("Key: ").lower()
    print("--> Cipher Text: {}".format(cipher(plain_text, key)))

    print("\n### Mode Decipher ###")
    cipher_text = raw_input("Cipher Text: ")
    key = raw_input("Key: ").lower()
    print("--> Plain Text: {}".format(decipher(cipher_text, key)))
