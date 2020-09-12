numeroDecimal=0 
numeroBinario="" 
numerito=""
resto=0 
print "Numero decimal a binario" 
numeroDecimal=int(raw_input('Introduce numero decimal:')) 
print "Numero decimal leido: ",numeroDecimal 
while (numeroDecimal>=2): 
    resto=numeroDecimal%2 
    numeroDecimal=(int)(numeroDecimal/2) 
    numeroBinario+=(str)(resto) 
numeroBinario+=(str)(numeroDecimal) 
lista=list(numeroBinario) 
lista.reverse() 
print "Numero binario obtenido: ",lista  
print numeroBinario

for elemento in lista:
     numerito+=(str)(elemento)
print numerito