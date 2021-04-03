#wap to calculate binomial coefficent of of a number
def factorial(a):
    factorial = 1
    for i in range(1,a+1):
        factorial =factorial*i
    return factorial

def binomial_coefficient(n,r):
    num =factorial(n)/factorial(r)*factorial(n-r)
    return num

b =int(input("Enter a number : "))
q = int(input("Enter a number : "))
print("binomial coefficient",binomial_coefficient(b,q))

