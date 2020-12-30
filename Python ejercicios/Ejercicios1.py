def dcto(num,porc):
    return(num-(num*porc/100))

def coniva(precio,porc):
    """ función que aplica un IVA a un precio, aunque en realidad el IVA es variable y más bien es un aumento """
    return(precio+precio*porc/100)

def precio_canasta(canasta, funcion):
    '''
    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
    Parámetros:
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    '''
    total=0
    for precio, descuento in canasta.items():
        total += funcion(precio, descuento)
    return total

print(dcto(500,20))    
print(coniva(100,22))
print("Precio de canasta: ", precio_canasta({1000:20, 500:10, 100:1}, dcto))
print("Precio con IVA de canasta: ", precio_canasta({1000:20, 500:10, 100:1}, coniva))

#-------------------- contar letras ----------------
nombre=input("**** Ingresa tu nombre ")
print("nombre ",nombre, " tiene ",len(nombre)," letras ")

#------------- cuenta -----------------
# calcular ((3+2)/2.5) todo al cuadrado
print("resultado= ",pow((3+2)/(2*5),2))

#------------------ Calcula la suma de los números desde 1 al ingresado  -------------------
def sumaNros(num):
    print("la suma de los números desde 1 hasta ", num," es ",str((num*(num+1))/2))

nro=input("Indica un número: ")
sumaNros(int(nro))

#-------------- Calculo de masa corporal ----------------

peso=input("Ingrese su peso ")
altura= input("Ingrese su altura en centímetros ")
mc=int(peso)/((int(altura)/100)**2)
print("Su masa corporal es: ",round(mc,2))

