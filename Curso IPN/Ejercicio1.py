#Calcular promedio de 3 calificaciones

#Entrada de datos
calif_1 = float(input("Ingresa la calificación 1: "))
calif_2 = float(input("Ingresa la calificación 2: "))
calif_3 = float(input("Ingresa la calificación 3: "))


#Proceso
promedio = (calif_1 + calif_2 + calif_3) / 3

#Salida de datos
print("El promedio de las 3 calificaciones es: ", promedio)

'''
Condiciones:
Aprobado 6-10
Panzaso 6
Reprobado 0 y <6
Prom Inválido <0 - >10
'''

#Proceso

if (promedio > 6 and promedio <= 10):
    print("El promedio es", promedio,"Aprobado")
elif (promedio >= 0 and promedio < 6):
    print("El promedio es", promedio, "Reprobado")
elif(promedio == 6):
    print("El promedio es", promedio,"Aprobado de panzaso")
else: 
    print("Promedio inválido")

# elif(promedio < 0 or promedio > 10):
#    print("El promedio es", promedio,"Promedio Inválido")