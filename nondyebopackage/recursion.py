def sum_array(array):

    '''Return sum of all items in array'''
    return sum(array)

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):

   '''Return n!'''

   if n == 1:
       return n
   elif n == 0 :
       return 1
   else:
       return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    reverse_word= ""
    for i in reversed(word):

        reverse_word+=i
    return reverse_word
    '''return word[::-1]'''
