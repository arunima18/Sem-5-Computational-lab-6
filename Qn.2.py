import math
import Library

#Function 2 
def fxn_2(x):
    y=math.exp(-x**2)
    return y 
    
#function to find N for upper bound error given 
def find_N_rectangle(a,b,f2_max_mod, tol):
    n = (((b-a)**3/(24*tol))*f2_max_mod)**0.5
    print(" N for midpoint method for",tol,"error:",math.ceil(n))
    return math.ceil(n)

def find_N_trapezoid(a,b,f2_max_mod,tol):
    n = (((b-a)**3/(12*tol))*f2_max_mod)**0.5
    print("N for trapezoidal method for",tol,"error:",math.ceil(n))
    return math.ceil(n)

def find_N_simpson(a,b,f4_max_mod,tol):
    n = (((b-a)**5/(180*tol))*f4_max_mod)**0.25
    if (math.ceil(n) % 2 != 0):
        print("N for simpson rule method for",tol,"error:",math.ceil(n)+1)
        return math.ceil(n) +1
    else:
        print("N for simpson rule method for",tol,"error:",math.ceil(n))
        return math.ceil(n)
        
        
        
#Main function 

#running the functions to find the desired values of N for all 3 itegration method
N_rect=find_N_rectangle(0,1,2,0.001)

N_trap=find_N_trapezoid(0,1,2,0.001)

N_simp=find_N_simpson(0,1,12,0.001)

#using the 3 found values as N in respective integrations
p=Library.Rect_(0,1,fxn_2,N_rect)
q=Library.trapezium(0,1,fxn_2,N_trap)
r=Library.simpson(0,1,fxn_2,N_simp)



print("Value of I by Rectangle/midpoint method:",p)
print("Value of I by trapezoidal method:",q)
print("Value of I by simpson rule method:",r)

    


           
    
'''
 N for midpoint method for 0.001 error: 10
N for trapezoidal method for 0.001 error: 13
N for simpson rule method for 0.001 error: 4
Value of I by Rectangle/midpoint method: 0.7471308777479975
Value of I by trapezoidal method: 0.7464612610366896
Value of I by simpson rule method: 0.7468553797909873





'''

           
    