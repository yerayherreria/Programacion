'''
Boletín Programación Modular III

Realizado por:Yeray Herrería Oña
'''
'''
#Ejercicio 1
caracter="r".upper()
texto="Corre curro por que currucu corre mas".upper()

def caractersInString(texto):
    cont=0
    for i in range(len(texto)):
        if texto[i]==caracter:
            cont+=1
    return cont

print(caractersInString(texto))

#Ejercicio 2
texto="Corre curro por que currucu corre mas"

#.islower()
# def lowCaseInString(texto):
#     cont=0
#     for i in range(len(texto)):
#         if texto[i].islower()==True:
#             cont+=1
#
#     return cont

#Sin .islower()
def lowCaseInString(texto):
    cont=0
    for i in texto:
        if i==i.lower() and i!=" ":
            cont+=1
    return cont

print(lowCaseInString(texto))

#Ejercicio 3
texto="Corre Curro Por Que Currucu Corre Mas"

#.isupper()
# def upperCaseInString(texto):
#     cont=0
#     for i in range(len(texto)):
#         if texto[i].isupper()==True:
#             cont+=1
#
#     return cont

#Sin .isupper()
def upperCaseInString(texto):
    cont=0
    for i in texto:
        if i==i.upper() and i!=" ":
            cont+=1
    return cont

print(upperCaseInString(texto))

#Ejercicio 4
texto="Corre 3 Curro Por 2 Que Curr4ucu Corre Mas"

def numberInString(texto):
    cont=0
    for i in range(len(texto)):
        if texto[i] in "0123456789":
            cont+=1
    return cont

print(numberInString(texto))

#Ejercicio 5
texto="anilina"

def palindrome(texto):
    cadenaRevertida=""
    resultado=False
   
    for i in texto:
        cadenaRevertida=i+cadenaRevertida
   
    if texto==cadenaRevertida:
        resultado=True
    return resultado

print(palindrome(texto))

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

#Ejercicio 7
texto="hola que pasa".lower()
palabra="pasa".lower()
sustituta="calabaza".lower()
def sustituirPalabra(texto,palabra,sustituta):
    cont=0
    empieza=0
    acum=0
    listaCadena=[]
    for i in range(len(texto)):
        if texto[i]==palabra[cont]:
            if acum==0:
                empieza=i
                acum=1
            cont=cont+1
        else:
            acum=0
            cont=0
    
    for i in texto:
        listaCadena.append(i)
        
    for i in range(cont):
        del listaCadena[empieza]
    
    for i in range(len(sustituta)):
        listaCadena.insert(empieza+i, sustituta[i])
    texto=""
    for i in listaCadena:
        texto+=i
    return texto

print(sustituirPalabra(texto, palabra, sustituta))

#Ejercicio 8
palabra="Abaco".upper()

def contarVocales(palabra):
    cont=0
    VOCALES="AEIOU"
    vocalesPalabra=""
    for letra in palabra:
        if letra in VOCALES and letra not in vocalesPalabra:
            vocalesPalabra+=letra
            cont+=1
    return cont
print(contarVocales(palabra))

#Ejercicio 9
texto="curso de programacion".upper()

def ordenarLetras(texto):
    VOCALES="AEIOU"
    vocalesFrase=""
    consonantesFrase=""
    for letra in texto:
        if letra!=" ":
            if letra in VOCALES:
                vocalesFrase+=letra
            else:
                consonantesFrase+=letra
        
    return consonantesFrase+vocalesFrase

print(ordenarLetras(texto))

#Ejercicio 10
texto="He estudiado mucho".upper()

def contarPalabras(texto):
    cont=0
    if texto[0]!=" ":
        cont+=1
    for i in range(len(texto)-1):
        if texto[i]==" " and texto[i+1]!=" ":
            cont+=1
    return cont

print(contarPalabras(texto))
'''
