""" Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y 
la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que
 saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
 Escribir un programa que lea el número de payasos y  muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
payasos=input ("Ingrese el número de payasos vendidos: ")
munecas=input ("Ingrese el número de muñecas vendidas: ")
peso=(int(payasos)*112)+(int(munecas)*75)
print("El peso total del pedido es: ",peso," gramos.")

#-----------------------------------------------------------------------------------
""" Cálculo de pago de impuesto según franjas """
renta=int(input("Ingrese el monte de su renta "))
if(renta<10000):
    print("Le corresponde abonar un 5%")
elif (renta<20001):
    print("Le corresponde abonar un 15%")
elif (renta<35001):
    print("Le corresponde abonar un 20%")
elif (renta<60001):
    print("Le corresponde abonar un 30%")
else:
    print("Le corresponde abonar un 60%")
