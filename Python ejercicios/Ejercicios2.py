#---- Calculo el cociente y resto de una division ------
n=input("Ingresa el primer número ")
m=input("Ingresa el segundo número ")
cociente=int(float(n)/float(m))
resto=float(n) % float(m)
print ("cociente ",cociente, " resto ",resto)

#---------- Contar cuántos números 6 hay del 1 al 1500 ------
cant=0
for i in range(1, 1500):
    pos=str(i).find('6')
    if (pos!=-1):
        cant+=1
        print("Encontré el 6 en ",i)
        j=0
        while pos!=-1:
            pos=str(i).find('6',pos+1)
            if (pos!=-1):
                cant+=1
                print("Encontré otro 6 en ",i)

print("Cantidad: ",cant)
