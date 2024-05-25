#3. Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de
#lo que ingresa sea “fin”
#En cada caso utilizar el bucle que considere adecuado:
#mientras (while) o para (for)

#entrada: input con nombre
#proceso: bucle while que repita hasta que se cumpla la condicion fin
#salida: print de nombre las veces que se repita
"""
pseudocodigo:
Inicializar:

Lista nombres vacía
Ciclo:

Repetir mientras:
nombre no sea "fin"
Dentro del ciclo:
Solicitar al usuario que ingrese un nombre: nombre = input("Ingrese un nombre (o escriba 'fin' para terminar): ")
Si nombre es "fin":
Salir del ciclo: break
Sino:
Agregar el nombre a la lista: nombres.append(nombre)
Mostrar nombres:

Imprimir un mensaje: "Nombres ingresados:"
Recorrer la lista nombres:
Para cada nombre en la lista:
Imprimir el nombre: print(nombre)
Fin del programa:

Imprimir un mensaje: "Fin del programa"""

print("Este programa imprime nombres.")

nombre=""
while nombre != "fin":
    nombre= input("ingresa diferentes nombres, si deseas terminar, ingresa fin. ")
    if nombre != "fin":
     print(f"Ud. ingreso {nombre}")
print ("ud ha finalizado este programa")




