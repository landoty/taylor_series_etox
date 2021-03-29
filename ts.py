#Taylor Series Approx.

def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return(fact)

def ts(n,x):
    e=0
    for i in range(0,n):
        e=e+((x**i)/(factorial(i)))
    return("e^" + str(x) + " is approximately: " + str(e))

approx_e_by = int(input("How many terms to approximate e^x by: "))
e_to_the = int(input("Value of x: "))

print(ts(approx_e_by, e_to_the))
