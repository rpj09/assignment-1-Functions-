#sum of first n natural numbers
def sumn(x):
    sum = 0
    for i in range(1,x+1):
        print(i,end=" ")
        sum = sum + i
    print("\nsum of n natural numbers is: ",sum)

n = int(input("Enter a number: "))
sumn(n)
    
