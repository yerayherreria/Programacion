'''
Boletín Programación Modular II

Realizado por:Yeray Herrería Oña
'''
'''
#Ejercicio 1
caracter="r".upper()
cadena="Corre curro por que currucu corre mas".upper()

def caractersInString(cadena):
    cont=0
    for i in range(len(cadena)):
        if cadena[i]==caracter:
            cont+=1
    return cont

print(caractersInString(cadena))

#Ejercicio 2
cadena="Corre curro por que currucu corre mas"

#.islower()
# def lowCaseInString(cadena):
#     cont=0
#     for i in range(len(cadena)):
#         if cadena[i].islower()==True:
#             cont+=1
#
#     return cont

#Sin .islower()
def lowCaseInString(cadena):
    cont=0
    for i in cadena:
        if i==i.lower() and i!=" ":
            cont+=1
    return cont

print(lowCaseInString(cadena))

#Ejercicio 3
cadena="Corre Curro Por Que Currucu Corre Mas"

#.isupper()
# def upperCaseInString(cadena):
#     cont=0
#     for i in range(len(cadena)):
#         if cadena[i].isupper()==True:
#             cont+=1
#
#     return cont

#Sin .isupper()
def upperCaseInString(cadena):
    cont=0
    for i in cadena:
        if i==i.upper() and i!=" ":
            cont+=1
    return cont

print(upperCaseInString(cadena))

#Ejercicio 4
cadena="Corre 3 Curro Por 2 Que Curr4ucu Corre Mas"

def numberInString(cadena):
    cont=0
    for i in range(len(cadena)):
        if cadena[i] in "0123456789":
            cont+=1
    return cont

print(numberInString(cadena))

#Ejercicio 5
cadena="anilina"

def palindrome(cadena):
    cadenaRevertida=""
    resultado=False
    
    for i in cadena:
        cadenaRevertida=i+cadenaRevertida
    
    if cadena==cadenaRevertida:
        resultado=True
    return resultado

print(palindrome(cadena))

#Ejercicio 6
texto="shybaoxlna"
palabra="hola"

def palabraEscondida(texto, palabra):
    cont=0
    
    for i in texto:
        if cont<len(palabra) and palabra[cont]==i:
            cont+=1

    return cont==len(palabra)

print(palabraEscondida(texto, palabra))
'''
#Ejercicio 7
'''7.Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase
y deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla
por la tercera.'''

#Ejercicio 8
#Ejercicio 9
#Ejercicio 10