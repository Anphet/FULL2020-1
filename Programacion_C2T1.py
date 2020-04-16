"""
Estudiante: Andrés Elías Forero Garzón.
Código: 202010024601.
Clase: Programación básica.
Profesor: Omar Ernesto Torres Ladino.
"""

#1.1 Determinar si una persona es apta para votar.
edad=0

edad=int(input("Ingrese la edad: "))
if edad>=18:
    print("La persona puede votar.")
else:
    print("La persona no puede votar.")

#1.2 Determinar salario en base a horas trabajadas.
valor_hora=0
horas_trabajadas=0
valor_maximo=0
salario=0

valor_hora=float(input("Ingrese el valor por hora de trabajo: "))
horas_trabajadas=int(input("Ingrese la cantidad de horas trabajadas: "))

if horas_trabajadas<=40 and horas_trabajadas>0:
    salario=(valor_hora*horas_trabajadas)
    print(f"El valor a pagar por {horas_trabajadas} es {salario}")
elif horas_trabajadas>40:
    valor_maximo=(valor_hora*40)
    horas_trabajadas=horas_trabajadas-40
    salario=(horas_trabajadas*valor_hora*2)+valor_maximo
    print(f"El valor a pagar es {salario}")
else:
    print("No hay que pagar.")

#1.3 Determinar regalo segun presupuesto.
presupuesto=0

print("Lista de regalos\nTarjeta = $1 a $10\nChocolates = $11 a $100\nFlores = $101 a $250\nAnillo = $251")

presupuesto=int(input("Ingrese su presupuesto: "))

if presupuesto>0 and presupuesto<=10:
    print("Claramente no hay nada mas bello que leer una carta hecha por esa persona especial.")
elif presupuesto>=11 and presupuesto<=100:
    print("El chocolate posee feniletilamina, tambien conocida como la hormona del enamoramiento, podrias intentar con ello.")
elif presupuesto>=101 and presupuesto<=250:
    print("Un buen ramo de flores puede simbolizar todo eso que las palabras no siempre pueden, solo0 recuerda que debe ser un ramo con numero impar.")
elif presupuesto>=251:
    print("Hasta yo me enamoraria de quien me regalase un anillo.")
else:
    print("Lo importante es que tienes la salud para poder decirle cuanto lo/a amas.")

#1.4 Determinar el costo por horas de un parqueadero
cantidad_h=0
cobro=0

cantidad_h=int(input("Ingrese la cantidad de horas que utilizo el parqueadero: "))

if cantidad_h>0 and cantidad_h<=2:
    cobro=(cantidad_h*5)
    print(f"El valor a pagar es {cobro}")
elif cantidad_h>2 and cantidad_h<=5:
    cobro=((cantidad_h-2)*4)+10
    print(f"El valor a pagar es {cobro}")
elif cantidad_h>5 and cantidad_h<=10:
    cobro=((cantidad_h-5)*3)+18
    print(f"El valor a pagar es {cobro}")
elif cantidad_h>10:
    cobro=((cantidad_h-10)*2)+33
    print(f"El valor a pagar es {cobro}")
else:
    print("No hay que pagar.")

#1.5 Algoritmo que especifique quien es mayor entre tres personas.
n1=0
n2=0
n3=0
e1=0
e2=0
e3=0

n1=input("Ingrese el nombre de la primera persona: ")
e1=int(input("Ahora ingrese su edad: "))
n2=input("Ingrese el nombre de la segunda persona: ")
e2=int(input("Ahora ingrese su edad: "))
n3=input("Ingrese el nombre de la tercera persona: ")
e3=int(input("Ahora ingrese su edad: "))

if e1==0 and e1==e2==e3:
    print(f"El cero es un numero intrigante, pero hay una infinidad mas de donde escoger.")
elif e1==e2 and e1==e3:
    print(f"{n1}, {n2} y {n3} tienen la misma edad.")
elif e1==e2 and e1>e3:
    print(f"{n1} y {n2} tienen la misma edad y son mayores que {n3}.")
elif e1==e3 and e1>e2:
    print(f"{n1} y {n3} tienen la misma edad y son mayores que {n2}.")
elif e1==e2 and e1<3:
    print(f"{n3} es mayor, {n1} y {n2} tienen la misma edad.")
elif e1==e3 and e1<e2:
    print(f"{n2} es mayor, {n1} y {n3} tienen la misma edad.")
elif e2==e3 and e1>e2:
    print(f"{n1} es mayor, {n2} y {n3} tienen la misma edad.")
elif e2==e3 and e1<e2:
    print(f"{n2} y {n3} tienen la misma edad y son mayores que {n1}.")
elif e1>e2 and e2>e3:
    print(f"{n1} es mayor y el menor es {n3}.")
elif e1>e2 and e2<e3:
    print(f"{n1} es mayor y el menor es {n2}.")
elif e1<e2 and e2<e3:
    print(f"{n3} es mayor y el menor es {n1}.")
elif e1>e2 and e2<e3:
    print(f"{n3} es mayor y el menor es {n2}.")
elif e1<e2 and e1>e3:
    print(f"{n2} es mayor y el menor es {n3}.")
elif e1<e2 and e1<e3:
    print(f"{n2} es mayor y el menor es {n1}.")

#1.6 Determinar el descuento de un producto segun su rango de precio.
valor_producto=0

valor_producto=float(input("Ingrese el valor del producto: "))

if valor_producto<=0:
    print("Yo sospecharia de algo que esta gratis.")
elif valor_producto>0 and valor_producto<=100:
    valor_producto=(valor_producto-(valor_producto*0.10))
    print(f"El valor del articulo con el descuento es {valor_producto}")
elif valor_producto>100 and valor_producto<200:
    valor_producto=(valor_producto-(valor_producto*0.12))
    print(f"El valor del articulo con el descuento es {valor_producto}")
elif valor_producto>=200:
    valor_producto=(valor_producto-(valor_producto*0.15))
    print(f"El valor del articulo con el descuento es {valor_producto}")