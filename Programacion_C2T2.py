#Taller de programacion.

#116
numero=float(input("Ingrese el numero que desea multiplicar: "))
for i in range(0,10):
    print(f"x{i+1} = {numero*(i+1)}")

#119
for i in range(0,201):
    if i%2==0 and i!=0:
        print(i)

#120
for j in range(200,0,-1):
    if j%2==0 and j!=0:
        print(j)

#121   
n=int(input("Ingrese el numero: "))

for i in range (2,n):
    if i%2==0 and i!=0:
        print(i)

#122
resultado=0
n=int(input("Ingrese el limite superior: "))
m=int(input("Ingrese el limite inferior: "))

if n<m:
    while n<m:
        m=int(input("Ingrese el limite inferior: "))
else:
    for i in range(n+1):
        resultado=resultado+i
    print(resultado)

#123
resultado1=0
n1=int(input("Ingrese el limite superior: "))
m1=int(input("Ingrese el limite inferior: "))

if m1>n1:
    while m1>n1:
        m1=int(input("Ingrese un valor menor al limite superior: "))
else:
    resultado1=m1
    for i in range(n1+1):
        resultado1=resultado1+(i**2)
    print(resultado1)

#124
resultado_suma=0
n1=int(input("Ingrese el limite superior: "))
m1=int(input("Ingrese el limite inferior: "))

if n1<m1:
    while n1<m1:
        m1=int(input("Ingrese un numero menor al limite superior: "))
else:
    resultado_suma=m
    for i in range(n1):
        if i%2==0 and i!=0:
            resultado_suma=resultado_suma+i
    print(resultado_suma)
