#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""nombre=input("Digite su nombre: ")
print(nombre*10)
print((nombre+'\n')*10)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad=int(input("Digite su edad: "))
for i in range(1, int(edad)+1):
    print (i)

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 
# hasta ese número separados por comas.
nro=int(input("Digite un número: "))
for i in range(1, nro+1):
    if(i%2!=0):
        print(i, " es impar")

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
# desde ese número hasta cero separados por comas.
nro=int(input("Digite un número para cuenta regresiva: "))
numeros=""
for i in range(nro, 0, -1):
    numeros=numeros+str(i)+','

print(numeros)    

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1,11):
    print("\ntabla del "+str(i)+":")
    for j in range(1,11):
        print(str(i)+"x"+str(j)+"="+str(i*j))
"""
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
""" 1
    3 1
    5 3 1
    7 5 3 1
    9 7 5 3 1        """
"""    
texto=""    
for i in range(1,10,2):
    print (str(i)+" "+texto)
    texto=""
    for j in range(i, 0, -2):
        texto+=str(j)+" " 

#Escribir un programa que pida al usuario una palabra y luego muestre 
#por pantalla una a una las letras de la palabra introducida empezando por la última. 
palabra=input("Ingrese una palabra ")       
for i in reversed(palabra):
    print(i)
"""
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.    
frase=input("Ingrese una frase: ")
letra=input("Ingrese una letra  buscar: ")
cant=0
pos=0
while (pos!=-1):
    pos=frase.find(letra, pos+1)
    if (pos!=-1):
        cant+=1

print("la letra ",letra, " se encuentra ",str(cant)," veces")
