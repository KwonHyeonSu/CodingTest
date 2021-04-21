a = [0,1,2,3]

for i in range(len(a)):
    #print(i, a[i])
    
    print(a.pop(i))
    i-=1
    print('i : ', i)