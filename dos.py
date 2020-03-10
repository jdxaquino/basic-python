#!/usr/bin/env python
# -*- coding: utf-8 -*-

cventas1, cventas2, cventas3 = 0, 0, 0 #Variables de Cantidad de Ventas por Categorías
subt1, subt2, subt3 = 0, 0, 0 #Variables de Montos Subtotales por Categorías
total = 0 #Variable de Monto Total de Venta y Contador

print ("\n><><><><><><><><><><><><><><><><><><><><")
print ("\n>>> BIENVENIDO A BOUTIQUE TRIKI TRAKA <<")
print ("\n><><><><><><><><><><><><><><><><><><><><")

numven = int(input("\n\n-> Por favor, ingrese Número de Ventas: "))

for x in range(numven):
	venta = float(input("\n--> Por favor, ingrese Valor del Producto: "))
	if venta > 1000:
		cventas1 += 1
		subt1 += venta
	else:
		if venta > 500:
			cventas2 += 1
			subt2 += venta
		else:
			cventas3 += 1
			subt3 += venta
		pass
	pass
	total += venta
pass

print ("\n\n-> Cantidad de Articulos Vendidos con Costo Igual o Menor a 500 Pesos: ", cventas3)
print ("\n-> Monto Subtotal de Articulos con Costo Igual o Menor a 500 Pesos: ", subt3)

print ("\n\n-> Cantidad de Articulos Vendidos con Costo Igual o Menor a 1000 Pesos: ", cventas2)
print ("\n-> Monto Subtotal de Articulos con Costo Igual o Menor a 1000 Pesos: ", subt2)

print ("\n\n-> Cantidad de Articulos Vendidos con Costo Mayor a 1000 Pesos: ", cventas1)
print ("\n-> Monto Subtotal de Articulos con Costo Mayor a 1000 Pesos: ", subt1)

print ("\n\n--> Monto Total de Articulos Vendidos: ", total, "<--")
