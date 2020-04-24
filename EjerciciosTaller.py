"""
Programación.
Parcial 2.
Andres Forero.
"""

"""
While
Nos piden que escribamos una función que le pida al usuario
que ingrese un número positivo, Si el usuario ingresa cualquier
cosa que no sea lo pedido, se le debe informar de su error mediante
un mensaje y volverle a pedir el número.
Resuelva el problema usando: Ciclo infinito que se rompe.

"""
def NumeroPositivo(n1):
    bandera=False
    if n1>0:
        print(f"{n1} es un numero positivo.")
        print("Felicidades.")
    else:
        while bandera==False:
            print(f"{n1} NO es un numero positivo.")
            n1=int(input("Ingrese un numero positivo: "))
            if n1>0:
                bandera=True
        print("Felicidades.")

n1=int(input("Ingrese un numero positivo: "))
NumeroPositivo(n1)

"""
If
Realice un algoritmo para determinar si una persona puede votar con
base en su edad en las proximas elecciones.
"""

edad=int(input("Edad: "))
if edad >=18:
    print("Puede votar.")
elif edad<18 and edad>1:
    print("No puede votar.")
else:
    print("No contabas con mi astucia.")

"""
For
Escriba un programa que muestre los numeros pares positivos entre 2
y un numero cualquiera que introduzca el usuario por teclado.
"""

numero_for=int(input("Numero: "))
if numero_for<1:
    while numero_for<1:
        numero_for=int(input("Es un gran numero, se me olvido decirte que debe ser mayor a 0, prueba otra vez: "))
for i in range(2,numero_for+1):
    if i%2==0:
        print(f"{i}, ", end="")