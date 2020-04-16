import math
#Un programa que calcule la magnitud de un vector con origen en (0,0).
"""
vx=int(input("Ingrese la coordenada 'x' "))
vy=int(input("Ingrese la coordenada 'y' "))
v=(math.sqrt((vx**2)+(vy**2)))

print(f"La magnitud del vector({vx},{vy}) es {v}")
"""

#Un programa que calcule el angulo entre dos vectores.
"""
v1=0
v2=0
vx=int(input("X1: "))
vy=int(input("Y1: "))
ux=int(input("X2: "))
uy=int(input("Y2: "))

#1. Calcular u*v
v1=((vx*ux)+(vy*uy))
print(f"El valor de u*v es {v1} ")

#2. Calcular el producto de sus longitudes.
v2=(math.sqrt((vx**2)+(vy**2)))*(math.sqrt((ux**2)+(uy**2)))
print(f"El valor de |u||v| es {v2} ")
"""

#Un programa que calcule la direccion de un vector.
v=0
vx=int(input("X: "))
vy=int(input("Y: "))

v=(math.sqrt((vx**2)+(vy**2)))

print(f"|v|={v}")



