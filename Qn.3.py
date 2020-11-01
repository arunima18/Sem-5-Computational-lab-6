import math
import Library


#function 3
def fxn_3(x):
    y=4/(1+(x**2))
    return y  
    

#Main function

#sum1=Library.montecarlo(fxn_3,0,1,10)
#print(sum1)

list_N=[]
list_value=[]

for i in range (1,4000):
    N=i*10 
    montecarlo=Library.montecarlo(fxn_3,0,1,N)
    list_N.append(N)
    list_value.append(montecarlo)
    
print(list_N)
print(list_value)
    

