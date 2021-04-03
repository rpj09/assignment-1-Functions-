def fun(l):
    for i in l:
        if i.isnumeric():
            print(3*i)
        else:
            print(i+'#')

n=list(input('ENter a list: '))
fun(n)
