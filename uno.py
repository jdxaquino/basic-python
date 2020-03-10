#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

cventas1, cventas2, cventas3 = 0, 0, 0 #Variables de Cantidad de Ventas por Categorías
subt1, subt2, subt3 = 0, 0, 0 #Variables de Montos Subtotales por Categorías
total, cont = 0, 1 #Variable de Monto Total de Venta y Contador

print ("""
><><><><><><><><><><><><><><><><><><><><
>>> BIENVENIDO A BOUTIQUE TRIKI TRAKA <<
><><><><><><><><><><><><><><><><><><><><
""")

time.sleep(2)
os.system("cls")

numven = int(input("\n\n-> Por favor, ingrese Número de Ventas: "))

while cont <= numven and numven > 0:
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
	cont += 1
pass

print ("\n\n-> Cantidad de Articulos Vendidos con Costo Igual o Menor a 500 Pesos: ", cventas3)
print ("\n-> Monto Subtotal de Articulos con Costo Igual o Menor a 500 Pesos: ", subt3)

print ("\n\n-> Cantidad de Articulos Vendidos con Costo Igual o Menor a 1000 Pesos: ", cventas2)
print ("\n-> Monto Subtotal de Articulos con Costo Igual o Menor a 1000 Pesos: ", subt2)

print ("\n\n-> Cantidad de Articulos Vendidos con Costo Mayor a 1000 Pesos: ", cventas1)
print ("\n-> Monto Subtotal de Articulos con Costo Mayor a 1000 Pesos: ", subt1)

print ("\n\n--> Monto Total de Articulos Vendidos: ", total, "<--")

time.sleep(5)
