'''
Boletín Programación Modular IV

Realizado por:Yeray Herrería Oña
'''
'''
#Ejercicio 1 USUARIOS

menu='''
######################################
#                                    #
#   A.Identificarse.                 #
#   B.Crear cuenta nueva.            #
#   C.Mostrar todos los usuarios.    #
#   D.Salir.                         #
#                                    #
######################################
'''
usuarios=["pe","h"]
contrasenyas=["p","h"]
intentos=[0,0,0,0,0,0,0,0,0,0]

def logearCuenta(usuarios,contrasenyas,intentos):
    if opcion=="A":
        usuario=input("Ingrese su nombre de usuario:")
        contrasenya=input("Ingrese su contraseña:")
        for i in range(len(usuario)):
            if usuario==usuarios[i]:
                    posicion=i
       
        if usuario not in usuarios:
            resultado=f"El usuario {usuario} no existe en el sistema."
        
        elif usuario in usuarios and contrasenya in contrasenyas and contrasenyas[posicion]==contrasenya:
            resultado=f"Bienvenido {usuario}."
        else:    
            while intentos[posicion]<3 and contrasenyas[posicion]!=contrasenya:
                intentos[posicion]+=1
                contrasenya=input("Error.Ingrese su contraseña:")
            if contrasenyas[posicion]==contrasenya:
                resultado=f"Bienvenido {usuario}."
            elif intentos[posicion]>=3:
                resultado="No hay más intentos."
    return resultado
    
def agregarUsuario(usuarios,contrasenyas):
    if len(usuarios)<10 and len(contrasenyas)<10:
        usuario=input("Introduzca un nuevo usuario:")
        usuarios.append(usuario)
        contrasenya=input("Introduzca la contraseña")
        contrasenyas.append(contrasenya) 
        resultado="Usuario y contraseña añadido correctamente."                
    else:
        resultado="No hay espacio para más usuarios."
    return resultado
print(menu)          
opcion=input("Escribe la opcion que desees:").upper()

while opcion!="A" and opcion!="B" and opcion!="C" and opcion!="D":
    opcion=input("Error.Escribe la opcion que desees:").upper()
    
while opcion!="D":
    if opcion=="A":
        print(logearCuenta(usuarios, contrasenyas, intentos))          
    elif opcion=="B":
        print(agregarUsuario(usuarios, contrasenyas))
    else:
        print(usuarios)
        
    opcion=input("Escribe la opcion que desees:").upper()

    while opcion!="A" and opcion!="B" and opcion!="C" and opcion!="D":
        opcion=input("Error.Escribe la opcion que desees:").upper()
print ("Programa finalizado.")


#Ejercicio 1 CALCULO
n=123

def sumaDigitos(n):
    suma=0
    for i in str(n):
        suma+=int(i)
    return suma

#Ejercicio 2 CALCULO
x=98 
y=56 

def maximoComunDivisor(x,y):
    if x==0:
        resultado=y 
    elif y==0:
        resultado=x
    elif x==y:
        resultado=x 
    elif x>y:
        resultado=maximoComunDivisor(x-y,y)
    else:
        resultado=maximoComunDivisor(x,y-x)
    return resultado

#Ejercicio 3 CALCULO
x=98 
y=56 

def minimoComunMultiplo(x,y):
    return (x*y)//maximoComunDivisor(x,y)


#Ejercicio 4 CALCULO
n=1
i=5

def sumarCifraDigitos(n,i):
    resultado=""
    suma=""
    acum=1
    while acum<i+1:
        resultado+=str(n*acum)
        acum+=1
        if acum<i+1:
            suma+=str(n)*(acum-1) + " + "
        else:
            suma+=str(n)*(acum-1) + " = " + resultado
    return suma

#Ejercicio 5 CALCULO
numerador=16
denominador=6
numerador2=20
denominador2=8

def leer_fraccion(numerador,denominador):
    mcd=maximoComunDivisor(numerador,denominador)
    resultado=f"La fracción es {numerador}/{denominador} y simplificada queda {numerador//mcd}/{denominador//mcd}"
    return resultado

def escribir_fraccion(numerador,denominador):
    if denominador==1:
        resultado=f"La fraccion es {numerador}."
    else:
        resultado=f"La fraccion es {numerador}/{denominador}."
    return resultado

def calcular_mcd(numerador,denominador):
    return maximoComunDivisor(numerador,denominador)

def simplificar_fraccion(numerador,denominador):
    mcd=maximoComunDivisor(numerador,denominador)
    resultado=f"La fracción simplificada queda {numerador//mcd}/{denominador//mcd}"
    return resultado

def sumar_fracciones(numerador,numerador2,denominador,denominador2):
    sumanumerador=numerador*denominador2+denominador*numerador2
    sumadenominador=denominador*denominador2
    mcd=maximoComunDivisor(sumanumerador,sumadenominador)
    resultado=f"La suma de {numerador}/{denominador} + {numerador2}/{denominador2} = {sumanumerador//mcd}/{sumadenominador//mcd}"
    return resultado

def restar_fracciones(numerador,numerador2,denominador,denominador2):
    restanumerador=numerador*denominador2-denominador*numerador2
    restadenominador=denominador*denominador2
    mcd=maximoComunDivisor(restanumerador,restadenominador)
    resultado=f"La resta de {numerador}/{denominador} - {numerador2}/{denominador2} = {restanumerador//mcd}/{restadenominador//mcd}"
    return resultado

def multiplicar_fracciones(numerador,numerador2,denominador,denominador2):
    multiplicacionnumerador=numerador*numerador2
    multiplicaciondenominador=denominador*denominador2
    mcd=maximoComunDivisor(multiplicacionnumerador,multiplicaciondenominador)
    resultado=f"La multiplicacion de {numerador}/{denominador} x {numerador2}/{denominador2} = {multiplicacionnumerador//mcd}/{multiplicaciondenominador//mcd}"
    return resultado

def dividir_fracciones(numerador,numerador2,denominador,denominador2):
    divisionnumerador=numerador*denominador2
    divisiondenominador=denominador*numerador2
    mcd=maximoComunDivisor(divisionnumerador,divisiondenominador)
    resultado=f"La division de {numerador}/{denominador} % {numerador2}/{denominador2} = {divisionnumerador//mcd}/{divisiondenominador//mcd}"
    return resultado

#Ejercicio 6 CALCULO
menu='''
######################################
#                                    #
#   A.Sumar dos fracciones.          #
#   B.Restar dos fracciones.         #
#   C.Multiplicar dos fracciones.    #
#   D.Dividir dos fracciones.        #
#   E.Salir                          #
#                                    #
######################################
'''

opcion=input("Escribe la opcion que desees:").upper()

while opcion!="A" and opcion!="B" and opcion!="C" and opcion!="D" and opcion!="E":
    opcion=input("Error.Escribe la opcion que desees:").upper()
    
while opcion!="E":
    if opcion=="A":
        numerador=int(input("Introduzca el numerador de la primera fracción:"))
        denominador=int(input("Introduzca el denominador de la primera fracción:"))
        numerador2=int(input("Introduzca el numerador de la primera segunda:"))
        denominador2=int(input("Introduzca el denominador de la primera segunda:"))
        print(sumar_fracciones(numerador,numerador2,denominador,denominador2))
    elif opcion=="B":
        numerador=int(input("Introduzca el numerador de la primera fracción:"))
        denominador=int(input("Introduzca el denominador de la primera fracción:"))
        numerador2=int(input("Introduzca el numerador de la primera segunda:"))
        denominador2=int(input("Introduzca el denominador de la primera segunda:"))
        print(restar_fracciones(numerador,numerador2,denominador,denominador2))
    elif opcion=="C":
        numerador=int(input("Introduzca el numerador de la primera fracción:"))
        denominador=int(input("Introduzca el denominador de la primera fracción:"))
        numerador2=int(input("Introduzca el numerador de la primera segunda:"))
        denominador2=int(input("Introduzca el denominador de la primera segunda:"))
        print(multiplicar_fracciones(numerador,numerador2,denominador,denominador2))
    else:
        numerador=int(input("Introduzca el numerador de la primera fracción:"))
        denominador=int(input("Introduzca el denominador de la primera fracción:"))
        numerador2=int(input("Introduzca el numerador de la primera segunda:"))
        denominador2=int(input("Introduzca el denominador de la primera segunda:"))
        print(dividir_fracciones(numerador,numerador2,denominador,denominador2))
        
    opcion=input("Escribe la opcion que desees:").upper()

    while opcion!="A" and opcion!="B" and opcion!="C" and opcion!="D" and opcion!="E":
        opcion=input("Error.Escribe la opcion que desees:").upper()

print("El programa a finalizado")

#Ejercicio 1 FIGURAS
radio=5
def areaCirculo(radio):
    import math
    pi=math.pi
    return pi*(radio*radio)

#Ejercicio 2 FIGURAS
def longitudCirculo(radio):
    import math
    pi=math.pi
    return 2*pi*radio

#Ejercicio 3 FIGURAS
x1=1
x2=5
y1=1
y2=4
def distanciaEuclidea(x1,x2,y1,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**(0.5)

#Ejercicio 4 FIGURAS
x1=1
x2=5
x3=6
y1=1
y2=4
y3=3
def perimetroTriangulo(x1,x2,x3,y1,y2,y3):
    lado1=((x2-x1)**2 + (y2-y1)**2)**(0.5)
    lado2=((x3-x1)**2 + (y3-y1)**2)**(0.5)
    lado3=((x3-x2)**2 + (y3-y2)**2)**(0.5)
    return lado1+lado2+lado3

#Ejercicio 5 FIGURAS
def areaTriangulo(x1,x2,x3,y1,y2,y3):
    return perimetroTriangulo(x1, x2, x3, y1, y2, y3)*0.5

#Ejercicio 1 FECHAS
#Primera hora
hora=21
minuto=0
segundo=60

def segundosTranscurridos(hora,minuto,segundo):
    resultado="Formato no válido."
    if 0<=hora<=23 and 0<=minuto<=59 and 0<=segundo<=59:
        hora=hora*3600
        minuto=minuto*60
        resultado=hora+minuto+segundo
    elif hora==24 and minuto==0 and segundo==0:
        resultado=hora*3600
    elif hora==23 and 0<=minuto<=60 and segundo==0:
        hora=hora*3600
        resultado=hora+segundo
    elif hora==23 and minuto==0 and 0<=segundo<=60:
        hora=hora*3600
        minuto=minuto*60
        resultado=hora+minuto
    elif 0<=hora<=22 and 0<=minuto<=60 and segundo==60:
        hora=hora*3600
        minuto=minuto*60
        resultado=hora+minuto+segundo
    return resultado

#Ejercicio 2 FECHAS
#Segunda hora
hora2=2
minuto2=34
segundo2=34
def calcularDiferencia(hora,hora2,minuto,minuto2,segundo,segundo2):
    resultado="Formato no válido."
    if (0<=hora<=23 and 0<=minuto<=59 and 0<=segundo<=59) or (0<=hora2<=23 and 0<=minuto2<=59 and 0<=segundo2<=59):
        resultado=f"La diferencia es de {segundosTranscurridos(hora,minuto,segundo)-segundosTranscurridos(hora2,minuto2,segundo2)} segundos."
    elif (hora==24 and minuto==0 and segundo==0) or (hora2==24 and minuto2==0 and segundo2==0):
        resultado=f"La diferencia es de {segundosTranscurridos(hora,minuto,segundo)-segundosTranscurridos(hora2,minuto2,segundo2)} segundos."
    elif (hora==23 and 0<=minuto<=60 and segundo==0) or (hora2==23 and 0<=minuto2<=60 and segundo2==0):
        resultado=f"La diferencia es de {segundosTranscurridos(hora,minuto,segundo)-segundosTranscurridos(hora2,minuto2,segundo2)} segundos."
    elif (hora==23 and minuto==0 and 0<=segundo<=60) or (hora2==23 and minuto2==0 and 0<=segundo2<=60):
        resultado=f"La diferencia es de {segundosTranscurridos(hora,minuto,segundo)-segundosTranscurridos(hora2,minuto2,segundo2)} segundos."
    elif (0<=hora<=22 and 0<=minuto<=60 and segundo==60) or (0<=hora2<=22 and 0<=minuto2<=60 and segundo2==60):
        resultado=f"La diferencia es de {segundosTranscurridos(hora,minuto,segundo)-segundosTranscurridos(hora2,minuto2,segundo2)} segundos."

    return resultado

#Ejercicio 3 FECHAS
seconds=223000

def convertirSegundos(seconds):
    day=seconds//(60*60*24)
    seconds=seconds%(60*60*24)
    hours=seconds//(60*60)
    seconds=seconds%(60*60)
    minutes=seconds//60
    seconds=seconds%60

    return f"En total son {day} días con {hours} horas {minutes} minutos y {seconds} segundos."
print(convertirSegundos(seconds))
'''

