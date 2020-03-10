#!/usr/bin/env python

import os
import time

nomcho = [] #Arreglo de los nombres de los choferes
kilsem = [] #Arreglo de los Kilometros Recorridos en la semana
kiltot = [] #Arreglo del Total de los Kilometros en la semana
saldia = [] #Arreglo del salario por día
saltot = [] #Arreglo del salario total

class Chofer():
    def __init__(self, nc):
        for x in range(nc):
            os.system("cls")
            print ("""
            ||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
            |*||*||*||*||*|| ENTRADA DATOS ||*||*||*||*||*||*|
            ||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
            """)
            nomcho.append (input("\n||--->> Por favor, ingrese nombre del chofer %d: " %(x+1)))
            kilxdia = [] #Declaro array para almacenar los kilometros por día
            salxdia = [] #Declaro array para almacenar el salario por día
            sumkil = 0 #Declaro variable para almacenar la suma de kilometros en la semana
            sumsal = 0 #Declaro variable para almacenar la suma del saladio en la semana
            for y in range(6):
                kilxdia.append (int(input("\n||---->> Por favor, ingrese kilometros recorridos en día %d: " %(y+1))))
                sumkil += kilxdia[y]
                salxdia.append(10 * kilxdia[y])
                sumsal += salxdia[y]
            pass
            kilsem.append(kilxdia) #Arreglo de kilometros por día añadido a arreglo kilometros en la semana
            kiltot.append(sumkil) #Variable suma de kilometros añadido a arreglo suma total de kilometros
            saldia.append(salxdia) #Arreglo de salario por día a arreglo de salario por día
            saltot.append(sumsal) #Arreglo de la suma del salario añadido a arreglo de la suma del salario
        pass
    pass

    def impresionDatos(self, nc):
        print ("""
        ||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
        ||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
        |*||*||*||*|| IMPRESIÓN DE DATOS  ||*||*||*||*||*|
        ||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
        ||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
        """)
        for z in range(nc): #Impresión de todos los datos
            print ("\n||-->> Chofer: ", nomcho[z])
            print ("\n||-->> Recorridos por día: ", kilsem[z])
            print ("\n||-->> Salario por día: ", saldia[z])
            print ("\n||-->> Total de recorridos: ", kiltot[z], "en la semana.")
            print ("\n||-->> Total de salario: ", saltot[z], "en la semana.\n")
        pass
        time.sleep(10)
    pass
pass

os.system("cls")
print ("""
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
||*|| BIENVENIDO A TRANSPORTES 'THE BIG OLD' ||*||
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
""")
time.sleep(2)
os.system("cls")
print ("""
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
|*||*||*||*||*|| ENTRADA DATOS ||*||*||*||*||*||*|
||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||*||
""")
n = int(input("\n||-->> Por favor, ingrese número de Choferes: "))
informacion = Chofer(n) #Solicita número de choferes
os.system("cls")
informacion.impresionDatos(n)
