#!/usr/bin/env python
import pyfirmata2
import time

print("Arduino conectado por USB.")
board = pyfirmata2.Arduino('COM3')

while True:
    print("Introduzca un valor para el pin digital, es decir, 0 o 1 (o ingrese 's' para salir): ", end="")
    user_input = input().lower()  #Convertimos la entrada del usuario a minúsculas utilizando el método lower() 
                                  #para que podamos compararla tanto con "s" como con "S" de manera insensible a mayúsculas y minúsculas.

    if user_input == 's':  #Opción de parar y salir del programa
        print("Apagando el LED y saliendo del programa.")
        board.digital[4].write(0)  # Apagar el LED antes de salir
        break #Rompe el bucle
    #Intenta convertir la entrada del usuario a un número entero
    try:
        pindigi = int(user_input)
    #Si ocurre un error al intentar convertir la entrada a un entero, se maneja aquí
    except ValueError:
        #Mostrar un mensaje de error si la entrada no es numérica
        print("Por favor, introduzca 's' para salir o 0 o 1 para el pin digital.")
        #Continuar con la siguiente iteración del bucle
        continue
    
    #Si la entrada es numérica pero no está en el rango válido [0, 1], se ve aquí
    if pindigi not in [0, 1]: #Esta condición verifica si el valor introducido por el usuario no está en la lista [0, 1], es decir, si no es 0 ni 1.
                              #De esta manera, si el usuario introduce un valor como 8, la condición será verdadera y se solicitará al usuario que introduzca el valor nuevamente.
        print("El valor introducido no es válido. Por favor, introduzca 0 o 1 para el pin digital (o 's' para salir).") #Muestra un mensaje de error si la entrada no es válida
        continue
    
    #Si la entrada es válida, se escribe el valor en el pin digital 13 en este caso
    board.digital[4].write(pindigi)
    #Muestra un mensaje si el led está encendido o apagado
    if pindigi == 1:
        print("Led encendido.")
    else:
        print("Led apagado.")

    time.sleep(1)

board.exit()
