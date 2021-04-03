#calculate power
def power(base,exp=2):
    return base**exp
base = int(input('Enter base: '))
ch = input('want to enter exponent value(y/n)?: ')
if ch in 'yY':
    exp=int(input('Enter base: '))
    print('Power of given values',base,'and',exp,':',power(base,exp))
else:
    print('square of given value',base,':',power(base))
