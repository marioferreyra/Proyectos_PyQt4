# -*- coding: utf-8 -*-

from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfilename


TAMANO = 'z'
BUSCAR = 's'
AGREGAR = 'a'
BORRAR = 'd'
VACIAR = 'e'
MOSTRAR = 'h'
DUPLICAR = 'c'
CARGAR = 'l'
GUARDAR = 'u'
FINALIZAR = 'q'

def print_menu():
    """
    Imprime el menu de opciones.
    """
    print("Elija lo que quiera hacer.")
    print("Las opciones son:")
    print("*****************************************************************")
    print("*\tz: Mostrar el tamaño del diccionario en uso.    \t*")
    print("*\ts: Buscar una definicion para una palabra dada. \t*")
    print("*\ta: Agregar una palabra con su definicion.       \t*")
    print("*\td: Borrar una palabra.                          \t*")
    print("*\te: Vaciar el diccionario.                       \t*")
    print("*\th: Mostrar el diccionario actual.               \t*")
    print("*\tc: Duplicar el diccionario actual.              \t*")
    print("*\tl: Cargar un nuevo diccionario desde un archivo.\t*")
    print("*\tu: Guardar el diccionario actual en un archivo. \t*")
    print("*\tq: Finalizar                                    \t*")
    print("*****************************************************************")

    opcion = raw_input("Introduzca su elección: ")

    return opcion

def imprimir_diccionario(diccionario):
    """
    Imprime el diccionario pasado como parametro
    """
    for k, v in diccionario.items():
        print("%s : %s" % (k, v))

flag = True
diccionario = dict() # Diccionario vacio
print("\n*** Bienvenido al Diccionario ***")
while flag:
    opcion = print_menu()
    if opcion == TAMANO:
        print("-> El tamaño es: %d" % len(diccionario))

    elif opcion == BUSCAR:
        palabra = raw_input("Por favor, ingrese la palabra a buscar en el diccionario: ")
        if palabra in diccionario:
            print("La definicion de '%s' es: '%s'." % (palabra, diccionario[palabra]))
        else:
            print("La palabra %s no exite en el diccionario." % palabra)

    elif opcion == AGREGAR:
        palabra = raw_input("Por favor, ingrese la palabra a añadir al diccionario: ")
        if palabra in diccionario:
            print("La palabra '%s' ya existe en el diccionario.")
        else:
            definicion = raw_input("Por favor ingrese la definicion: ")
            diccionario[palabra] = definicion
            print("La palabra y su definicion fueron agregadas con exito")

    elif opcion == BORRAR:
        palabra = raw_input("Por favor, ingrese la palabra que desea eliminar del diccionario: ")
        if palabra in diccionario:
            del diccionario[palabra]
            print("-> La palabra '%s' fue eliminada." % palabra)
        else:
            print("-> la palabra '%s' no existe." % palabra)

    elif opcion == VACIAR:
        diccionario.clear()
        print("-> El diccionario fue vaciado.")

    elif opcion == MOSTRAR:
        imprimir_diccionario(diccionario)

    elif opcion == DUPLICAR:
        diccionario_tmp = diccionario.copy()
        print("El diccionario fue duplicado.\nMostrando el diccionario duplicado:")
        imprimir_diccionario(diccionario)

    elif opcion == CARGAR:
        # import ipdb; ipdb.set_trace()
        # filename = raw_input("Por favor, ingrese el nombre del diccionario a cargar: ")
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        name_file = filename.split('/')[-1]
        diccionario.clear()
        diccionario = dict()
        with open(filename, "r") as f:
            for line in f:
                key, separator, val = line.split()
                diccionario[key] = val
        print("El diccionario '%s' fue cargado con exito" % name_file)

    elif opcion == GUARDAR:
        # filename = raw_input("¿Como quiere llamar el archivo a guardar?: ")
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = asksaveasfilename() # show an "Save" dialog box and return the path to the selected file
        name_file = filename.split('/')[-1]
        with open(filename, "w") as f:
            for c, v in diccionario.items():
                a = "%s : %s\n" % (c, v)
                f.write(a)
        print("El diccionario '%s' fue creado con exito" % name_file)

    elif opcion == FINALIZAR:
        print("Finalizando...")
        flag = False

    else:
        print("Opcion Invalida")
    print("\n")
