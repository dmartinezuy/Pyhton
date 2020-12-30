# Factorial de un número 
def Factorial(num):
    i=1
    fact=1
    while i<num:
        print("i=",i)
        fact += fact*i
        i +=1
    
    return(fact)

print("factorial 5: ",Factorial(5)) 
