def partisi(data, under, upper):
    pivot = data[upper]
    i = under - 1
    
    for j in range(under, upper):
        if data[j] < pivot:
            i = i + 1
            (data[i], data[j]) = (data[j], data[i])
            
    (data[i + 1], data[j]) = (data[j], data[i + 1])
    return i + 1

def quick(data, under, upper):
    if under < upper:
        p = partisi(data, under, upper)
        quick(data, under, p - 1)
        quick(data, p + 1, upper)


data = [53,20,19,78,43,10,27,3,14,98]
n = len(data)
quick(data, 0 , n- 1)
print(data)
