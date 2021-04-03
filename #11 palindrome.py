def palindrome(x):
    if x==x[::-1]:
        print('The entered string is palindrome')
    else:
        print('The entered string is not palindrome')

n = input('Enter a string: ')
palindrome(n)
