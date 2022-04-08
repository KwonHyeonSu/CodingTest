
def solution(prices):
    ans = []
    
    for i in range(len(prices)-1):
        endVal=-1
        for j in range(i+1, len(prices)):
            #print(prices[i], prices[j])
            if prices[i] > prices[j]:
                endVal = j
                break
        if endVal == -1:
            endVal = len(prices)-1
        #print('endval : ', endVal)
        ans.append(endVal-i)
    ans.append(0)
    return ans
p = [1,2,3,2,3]


solution(p)