#accepting a number as parameter and returns factorial of a given number
def factorial(a):
    factorial = 1
    for i in range(1,a+1):
        factorial =factorial*i
    return factorial

n = int(input("Enter a number to calculate the factorial : "))
print(factorial(n))

        
    
