#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.

asignaturas=[]
materia=""
while (materia != "fin"):
    materia=input("Ingrese una materia (fin para salir)")
    if(materia!="fin"):
        asignaturas.append(materia)

print("la curricula se compone de: ", asignaturas)    

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
asignaturas=[]
materia=""
while (materia != "fin"):
    materia=input("Ingrese una materia del curso (fin para salir)")
    if(materia!="fin"):
        asignaturas.append(materia)

for i in(asignaturas):
    print("Yo estudio ",i)

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla # con el mensaje En <asignatura>
#  has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes 
# notas introducidas por el usuario.
asignaturas=[]
notas=[]
materia=""
while (materia != "fin"):
    materia=input("Ingrese una materia del curso (fin para salir): ")
    if(materia!="fin"):
        asignaturas.append(materia)
        nota=input("Ingrese la nota con que aprobó: ")
        notas.append(nota)

print("largo ",len(asignaturas))
for i in range(0, len(asignaturas)):
    print("En la materia ",asignaturas[i], " me saque nota ",notas[i])

#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista
#  y los muestre por pantalla ordenados de menor a mayor.
loteria=[]
nro=9
while (nro > 0):
    nro=int(input("Ingrese una número de la loteria, (0 para fin)"))
    if(nro > 0):
        loteria.append(nro)
loteria.sort()
for i in(loteria):
    print("Número ganador ",i)

#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

lista=[1,2,3,4,5,6,7,8,9,10]
lista.sort(reverse=True)
print(lista)

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
#  pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
asignaturas=[]
notas=[]
materia=""
while (materia != "fin"):
    materia=input("Ingrese una materia del curso (fin para salir): ")
    if(materia!="fin"):
        asignaturas.append(materia)
        nota=int(input("Ingrese la nota que sacó (con 3 o menos debe recursar): "))
        if(nota>3):
            asignaturas.pop()

for i in range(len(asignaturas)):
    print("Debe recursar la materia ",asignaturas[i])

#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
# y muestre por pantalla la lista resultante.

lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(lista, "largo de lista ",len(lista))
for i in range(len(lista), 1 , -1):
   # print("valor de i=",i)
    if (i%3==0):
        #print("saco ", lista(i))
        lista.pop(i-1)

print(lista)        

#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra=input("ingrese palabra para ver si es Palíndromo: ")
lista_palabra=list(palabra)
lista_inversa=list(reversed(palabra))
print(lista_palabra, lista_inversa)
l=len(palabra)
palidroma=True
for i in range(0, l):
    #print(lista_palabra[i],lista_inversa[i])
    if(lista_palabra[i]!=lista_inversa[i]):
        palidroma=False

print("Es Políndroma= ", palidroma)

#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra=input("Ingrese frase para ver vocales: ")
lista_palabra=list(palabra)
va=0
ve=0
vi=0
vo=0
vu=0
for i in lista_palabra:
    print(i)
    if (i=="a"):
        va+=1
    elif (i=="e"):
        ve+=1
    elif (i=="i"):
        vi+=1
    elif (i=="o"):
        vo+=1
    elif (i=="u"):
        vu+=1

print("Cantidad de veces que aparece a=",va," e=",ve," i=",vi," o=",vo," u=",vu)    
#Solución del ejercicio según sitio web:
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")


#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.
precios=[50, 75, 46, 22, 80, 65, 8]
max=0
min=100
for p in precios:
    if (p>max):
        max=p
    if (p<min):
        min=p

print("mínimo= ", min, " máximo= ", max)

#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

v1=(1,2,3)
v2=(-1,0,2)
prod=0
for a in range(len(v1)):
    prod+=v1[a]*v2[a]

print("el producto es ", prod)
