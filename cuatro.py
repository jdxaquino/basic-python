#!/usr/bin/env python

nomcho = [] #Arreglo de los nombres de los choferes
kilsem = [] #Arreglo de los Kilometros Recorridos en la semana
kiltot = [] #Arreglo del Total de los Kilometros en la semana

print ("""
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
||*|| BIENVENIDO A TRANSPORTES 'THE BIG OLD' ||*||
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
""")

numcho = int(input("\n\n||-->> Por favor, ingrese número de Choferes: ")) #Solicita número de choferes

for x in range(numcho): #Comienza arreglo para solicitar nombres de los choferes
	nomcho.append (input("\n\n||--->> Por favor, ingrese nombre del chofer %d: " %(x+1))) #Solicita nombre del chofer

	kildia = [] #Declaro array para almacenar los kilometros por día
	kilsum = 0 #Declaro variable para almacenar la suma de kilometros en la semana

	for y in range(6): #Inicio de arreglo para solicitar kilometros por día
		kildia.append (int(input("\n||---->> Por favor, ingrese kilometros recorridos en día %d: " %(y+1)))) #Solicita kilometros recorridos por día
		kilsum += kildia[y] #Suma de los kilometros recorridos en los 6 días
	pass
	kilsem.append(kildia) #Arreglo de kilometros por día añadido a arreglo kilometros en la semana
	kiltot.append(kilsum) #Variable suma de kilometros añadido a arreglo suma total de kilometros
pass

for z in range(numcho): #Impresión de todos los datos
	print ("\n\n||-->> Chofer: ", nomcho[z])
	print ("\n||-->> Recorridos por día: ", kilsem[z])
	print ("\n||-->> Total de recorridos: ", kiltot[z], "en la semana\n\n.")
pass
