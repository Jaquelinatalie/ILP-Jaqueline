#Nómina

#Enero

#Entrada de datos

pago_por_dia = int(input("Ingresa la cantidad que ganas por día: ")) 
dias_laborales = 31
iva = 0.16
isr = 0.10

#Proceso
pago_base = pago_por_dia * dias_laborales
iva_trasladado = pago_base * iva
subtotal = pago_base + iva_trasladado
iva_retenido = 2/3 * iva_trasladado
isr_retenido = pago_base * isr
pago_neto = subtotal - iva_retenido - isr_retenido

#Salida de datos
print("Pago base o pago bruto: ", round(pago_base, 2))
print("IVA trasladado: ", iva_trasladado)
print("Subtotal: ", subtotal)
print("IVA retenido: ", iva_retenido)
print("ISR retenido: ", isr_retenido)
print("Pago neto: ", pago_neto)
