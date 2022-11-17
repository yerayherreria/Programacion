'''
Boletín Programación Modular I

Realizado por:Yeray Herrería Oña
'''
'''
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
   
    for i in range(len(lista)):
        numC=lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)]=num
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

def esBisiesto(year):
    return (year%4==0 and (year%100!=0 or year%400==0))

def fechaValida(d,m,y):
    diasMaximos=[31,28,31,30,31,30,31,31,30,31,30,31]
   
    return (1<=d<=diasMaximos[m-1] or (esBisiesto(y) and m==2 and 1<=d<=29))

def transformarFecha(day,month,year):
    nombreMeses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
   
    if fechaValida(day,month,year):
        mesLargo=nombreMeses[month-1]
        resultado=f"{day} de {mesLargo} de {year}"    

    return resultado

dia=int(input("Introduzca un día:"))
mes=int(input("Introduzca un mes válido:"))
anyo=int(input("Introduzca un mes válido:"))

while dia>0:
    print(transformarFecha(dia,mes,anyo))
     
    dia=int(input("Introduzca un día:"))
    mes=int(input("Introduzca un mes válido:"))
    anyo=int(input("Introduzca un mes válido:"))
print("Fin del programa.")
 

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
    listarevertida=[]
   
    for i in range(len(lista)-1,-1,-1):
        listarevertida+=[lista[i]]
    return listarevertida

print (revertirLista(lista))


#Ejercicio 6

lista=[1,4,9,6,7]

def estaOrdenada(lista):
    resultado=True

    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            resultado=False
    return resultado
 
print(estaOrdenada(lista))


#Ejercicio 7
ficha1=[3,4]
ficha2=[2,5]

def encajan(ficha1,ficha2):
    resultado=False
    for i in ficha1:
        if i==ficha2[0] or i==ficha2[1]:
            resultado=True
           
    return resultado

print(encajan(ficha1, ficha2))


#Ejercicio 8

numeros=[]
n=1

def numerosPrimos(numeros):
    esPrimo = []
    for n in numeros:
        contador = 0
        for i in range(2,n):
            if n%i == 0:
                contador += 1
        if contador == 0:
            if n > 0:
                esPrimo.append(n)
    return esPrimo

def numerosSumatorio(numeros):
    acum=0
    for i in numeros:
        acum+=i
    return acum

def numerosPromedio(numeros):
    acum=0
    cont=0
    promedio=0
    for i in numeros:
        acum+=i
        cont+=1
        promedio= acum/cont
    return promedio

def numerosFactorial(numeros):
    factorial=[]
    acum=1    
    for i in numeros:
        acum = acum + acum*i
        factorial.append(acum)
    return factorial


while n>=0:
    n= int(input("Introduzca los números(Negativo para acaba):"))
    numeros.append(n)

print(numerosPrimos(numeros))  
print(numerosSumatorio(numeros))
print(numerosPromedio(numeros))
print(numerosFactorial(numeros))


#Ejercicio 9

numeros=[1,2,3,4,5,6,7,8,9]
k=9

def numerosMenores(numeros):
    menores=[]
    for i in numeros:
        if i<k:
            menores.append(i)
    return menores

def numerosMayores(numeros):
    mayores=[]
    for i in numeros:
        if i>k:
            mayores.append(i)
    return mayores

def numerosMultiplos(numeros):
    multiplos=[]  
    for i in numeros:
        if k%i==0:
            multiplos.append(i)
    return multiplos

print(numerosMenores(numeros))
print(numerosMayores(numeros))
print(numerosMultiplos(numeros))


#Ejercicio 10

def conversorBinarioDecimal(n):
    numero_decimal = 0
    posicion=len(numero)-1

    for i in numero:
        numero=int(i)
        numero_decimal+=numero*2**posicion
        posicion -= 1

    return numero_decimal

def conversorDecimalBinario(n):
    numeroBinario=0
    posicion=1
    n=int(n)
    while n!=0:
        numeroBinario=numeroBinario+n%2*posicion
        n//=2
        posicion*=10
    return numeroBinario

n=input("Introduce un número en binario o decimal acabado por D/B:").upper()

acceso=False
if n[len(n)-1:len(n)]=="B":
    while acceso==False:
        cambio=str(n[:-1])
        for i in range(len(cambio)):
            if cambio[i]=="0" or cambio[i]=="1":
                acceso=True
            else:
                acceso=False
               
        if acceso==False:
            n=input("Error.Introduce el formato correcto:")
           
    print(conversorBinarioDecimal(n))

elif n[len(n)-1:len(n)]=="D":
    n=int(n[:-1])
    while n<0:
        n=input("Error.El formato debe estar en positivivo.Inténtelo de nuevo:")
 
    print(conversorDecimalBinario(n))


#Ejercicio 11

lista1=[1,2,3,4,"Hola","Mundo",3]
lista2=["Mundo",3,3]

def intersect(lista1,lista2):
    comunes=[]
    sinRepetir=[]
   
    for i in lista1:
        for j in lista2:
            if j==i:
                comunes.append(i)
                   
    for j in comunes:
        if j not in sinRepetir:
            sinRepetir.append(j)
    return sinRepetir

print(intersect(lista1, lista2))


#Ejercicio 12

lista1=[1,2,3,4,"Hola","Mundo",3]
lista2=["Mundo",3,3]

def unionLista(lista1,lista2):
    norepetidos=[]
    union=lista1+lista2
   
    for i in union:
        if i not in norepetidos:
            norepetidos.append(i)
    return norepetidos

print(unionLista(lista1, lista2))


#Ejercicio 13

nombres=["Diego","Dario","Duran","Estefania"]
letra="D"

def busquedaNombre(nombres):
    nombresCorrectos=[]

    for i in nombres:
        if letra==i[0]:
            nombresCorrectos.append(i)
    return nombresCorrectos

print(busquedaNombre(nombres))


#Ejercicio 14

lista=["Hola","que","paesa","poema",]

def cadenaLarga(lista):
    caracter=0
    caracterRepetido=0
    lista1=[]
    valor=""
    
    for i in lista:
        caracter1=len(i)
        if caracter1>caracter:
            caracter=caracter1
            valor=i         
    for j in lista:
        if len(valor)==len(j):
            lista1.append(j)          
    for k in lista1:
        caracterRepetido2=0
        for u in range(len(k)):
            for z in range(1,len(k)):
                if k[u]==k[z]:
                    caracterRepetido2+=1
        if caracterRepetido2>caracterRepetido:
            caracterRepetido=caracterRepetido2
            palabra=k
    return palabra

print(cadenaLarga(lista))
'''
