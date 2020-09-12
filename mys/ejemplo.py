dicc={'nombre':'Fernando','edad':32,'direccion':'zaragoza','lenguajes':['Python','Groovy','Scala']}
print dicc
print dicc.has_key('nombre')
print dicc.items()
for i in dicc:
  print"llave: ",i,"  valor: ",dicc[i]
otro=dicc.copy()
print otro
dicc.clear()
print dicc