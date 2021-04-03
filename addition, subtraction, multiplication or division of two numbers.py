#addition, subtraction, multiplication or division of two numbers
print('''addition = +
subtraction = -
multiplication = *
division = / ''')
def calculator(p,q):
    n =(input("Enter a operator : "))
    if n == "+":
        print(p+q)
    elif n== "-":
        print(p-q)
    elif n== "*":
        print(p*q)
    elif n== "/":
        print(p/q)
    else :
        print("invalid operator") 

f = float(input("Enter first number: "))
v = float(input("Enter second number: "))
calculator(f,v)
        
        
