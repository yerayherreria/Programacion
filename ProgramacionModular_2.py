'''
Boletín Programación Modular II

Realizado por:Yeray Herrería Oña
'''
'''
#Ejercicio 1

n=7

def computaFactorial(n):
    acum=1
    resultado=True
    if n>-1:  
        for i in range(0,n):
            acum = acum + acum*i
        resultado=acum
    elif n<0:
        resultado=False
       
    return resultado
print(computaFactorial(n))

#Ejercicio 2

year=2017

def esAñoBisiesto(year):
    resultado=False
   
    if year%4==0 and (year%100!=0 or year%400==0):
        resultado=True
    return resultado

print(esAñoBisiesto(year))

#Ejercicio 3

year=2022
month=2

def esBisiesto(year):
    return (year%4==0 and (year%100!=0 or year%400==0))

def computeDaysInMonth(month,year):
    diasMaximos=[31,28,31,30,31,30,31,31,30,31,30,31]
    resultado=""
    
    if (month<1 or month>12) or year<1:
        resultado=-1 
    else:
        resultado=diasMaximos[month-1]      
        if esBisiesto(year)==True:
            diasMaximos=[31,29,31,30,31,30,31,31,30,31,30,31]
            resultado=diasMaximos[month-1]
                
    return resultado

print (computeDaysInMonth(month,year))

#Ejercicio 4

fecha=[]
fecha.append(int(input("Introduzca un día:")))
fecha.append(int(input("Introduzca un mes válido:")))
fecha.append(int(input("Introduzca un año válido:"))) 

def getDayOfWeek(fecha):
    week=["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
    a=(14-fecha[1])//12
    y=fecha[2]-a
    m=fecha[1]+12*a-2
    d=(fecha[0] + y + y//4 - y//100 + y//400 + (31*m)//12)%7   
    return week[d]

print(getDayOfWeek(fecha))

#Ejercicio 5
n1=5
n2=0

#Recursiva
def powerIt(n1,n2):
    resultado=0

    if n2==0:
        resultado=1
    else:
        resultado=n1*powerIt(n1,n2-1)
    return resultado

#Producto
def powerIt(n1,n2):
    cont=1
    
    for i in range(n2):
        cont*=n1
        
    return cont

print(powerIt(n1,n2))

#Ejercicio 6

#Ejercicio 7

def isPrimo(n):
    if n>0:
        resultado=True
        for i in range(2,n):
            if n%i==0:
                resultado=False
    else:
        resultado="Ninguno."
    return resultado
            
n=int(input("Introduzca un número mayor que 0:"))

print(isPrimo(n))

#Ejercicio 8

def solveSecondOrderEquation(a,b,c):
    opcion1=""
    opcion2=""
    resultado=""
    
    if a>0 and b>0 and c>0:
        opcion1=(-b + (((b)-(2*a*c))**0.5)/(2*a))
        opcion2=(-b - (((b)-(2*a*c))**0.5)/(2*a))
        
        resultado=f"La primera solución es {opcion1} y la segunda es {opcion2}."
    else:
        resultado="Ninguno."
    return resultado

a=3
b=5
c=1

print(solveSecondOrderEquation(a,b,c))

#Ejercicio 9

def getPrimeDivisors(n):
    resultado=""
    divisores=[1]
    primos=[]
    if n>0:
        for i in range(2,n):
            if n%i==0:
                divisores.append(i)
        for n in divisores:
            contador = 0
            for i in range(2,n):
                if n%i == 0:
                    contador += 1
            if contador == 0:
                if n > 0:
                    primos.append(n)
        resultado=primos
    else:
        resultado="Ninguno."
    return resultado    

n=100

print(getPrimeDivisors(n))

#Ejercicio 10

n1=2620
n2=2924

def isFriendNumber(n1,n2):
    cont=1
    divisores=[]
    resultado=False 
    if n1>0 and n2>0:
        for i in range(2,n1):
            if n1%i==0:
                divisores.append(i)
                cont+=i
        if cont==n2:
            resultado=True 
    return resultado

print(isFriendNumber(n1,n2))
'''