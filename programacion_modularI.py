'''
Boletín Programación Modular I

Realizado por:Yeray Herrería Oña
'''
'''
from programa.prueba import num

#Ejercicio 1
from random import randint

menu='''
#############################################
#               Bienvenido!                 #
#                                           #
#  Elige la opción:                         #
# A. Conocer el mayor:                      #
# B. Conocer el menor:                      #
# C. Obtener la suma de todos los números:  #
# D. Obtener la media:                      #
# E. Sustituir el valor de un elemento por  #
#     otro número introducido por teclado:  #
# F. Mostrar todos los números:             #
# G. Salir                                  #
#############################################
'''

lista=[]

for i in range(100):
    lista.append(randint(0,1000))

#Estas son la funciones:
def obtenerMayor(lista):
    mayor= lista[0]
   
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

def obtenerMenor(lista):
    menor= lista[0]
   
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor

def obtenerSuma(lista):
    suma=0
       
    for i in lista:
        suma+=i
    return suma

def obtenerMedia(lista):
    suma=0
    cont=0
    for i in lista:
        suma+=i
        cont+=1
    media=suma/cont
    return media

def sustituirValor(lista):
   
    posicion = int(input("Introduzca la posición que desees sustituir:"))
    while posicion < 0:
        posicion = input("Error.Introduzca la posición que desees sustituir:")

    n= int(input("Introduzca el valor que quiere poner en la posición:"))

    lista[posicion]=n

    return lista

print(menu)

opcion="A"

while opcion!="G":
    opcion=input("Escribe la opcion que desees:").upper()
    while opcion!="A" and opcion!="B" and opcion!="C" and opcion!="D" and opcion!="E" and opcion!="F" and opcion!="G":
        opcion=input("Error.Escribe la opcion que desees:").upper()
       
    if opcion=="A":
        print(obtenerMayor(lista))
    elif opcion=="B":
        print(obtenerMenor(lista))
    elif opcion=="C":
        print(obtenerSuma(lista))
    elif opcion=="D":
        print(obtenerMedia(lista))
    elif opcion=="E":
        print(sustituirValor(lista))
    elif opcion=="F":
        print(lista)

print("Fin del programa.")


#Ejercicio 2

lista=[0,1,2,3,4,5,6,7,8,9]

def desplazarDerecha(lista):
    num=lista[0]
    numC=0
    lista[0]=lista[len(lista)-1]
   
    for i in range(1,len(lista)):
            numC=lista[i]
            lista[i]=num
            num=numC
    return lista        

def desplazarIzquierda(lista):
    num=lista[0]
   
    for i in range(len(lista)-1):
        lista[i]=lista[i+1]
    lista[len(lista)-1]=num
    return lista
   
direccion=input("Escriba la direccion(D/I):").upper()

if direccion=="D":
    print(desplazarDerecha(lista))    
elif direccion=="I":
    print(desplazarIzquierda(lista))
   

#Ejercicio 3

day=0
month=0
year=0
lista=[0,"Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

while day>=0 and month>=0 and year>=0:
    day=int(input("Introduce el día de la fecha:"))
    while day<0:
        day=int(input("Error.Introduce el día de la fecha:"))
       
    month=int(input("Introduce el mes de la fecha:"))
    while month<1 or month>12:
        month=int(input("Error.Introduce el mes de la fecha:"))

    year=int(input("Introduce el año de la fecha:"))
    while year<0:
        year=int(input("Error.Introduce el año de la fecha:"))
   
    print(f"La fecha en formato largo es {day} de {lista[month]} del {year}.")
   
   
#Ejercicio 4

lista=[]
n=0

def obtenerMayor(lista):
    mayor= lista[0]
   
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor
def obtenerPar(lista):
    listapar=[]
   
    for i in range(len(lista)):
        if lista[i]%2==0:
            listapar+=[lista[i]]
    return listapar

while n>=0:
    n=int(input("Introduzca los numeros que desees(Negativo para acabar):"))
    lista+=[n]

print(f"El mayor de la lista es {obtenerMayor(lista)}.")
print(f"Los pares de la lista son {obtenerPar(lista)}.")


#Ejercicio 5

lista=[1,2,"Hola","que","pasa",235]

def revertirLista(lista):
    revertir=(list(reversed(lista)))
    return revertir

print (revertirLista(lista))

'''
#Ejercicio 6

lista=[1,4,9,6,7]

def estaOrdenada(lista):
    resultado=True

    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            resultado=False
    return resultado
 
