l = [1,2,3,4,5]

def slicing(l, n):
    l.insert(0,l[-n:])


slicing(l, 3)
print(l)