'''
Estudiante: Andrés Elías Forero Garzón.
Código: 202010024601.
Clase: Programación básica.
Profesor: Omar Ernesto Torres Ladino.
'''
"""
#Script que calcule el área de un triángulo usando la fórmula general: (b*h)/2
base=0
altura=0
area=0;

base=float(input("Ingrese el valor de la base: "))
altura=float(input("Ingrese el valor de la altura: "))

area=(base*altura)/2

print(f"El area del triangulo de la altura {altura} y la base {base} es {area}\n")

#Script que calcule cuantos dolares puede comprar una empresa con pesos mexicanos, 1 usd = 20.88
valor_usd=20.88
cantidad_mxn=0
cantidad_usd=0

cantidad_mxn=int(input("Ingrese la cantidad de pesos mexicanos que posee: "))

cantidad_usd=(cantidad_mxn/valor_usd)

print(f"La cantidad de dolares que puede comprar con MXN${cantidad_mxn} es", "USD${0:.2f}\n".format(cantidad_usd)) 

#Script que determine la edad de los aspirantes segun el año de nacimiento, teniendo en cuenta 2020 como año actual.
a_aspirante=0
a_actual=2020
edad=0

a_aspirante=int(input("Ingrese el año de nacimiento del aspirante: "))

edad=(a_actual-a_aspirante)

print(f"La edad del aspirante es {edad}\n")

#Script que determine el cobro por uso de estacionamiento segun la cantidad de horas, teniendo en cuenta las fracciones de hora como completas.
valor_hora=0
cantidad_horas=0
total_cobro=0
x=0

valor_hora=float(input("Ingrese el valor por hora del estacionamiento: "))
cantidad_horas=(float(input("Ingrese la cantidad de horas a cobrar: ")))
x=cantidad_horas

if cantidad_horas%1 != 0:
    cantidad_horas+=1

total_cobro=float(valor_hora*cantidad_horas)

print(f"El total a pagar por {x} horas es ${total_cobro}\n")

#Script que determine el valor a pagar por trabajos de pintura segun la cantidad de m2.
precio_m=0
cantidad_m=0
presupuesto=0

precio_m=float(input("Ingrese el valor del trabajo por metro cuadrado; "))
cantidad_m=float(input("Ingrese la cantidad de metros cuadrados a trabajar; "))

presupuesto=float(precio_m*cantidad_m)

print("{0:.2f} m2 tienen un precio de ${0:.2f}\n".format(cantidad_m,presupuesto)) 

#Script que calcule el valor de la hipotenusa de un triangulo rectangulo usando el Teorema de Pitagoras.
import math
catetoA=0
catetoB=0
hipotenusa=0

catetoA=float(input("Ingrese el valor del cateto 1: "))
catetoB=float(input("Ingrese el valor del cateto 2: "))
hipotenusa=math.sqrt((pow(catetoA,2))+(pow(catetoB,2)))

print("El valor de la hipotenusa es {0:.2f}\n".format(hipotenusa))
"""
#Script que determine el costo por ticket en base a precio por kilometro y kilometro recorrido
precio_km=0
km_recorrido=0
precio_ticket=0

precio_km=float(input("Ingrese el valor por kilometro: "))
km_recorrido=float(input("Ingrese los kilometros a recorrer: "))

precio_ticket=(precio_km*km_recorrido)

print("El precio del ticket es ${0:.2f}".format(precio_ticket))

                       
