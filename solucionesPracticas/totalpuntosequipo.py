print("Calculemos los puntos de tu equipo!")

totalPartidos=int(input("Ingrese el Total de partidos jugados hasta hoy: "))

cantpartidoGanados=int(input("Ingrese el Total de partidos ganados: "))
cantpartidoEmpatados=int(input("Ingrese el Total de partidos empatados: "))
cantpartidoPerdidos=int(input("Ingrese el Total de partidos perdidos: "))
 
total_partidosingresados=cantpartidoGanados+cantpartidoEmpatados+cantpartidoPerdidos

if totalPartidos == total_partidosingresados:
    totalPuntos=(cantpartidoGanados*3)+(cantpartidoEmpatados*1)

    print(f"El total de puntos es: {totalPuntos}")

if totalPartidos> total_partidosingresados:

    faltadato=totalPartidos-total_partidosingresados
    print(f"No podemos calcular el total de puntos. Faltan ingresar {faltadato}resultado/s")
    
if totalPartidos<total_partidosingresados:

    sobradato=total_partidosingresados-totalPartidos
    print(f"No podemos calcular el total de puntos, has ingresado {sobradato}resultado/s de mas. ")
    
	

	
"""Escribir cantpartidoGanado
	Leer cantpartidoGanado
	Escribir cantpartidoEmpatado
	Leer cantpartidoEmpatado
	Escribir cantpartidoPerdido
	Leer cantpartidoPerdido
	
	totalPuntos=(cantpartidoGanado*3)+(cantpartidoEmpatado*1)
	
	Mostrar totalPuntos"""
	
	