# 마법사 상어와 파이어볼

'''
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1

'''

import sys

sys.setrecursionlimit(10**5) # 반복 횟수 제한 늘리기
'''
def pprint(arr):
    n = len(arr)
    print('---------------------')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()
    print('---------------------')
'''
N, Q = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(2**N)]
arr = list(map(int, sys.stdin.readline().split()))
dir = [(1,0), (0,1), (-1,0), (0,-1)]

for L in arr:
    #회전
    k = 2 ** L
    for x in range(0, 2**N, k):
        for y in range(0, 2**N, k):
            
            temp = [ice[i][y:y+k] for i in range(x, x+k)]
            for i in range(k):
                for j in range(k):
                    ice[x+j][y+k-1-i] = temp[i][j]

    #인접한 얼음 카운팅
    cnt = [[0] * (2**N) for i in range(2**N)]
    for x in range(0,2**N):
        for y in range(0, 2**N):
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and ice[nx][ny]:
                    cnt[x][y] += 1

    #얼음 제거
    for x in range(0, 2**N):
        for y in range(0, 2**N):
            if ice[x][y] > 0 and cnt[x][y] < 3:
                ice[x][y] -= 1


print(sum(map(sum, ice))) #2차원 배열 합

#(x, y)가 속한 덩어리의 크기
def dfs(x, y):
    ret = 1
    ice[x][y] = 0
    for d in dir:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < 2**N and 0 <= ny < 2**N and ice[nx][ny]!=0:
            ret += dfs(nx, ny)
    return ret

ans = 0
for x in range(2**N):
    for y in range(2**N):
        if ice[x][y] > 0:
            ans = max(ans, dfs(x,y))

print(ans)