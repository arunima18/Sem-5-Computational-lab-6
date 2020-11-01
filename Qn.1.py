#Library
import math
import Library

#Funtion 1 
def fxn_1(x):
    y=x/(1+x)
    return y  
    
    


#Main Function


#for N=5
print('For N=5')
sum1f1=Library.Rect_(0,1,fxn_1,5)
print('The value of I using midpoint method is', sum1f1)
sum1f2=Library.trapezium(0,1,fxn_1,5)
print('The value of I using trapezium method is',sum1f2)
sum1f3=Library.simpson(0,1,fxn_1,5)
print('The value of I using simpson method is',sum1f3)
#for N=10 
print('For N=10')
sum2f1=Library.Rect_(0,1,fxn_1,10)
print('The value of I using midpoint method is',sum2f1)
sum2f2=Library.trapezium(0,1,fxn_1,10)
print('The value of I using trapezium method is',sum2f2)
sum2f3=Library.simpson(0,1,fxn_1,10)
print('The value of I using simpson method is',sum2f3)
#for N=25
print('For N=25')
sum3f1=Library.Rect_(0,1,fxn_1,25)
print('The value of I using midpoint method is',sum3f1)
sum3f2=Library.trapezium(0,1,fxn_1,25)
print('The value of I using trapezium method is',sum3f2)
sum3f3=Library.simpson(0,1,fxn_1,25)
print('The value of I using simpson method is',sum3f3)



'''

Analytical value: 1.3068528194

Output:

For N=5
The value of I using midpoint method is 0.30809211428406474
The value of I using trapezium method is 0.3043650793650794
The value of I using simpson method is 0.2158730158730159
For N=10
The value of I using midpoint method is 0.30716463959003976
The value of I using trapezium method is 0.3062285968245721
The value of I using simpson method is 0.3068497693110696
For N=25
The value of I using midpoint method is 0.3069028019555278
The value of I using trapezium method is 0.3067528394240818
The value of I using simpson method is 0.2871915019453158




'''


        
        
        
        
            
        
        
        
    
