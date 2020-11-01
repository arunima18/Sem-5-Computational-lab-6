import math
import Library


#function 3
def fxn_3(x):
    y=4/(1+(x**2))
    return y  
    

#Main function
sum1,sum2=Library.montecarlo(fxn_3,0,1,10)
print(sum1,sum2)

