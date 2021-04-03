# Discount
def discount(d):
    if 1000>d>=500: 
        print("Total discount",(5*d)/100)
        print("Final price",(95*d)/100)
    elif 2000>d>=1000: 
        print("Total discount",(8*d)/100)
        print("Final price",(92*d)/100)
    elif d>=2000:
        print("Total discount",(10*d)/100)
        print("Final price",(90*d)/100)
    else:
        print("Enter a higher value")

n = int(input("Enter a amount: "))
m = input("Are you member of store(y/n): ")
if m=='y' :
    n=95*n/100
discount(n)
        
        
        
        
