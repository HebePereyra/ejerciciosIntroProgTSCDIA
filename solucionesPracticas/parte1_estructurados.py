"""Actividades parte 1: Iniciando
Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:
Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 
Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo
Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.
En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)

Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.

Nota: para saber si el número i es par hacer i % 2 == 0"""
"""
print("Pedir 10 nombres")

nombresPersonas = []

for i in range(10):
    while True:
        nombre = input("Ingrese un nombre (no repetido): ").strip()
        if nombre not in nombresPersonas:
            nombresPersonas.append(nombre)
            break
        else:
            print("Error: El nombre ya se encuentra en la lista.")

print("Nombres:")
for nombre in nombresPersonas:
    print(f"- {nombre}")


print("**********************************************************")
print("Eliminar la tercer y la última persona de la lista del ejercicio 1")
print("luego ordenar la lista y mostrarlo")

del nombresPersonas[2]
del nombresPersonas[-1]
nombresPersonas.sort()
print (nombresPersonas)
"""
"""
print("Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.")


persona = {
    "nombre": "Hebe",
    "apellido": "Pereyra",
    "dni": 11111111,
    "email": "hebe@email.com",
    "fecha_nacimiento": "12/07/1987"
}


print(persona["nombre"])  # Accede a los datos del diccionario
print(persona["apellido"]) 
print(persona["dni"])  
print(persona["email"]) 
print(persona["fecha_nacimiento"])  


persona["email"] = "hebecorreo@email.com"  # Modifica los datos del diccionario
print(persona["email"])  


persona["telefono"] = 155123456 # Agrega telefono al diccionario
print(persona)  

print("En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)")
"""
#creacion a partir de otro diccionario

datosMama = {
    "nombre": "lucia",
    "apellido": "Pereyra",
    "dni": 11111111,
    "email": "lucia@email.com",
    "fecha_nacimiento": "12/07/1987"
}
datosPapa = {
    "nombre": "Juan",
    "apellido": "Rut",
    "dni": 22222222,
    "email": "juan@email.com",
    "fecha_nacimiento": "23/09/1984"
}
datosHijoMayor={
    "nombre": "Lucas",
    "apellido": "Rut",
    "dni": 33333333,
    "email": "lucas@email.com",
    "fecha_nacimiento": "23/03/2005"
}
datosHijoMenor={
    "nombre": "Matias",
    "apellido": "Rut",
    "dni": 34444444,
    "email": "matias@email.com",
    "fecha_nacimiento": "11/01/2007"
}
familia={"mama":datosMama, "papa":datosPapa,"hijoMayor":datosHijoMayor,"hijoMenor":datosHijoMenor}

print(familia)



""" probando algo mas
# programa para que puedas cargar tu familia

integrantesFamilia=int(input(" ingresa cantidad de personas que componen tu familia."))

integrante=""
while integrante!= "no" :
    orden=input("Desea agregar integrante? si/no: ")

    if orden =="si":   #falta validar todos los datos!
       
        nombre=input("Nombre")
        apellido=input("Apellido")
        dni=int(input("Numero dni"))
        email=input("Email")
        fechaNacimiento=input("Fecha de Nacimiento formato:dd/mm/yy")
    
        datos=[nombre,apellido,dni,email,fechaNacimiento]
        continue #deja cargar varios parientes
    else:
       print ("ud finalizo el programa")
    break

#esto crea un diccionario pero del ultimo dato ingresado.ver
claves=["nombre","apellido","dni","email","fechaNacimiento"]
familia=dict (zip(claves,datos))  

print(familia)"""