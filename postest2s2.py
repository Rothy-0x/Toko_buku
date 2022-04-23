listKu = ['galda', 'zaki', ['ibnu', 'zaki'], 'kalam', ['zaki', 'ari', 'ibnu'], 'zaki']
list1 = []
list2 ={}

def merge_sort(lst): 
    if len(lst) <= 1: 
        return lst 
    mid = len(lst) // 2 
    left = merge_sort(lst[:mid]) 
    right = merge_sort(lst[mid:]) 
    return merge(left, right) 

def merge(left, right): 
    result = [] 
    i, j = 0, 0 
    while i < len(left) and j < len(right): 
        if left[i] <= right[j]:
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
    result += left[i:] 
    result += right[j:] 
    return result

def fibonnaci(arr, x, n):
    fib2 = 0 
    fib1 = 1  
    fib = fib2 + fib1 
    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    offset = -1
    while (fib> 1):
        i = min(offset+fib2, n-1)
        if (arr[i] < x):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif (arr[i] > x):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib- fib1
        else:
            return i
    if(fib1 and arr[n-1] == x):
        return n-1
    return -1

for i in range(len(listKu)):
    if(type(listKu[i])) == str: 
        list1.append(listKu[i])
    else:
        list2[i] = merge_sort(listKu[i])

list1 = merge_sort(list1)
for index in list2 :
    list1.insert(index, list2[index])
print(list1)
for i in reversed(range(len(list1))):
    if type(list1[i]) == str:
        if list1[i] == 'zaki':
            print(f'zaki berada di array index ke -',i)
    elif  type(list1[i]) == list:
        column = fibonnaci(list1[i], 'zaki', len(list1[i]))
        if column != -1:
            print(f'zaki berada di index ke {i} kolom {column}')