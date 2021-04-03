def myMean(x):
    return sum(x)/len(x)
s = eval(input("Enter a list: "))
print("mean of given elements: ",round(myMean(s),2))
