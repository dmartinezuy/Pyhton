#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
# y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
monedas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
mon=input("ingrese moneda ")
if (monedas.get(mon)):
    print(monedas.get(mon))
else:
    print("No existe moneda ")
"""
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
nom=input("ingrese su nombre ")
edad=input("ingrese su edad ")
dire=input("ingrese su dirección ")
datos={'Nombre':nom, 'Edad':edad, 'Dirección':dire}
print( datos['Nombre']," tiene ",datos['Edad']," años y vive en ",datos['Dirección'])

#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario  debe mostrar un mensaje informando de ello.

frutas={'Pera':1.35, 'Manzana':0.80, 'Banana':0.4, 'Naranja':0.33}
tufruta=input("Ingresa una fruta ")
kilos=input("Cuántos kilos quieres ")
if tufruta in frutas:
    print("Llevas ", kilos," de ", tufruta, " te cuesta $",round(float(frutas[tufruta])*float(kilos),2))
else:
    print("No existe esa fruta")

# Armar el diccionario con fruta:precio y mostrarlo al final
frutas={}
fruta=""
while fruta!="fin":
    fruta=input("Ingresa una fruta (fin para terminar) ")
    precio=input("Ingresa su precio por kilo ")
    if fruta!="fin":
        frutas[fruta]=precio

print (frutas)
for key in frutas:
    print (key , frutas[key])

#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
# muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
from datetime import datetime
fecha=input("Ingrese fecha en formato dd/mm/aaaa ")
formato="%d/%m/%Y"
fecdma= datetime.strptime(fecha, formato)
print (fecdma)
print("La fecha es ", fecdma.strftime("%d"), " de ", fecdma.strftime("%B"), " de ", fecdma.strftime("%Y"))

#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
# y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura>
#  es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

materias={}
mat=""
while mat!="fin":
    mat=input("Ingrese nombre materia (fin para terminar) ")
    if mat!="fin":
        cred=input("Ingrese el crédito de esa materia ")
        materias[mat]=cred
total=0
for asignatura  in materias:
    print("La materia ", asignatura, " precisa ", materias[asignatura], " créditos")
    total+= int(materias[asignatura])

print("Total de créditos del curso: ", total)    

#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés 
# separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras 
# y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.
traductor={}
esp_ing=""
while esp_ing!="fin":
    esp_ing=input("Ingrese una palabra en español:ingles (fin para terminar): ")
    if esp_ing!="fin":
        pal_esp=  esp_ing[0:esp_ing.find(":")]
        pal_ing= esp_ing[esp_ing.find(":")+1:len(esp_ing)]
        traductor[pal_esp]=pal_ing

print (traductor)
frase=input("Ingrese una frase en español: ")
lista_frase=frase.split(" ")
print(lista_frase)
frase_ing=""
for pal in lista_frase:
    frase_ing+=traductor[pal]+" "

print("en inglés= ", frase_ing) 

#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde 
# la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere 
# añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y 
# su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

opc="A"
facturas={}
while opc!="T":
    opc=input("Qué dese hacer? Agregar una factura (A), Pagar una (P), Terminar (T): ")
    if opc!="T":
        if opc=="A":
            nro=input("Ingrese número de factura a agregar: ")
            valor=input("Ingrese importe de la misma: ")
            facturas[nro]=valor
        elif opc=="P":
            nro=input("Ingrese número de factura a pagar: ")
            del facturas[nro]
            
        print("Facturas: ", facturas)
"""
#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario 
# en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
# correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
# (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. 
opc=0
clientes={}
while opc!=6:
    opc=int(input("Ingrese opción, (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar "))
    if opc!=6:
        if opc==1:
            nro=input("Ingrese número de cliente: ")
            nombre=input("Ingrese nombre del cliente: ")
            direccion=input("Ingrese dirección: ")
            preferente=input("Ingrese Preferente(S/N): ")
            clientes[nro]={"nombre":nombre, "direccion":direccion, "preferente":preferente}
            print(clientes[nro]["nombre"], clientes[nro]["direccion"])
        elif opc==2:
            nro=input("Ingrese número de cliente a eliminar: ")
            del clientes[nro]
        elif opc==3:
            nro=input("Ingrese número de cliente a mostrar: ")
            print("Los datos del cliente ",nro, " son: ", clientes[nro])
        elif opc==4:
            for cli in clientes:
                print("Cliente número ", cli, " Nombre: ",clientes[cli]["nombre"], " dirección: ", clientes[cli]["direccion"], " preferente: ", clientes[cli]["preferente"])
        elif opc==5:
            for cli in clientes:
                if clientes[cli]["preferente"]=="S":
                    print("Cliente Preferente número ", cli, " Nombre: ",clientes[cli]["nombre"], " dirección: ", clientes[cli]["direccion"], " preferente: ", clientes[cli]["preferente"])


            
