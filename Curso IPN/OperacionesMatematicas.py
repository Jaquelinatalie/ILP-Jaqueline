#EJEMPLO 2
# Operaciones Matemáticas: suma , resta, multiplicación, división

#Entrada de datos
# - declarar o crear variables

#importes
import math 


numero_1 = int(input("Escribe el 1er número: ")) #10.5
numero_2 = int(input("Escribe el 2do número: "))  #2.3

#Procesos (Operaciones o cálculos matemáticos y/o lógicos)

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

potencia_1 = numero_1 ** numero_2
potencia_2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** numero_2
cubo = pow(numero_2, 3)

raiz_cuadrada_1 = math.sqrt(9)
raiz_cuadrada_2 = pow(9, 1/2)
raiz_cuabica = pow(27, 1/3)

modulo_residuo = 20 % 6

# redondear
# input


#Salida de datos
print("La suma es igual a = ", suma)
print("La suma es =" + str(suma)) #concatenación: union

#castear (convertir un tipo de dato en otro)
print(f"La suma es igual = {suma}")




print("La resta es igual a = ", resta)
print("La división es igual a = ", division)
print("La multiplicación es igual a = ", multiplicacion)
print("La potencia 1 es igual a = ", potencia_1)
print("La potencia 2 es igual a = ", potencia_2)
print("El cuadrado es igual a = ", cuadrado)
print("El cubo es igual a = ", round (cubo, 2)) #redondeo
print("La raíz cuadrada 1 es igual a = ", raiz_cuadrada_1)
print("La raíz cuadrada 2 es igual a = ", raiz_cuadrada_2)
print("La raíz cubica es igual a = ", raiz_cuabica)
print("El modulo o residuo de 20 % 6 es igual a = ", modulo_residuo)