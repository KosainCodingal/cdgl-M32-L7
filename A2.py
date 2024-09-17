def minList(a):
    size = len(a)
    tmp = a[0]
    for i in range(1, size): tmp = min(tmp, a[i])
    return tmp

def maxList(a):
    size = len(a)
    tmp = a[0]
    for i in range(1, size): tmp = max(tmp, a[i])
    return tmp

a = [1, 6, 5, 0, 3]
print(minList(a))
print(maxList(a))