def num(x,y):
    if x[len(x)-1]>y[len(y)-1]:
        print(x)
    else:
        print(y)

n = input("Enter a number: ")
m = input("Enter a number: ")
num(n,m)
