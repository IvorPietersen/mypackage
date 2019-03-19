def sum_array(array, count = 0, temp = 0):
    '''Return sum of all items in array'''
    while count < len(array):
        temp = temp + array[count]
        return sum_array(array, count + 1, temp)
    return temp

def fibonacci(n):
    if n <= 3:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return 1
    else:

        return fibonacci(n - 1) + fibonacci(n - 2)

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

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    flag = False
    i = 0
    while i < len(items) - 1:
        if items[i] > items[i + 1]:
            items[i], items[i + 1] = items[i + 1], items[i]
            i = 0
        else:
            i += 1
    return items

def merge_sort(items, count = 0):

    '''Return array of items, sorted in ascending order'''
    count = 0
    records = []
    def split(sub_items):
        nonlocal count
        count += 1
        left =[]
        right = []
        i = 0
        j = len(sub_items) - 1
        while i < j:
            left.append(sub_items[i])
            i += 1
            j -= 1
        while i < len(sub_items):
            right.append(sub_items[i])
            i +=1
        return left, right, count

    def assign(segment):
        nonlocal records
        left, right, counter = split(segment)
        entry = (counter, left, len(left), right, len(right))
        records.append(entry)
        return records

    def grow(records):
        i = 0
        while i < len(records):
            check = 0
            if records[i][2] > 1:
                assign(records[i][1])
                check +=1
            if records[i][4] > 1:
                assign(records[i][3])
                check +=1
            if i == len(records) - 1:
                if check > 0:
                    i = 0
                    check = 0
                else:
                    break
            i+=1
        return records

    def order(list11, list12):
        list3 = []
        if len(list11) > len(list12):
            list1, list2 = list12, list11
        else:
            list1, list2, = list11, list12
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                list3.append(list1[i])
                i += 1
            else:
                list3.append(list2[j])
                j += 1
        if i < j:
            k = i
            tempor = list1
        else:
            k = j
            tempor = list2
        while k < len(tempor):
            list3.append(tempor[k])
            k +=1
        return list3

    def put_together(record):
        count = 1
        r = 1
        li = []
        li1 = []
        li2 = []
        while len(record) > r:
            if record[-r][2] == 1 and record[-r][4] == 1 and len(record[-r]) == 5:
                li1 = record[-r][1]
                li2 = record[-r][3]
                li.append(order(li1, li2))
                r +=1
            elif record[-r][2] == 1 and record[-r][4] != 1 and len(record[-r]) == 5:
                li.append(record[-r][1])
                r +=1
            elif record[-r][2] != 1 and record[-r][4] == 1 and len(record[-r]) == 5:
                li.append(record[-1 - r][3])
                r +=1

            else:
                r +=1

        return li

    def groupy(listing):
        if len(listing) % 2 == 0:
            f = 0
            lis5 = []
            while f+1 <= len(listing):
                inpu = (order(listing[f], listing[f+1]))
                lis5.append(inpu)
                f +=2
        else:
            f = 0
            lis5 = []
            while f+1 < len(listing) - 1:
                iup = (order(listing[f], listing[f+1]))
                lis5.append(iup)
                f +=2
            f -= 1
            pup = (listing[f])
            lis5.append(pup)
        temp = []
        for item in lis5:
            temp.append(item)
        return temp

    def sorteds(lists):
        while len(lists) > 1:
            lists = groupy(lists)
        return lists


    assigned = assign(items)
    grown = grow(assigned)

    singles = put_together(grown)
    grouped = groupy(singles)
    finale = sorteds(grouped)
    return finale
