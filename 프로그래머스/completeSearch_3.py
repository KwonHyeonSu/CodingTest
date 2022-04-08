def solution(brown, yellow):
    ans = []
    for row in range(2, brown//2):
        found = False
        for col in range(2, row+1):
            if brown == 2*(row+col) - 4 and yellow == (row-2)*(col-2):
                
                ans.append(row)
                ans.append(col)
                #print(ans)
                found = True
                break
        if found:
            break
    return sorted(ans, reverse=True)
b = 24
y = 24
solution(b, y)