import heapq

def solution(scovile, K):
    
    heapq.heapify(scovile)
    cnt = 0
    while K > scovile[0] and len(scovile) != 1:
        value = heapq.heappush(scovile, heapq.heappop(scovile) + heapq.heappop(scovile) * 2)
        cnt += 1
        
    if scovile[0] < K :
        return -1

    return cnt
    


scovile = [1,2,3,9,10,12]
K = 7
print(solution(scovile, K))
    