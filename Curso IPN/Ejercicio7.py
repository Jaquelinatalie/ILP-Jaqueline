#Nivel de agua en cisterna

#Entrada de datos
nivel = float(input("Indica la cantidad de litros de agua que hay en la cisterna: "))

#Proceso

if nivel < 0:
    print("Fuga en cisterna")
elif nivel == 0:
    print("Encender bomba de agua")
elif nivel > 0 and nivel <= 2:
    print("Acelerar bomba de agua")
elif nivel > 2 and nivel <= 4:
    print("Bomba trabajando")
elif nivel > 4 and nivel < 6:
    print("Desacelerar bomba")
elif nivel == 6:
    print("Apagar Bomba")
elif nivel > 6:
    print("Desbordamiento de agua en la cisterna")