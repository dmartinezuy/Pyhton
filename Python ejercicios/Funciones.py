#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def mcd(nro1, nro2):
    divisores1=[]
    divisores2=[]
    resto=1
    print(nro1)
    for i in range(nro1-1, 0, -1):
        #print(i)
        resto=nro1%i
        if resto==0:
            divisores1.append(i)

    #print(divisores1)
    for i in range(nro2-1, 0, -1):
        #print(i)
        resto=nro2%i
        if resto==0:
            divisores2.append(i)

    print(divisores1)
    print(divisores2)
    divisor=0
    for i in divisores1:
        for j in divisores2:
            if i==j:
                divisor=i
                print("divisor= ", divisor)
                break
            if divisor!=0:
                break
    print("El máximo común divisor de ",nro1, " y ",nro2," es: ", divisor)

def mcm(nro1, nro2):
    multiplos1=[]
    multiplos2=[]
    mayor=nro2
    if nro1>nro2:
        mayor=nro1
    for i in range(1, mayor+1):
        multiplos1.append(i*nro1)
        multiplos2.append(i*nro2)
    
    print("multiplo1= ",multiplos1)
    print("multiplo2= ",multiplos2)
    minimo=0
    for i in multiplos1:
        for j in multiplos2:
            if i==j:
                minimo=i
                break
        if minimo!=0:
            break
    print("El mínimo común múltiplo de ", nro1, " y ", nro2, " es: ", minimo)

mcd(890, 307)
mcm(80, 203)

#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
#Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
import operator
def cuenta_palabras(frase):
    lista_frase=sorted(frase.split(" "), key=str.lower)
    print("lista= ",lista_frase)
    ant=""
    for pal in lista_frase:
        if pal==ant:
            diccio[pal]+=1
        else:
            diccio[pal]=1
        ant=pal
    print(diccio)
    for pal in diccio:
        print("Palabra ",pal, " se repite: ",diccio[pal], " veces")

def mas_repetida(diccionario):
    diccio_ord=sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
    print(diccio_ord)
    print(diccio_ord[0])

diccio={}
cadena=input("Digite una frase: ")
cuenta_palabras(cadena)

mas_repetida(diccio)