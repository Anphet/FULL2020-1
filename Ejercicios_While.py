#1 Realizar un script que me diga si un numero es primo o no, usando While.

n1=int(input("Ingrese un numero: "))
bandera=False
contador=0
resultado=0
i=1
while(bandera==False):
    resultado=n1%i

    if(resultado==0):
        contador+=1

    i+=1

    if(i==n1+1):
        bandera=True

if(contador==2):
    print(f"El numero {n1} es primo.")
else:
    print(f"El numero {n1} NO es primo.")

#2 Realizar un script que imprima la serie Fibonacci.

c_f=int(input("Ingrese la cantidad de digitos: "))
contador=0
resultado=0
n1=0
n2=1
while(contador<c_f):
    print(f"{n1},", end="")
    resultado=n1+n2
    n1=n2
    n2=resultado
    contador+=1

#3 Realizar un script que muestre la tabla de multiplicar

n1=int(input("\nIngrese el numero: "))
i=1
while(i<=10):
    print(f"{n1}*{i} = {n1*i}")
    i+=1
