''' 
Obtener un número y determinar lo siguiente:
a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
c) en otro caso imprimir No Válido
'''

#Entrada de datos
numero = int(input("Ingresa un número: "))

#Proceso

if(numero <-1 and numero > -100):
    for i in range(-1, -100, -2):
        print(i)
elif (numero > 0 and numero < 100):
   j = 2 
   while(j <= 100): 
      print(j) 
      j = j + 2 
else:
    print("No válido")
