#Temperatura

#Entrada de datos
temp = int(input('Ingrese una temperatura: '))
#fahrenheit = int(input('Ingrese una temperatura en grados °F: '))
#kelvin = int(input('Ingrese una temperatura en grados °: '))


#fahrenheit = int(input('Ingrese una temperatura en grados °C: '))


#Proceso
celsius_a_fahrenheit = 9.0/5.0 * temp + 32
fahrenheit_a_celsius = (temp - 32) * 5/9 
celsius_a_kelvin = temp + 273.15
kelvin_a_celsius = temp - 273.15 
kelvin_a_fahrenheit = (temp - 273.15) * 9/5 + 32 
fahrenheit_a_kelvin = (temp - 32) * 5/9 + 273.15




#celsius = (fahrenheit - 32) * 5.0/9.0

#Salida de datos
print("La temperatura de °C a °F es: ", celsius_a_fahrenheit)
print("La temperatura de °F a °C es: ", fahrenheit_a_celsius)
print("La temperatura de °C a °K es: ", celsius_a_kelvin)
print("La temperatura de °K a °C es: ", kelvin_a_celsius)
print("La temperatura de °K a °F es: ", kelvin_a_fahrenheit)
print("La temperatura de °F a °K es: ", fahrenheit_a_kelvin)