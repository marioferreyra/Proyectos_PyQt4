# -*- coding: utf-8 -*-

import os
from temperaturas import *


def print_menu():
    """
    Imprime un menu de opciones
    """
    # os.system('clear')
    print("\nElija la escala de temperatura que va ingresar.")
    print("Las opciones son: ")
    print("*************************")
    print("*\t1: Kelvin\t*")
    print("*\t2: Celsius\t*")
    print("*\t3: Fahrenheit\t*")
    print("*\t0: SALIR\t*")
    print("*************************")

    opcion = raw_input("Introduzca su elección: ")

    return opcion

flag = True
while flag:
    opcion = print_menu()
    opcion = int(opcion)
    if opcion in range(0, 4):
        if opcion != 0:
            x = raw_input("Ingrese la temperatura que desea convertir: ")
            x = float(x)

        if opcion == 1:
            print("Grados Kelvin: %f" % x)
            print("Grados Celsius: %f" % kelvinToCelsius(x))
            print("Grados Fahrenheit: %f" % kelvinToFahrenheit(x))
        elif opcion == 2:
            print("Grados Celsius: %f" % x)
            print("Grados Kelvin: %f" % celsiusToKelvin(x))
            print("Grados Fahrenheit: %f" % celsiusToFahrenheit(x))
        elif int(opcion) == 3:
            print("Grados Fahrenheit: %f" % x)
            print("Grados Celsius: %f" % fahrenheitToCelsius(x))
            print("Grados Kelvin: %f" % fahrenheitToKelvin(x))
        elif opcion == 0:
            print "Finalizando...\n"
        flag = False
    else:
        print("Opcion Invalida")
