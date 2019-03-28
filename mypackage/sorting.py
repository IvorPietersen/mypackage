def sum_array(array, count = 0, temp = 0):
    '''Return sum of all items in array'''
    while count < len(array):
        temp = temp + array[count]
        return sum_array(array, count + 1, temp)
    return temp

def factorial(n, count = 1, temp = 1, orig = 0):

    '''Return n!'''
    if n == 0:
        return 1
    if count == 1:
        orig = n
    if n <= 1:
        return n    
    else:
        count += 1
        temp = n * temp
        if count == orig:
            return temp
        else:
            return factorial(n - 1, count, temp, orig)

def factorial(n, count = 1, temp = 1, orig = 0):

    '''Return n!'''
    if count == 1:
        orig = n
    if n <= 1:
        return n
    else:
        count += 1
        temp = n * temp
        if count == orig:
            return temp
        else:
            return factorial(n - 1, count, temp, orig)

def reverse(word, lis = [], length = 0, counter = 0):
    '''Return word in reverse'''
    if lis == []:
        counter = 1
        length = len(word)
    if counter <= length:
        lis.append(word[length - counter])
        counter += 1
        return reverse(word, lis, length, counter)
    else:
        return ''.join(lis)
