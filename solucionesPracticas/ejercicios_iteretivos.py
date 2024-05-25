"""En una escuela, luego de tomar un determinado examen, 
es necesario calcular el promedio de notas 
(las notas van de 0 a 10) de los alumnos de un curso. 
Se necesita saber si el rendimiento ha sido elevado
(el promedio es mayor a 8), aceptable 
(el promedio está comprendido entre 6 y 8)
o bajo (promedio es inferior a 6).
Desarrollar un algoritmo que resuelva este problema.
Para tener en cuenta: las autoridades del colegio 
saben cuántos estudiantes del curso han rendido el examen."""

#analicis: datos de entrada notas (del 0 al 10) y cantidad de alumnos,escala de rendimiento
 #         proceso: paso 1. calcular promedio
 #                  paso 2. Evaluar promedio elevado,aceptable, bajo 
 #                  salida: muestra nivel de rendimiento
"""
analicis
escribir y leer numero de estudiantes
designar acumulador=0
recorrer i en un rango (numero de estudiantes ingresados) 
buble while repite pidiendo las notas, segun el numero de estudiantes ingresado
if para evaluar que las notas ingresadas enten entre 0 y 10
sino emite error de ingreso notas
se coloca acumulador para ir sumando las notas y obtener un solo numero.

calcular promedio: la suma de la notas / numero de alumnos
para analiza el promedio if elevedo, elif aceptable, else bajo
 print resultado y promedio.
 
"""

print("Este programa te ayudara a calcular el promedio de un curso y evaluar el rendimiento general.")

numeroEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))
acumulador = 0
for i in range(numeroEstudiantes):
  while True:
    nota = float(input("Ingrese una nota (entre 0 y 10): "))
    if 0 <= nota <= 10:
      break
    else:
      print("Error: la nota debe estar entre 0 y 10.")
  acumulador += nota

promedio = acumulador / numeroEstudiantes

if promedio > 8:
  rendimiento = "elevado"
elif 6 <= promedio <= 8:
  rendimiento = "aceptable"
else:
  rendimiento = "bajo"

print("Promedio:", promedio)
print("Rendimiento:", rendimiento)
