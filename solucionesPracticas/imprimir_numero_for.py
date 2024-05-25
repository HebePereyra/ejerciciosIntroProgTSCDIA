""" Desarrollar en Python las siguientes consignas utilizando la estructura iterativas adecuada para
cada uno de estos casos:
1. Mostrar los números desde el 0 al número solicitado al usuario (input)
datos de entrada: desde 0 (incluido)"""

#proceso: _pedir numero a usuario del 5 al 12 (pongo un rango para que haya un minimo y maximo de impreciones)
         #_verificar que lo ingresado sea un numero valido. (si no es valido retorne a la pregunta)
         #_Con un For recorrer desde el 0 hasta el numero ingresado e imprimir.
#salida. muestra 0,1,2,... hasta numero ingresado
"""
iniciar: algoritmo_numeros

Mostrar mensaje:

Imprimir: "Mostraremos impreso desde el 0 hasta un numero de su eleccion."
Solicitar número:

Solicitar al usuario que ingrese un número entero: suNumero = int(input("Ingrese un número del 5 al 12: "))
Validar número:

Si suNumero es menor que 5 o mayor que 12:
Imprimir: "El numero ingresado no es valido. "
Salir del algoritmo.
Imprimir números:

Si el número es válido:
Recorrer los números desde 0 hasta suNumero:
Para cada número i:
Imprimir: print(i)
Salir del algoritmo."""

print("Mostraremos impreso desde el 0 hasta un numero de su eleccion.")
 
suNumero=int(input("Ingrese un número del 5 al 12: "))

if suNumero >= 5 and suNumero <= 12:
    for i in range(0, suNumero + 1):
        print(i)
else: 
    print("El numero ingresado no es valido. ")
    
       


#2. Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para
#saber si un número es par hacer i % 2 == 0)

#repito mismo procedimiento, por el for in range le agrego que vaya de a dos numero
print("Mostraremos los numeros pares desde 0 hasta su numero")
suNumero=int(input("Ingrese un número menos a 30: "))

if suNumero <= 30:
    for i in range(0, suNumero + 1,2):
        print(i)
else: 
    print("El numero ingresado no es valido. ")
    


