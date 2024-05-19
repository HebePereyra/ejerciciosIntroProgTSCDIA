"""Una despensa de barrio vende la leche de vaca entera
 de litro a 1000 pesos la unidad. Si el cliente compra
más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%.
Si compra más de 24 unidades, el descuento es del 15%.
Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento 
(si posee otros descuentos, se suma los descuentos). 
Desarrolle una solución 
algorítmica para saber cuento debe pagar el cliente"""


lecheUnidades = int(input(" Unidades de leche a comprar: "))
jubilado= int(input("Si el cliente es jubilado ingrese 1: "))

precioLeche= 1000
montoTotal= lecheUnidades * precioLeche
if lecheUnidades<=12 and jubilado==1:
    descuentoJubilado={montoTotal}-({montoTotal*0.10})
    print(f" Ud debe abonar:{descuentoJubilado} ")

if jubilado==1 and (lecheUnidades>12 and lecheUnidades<=24):
    montoDescuento20= montoTotal -(montoTotal*0.20)
    print(f"El monto a abonar con 20% de descuento es: {montoDescuento20}")
elif jubilado==1 and (lecheUnidades>24):
    montoDescuento25= montoTotal -(montoTotal*0.25)
    print(f"El monto a abonar con 25% de descuento es: {montoDescuento25}")
if (lecheUnidades>12 and lecheUnidades<=24) and jubilado!=1:
    montoDescuento10= montoTotal - (montoTotal* 0.10)
    print(f"El monto a abonar con 10% de descuento es: {montoDescuento10}")
if lecheUnidades>24 and jubilado!=1:
    montoDescuento15= montoTotal -(montoTotal*0.15)   
    print(f"El monto a abonar con 15% de descuento es: {montoDescuento15}")
elif lecheUnidades<=12 and jubilado!=1: 
    print(f"El monto total es: {montoTotal}")

