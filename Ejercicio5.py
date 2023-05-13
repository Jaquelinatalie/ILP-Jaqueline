#Formula general


#Entrada de datos
import math


a = int(input('Ingresa el valor a: '))
b = int(input('Ingresa el valor b: '))
c = int(input('Ingresa el valor c: '))

#Proceso
d= (b*b)-4*a*c 

x1 = (- b + math.sqrt(d)) / (2 * a)

x2 = (- b - math.sqrt(d)) / (2 * a)


#Salida de datos

print("El valor de X1 es: ", x1)
print("El valor de X2 es: ", x2)