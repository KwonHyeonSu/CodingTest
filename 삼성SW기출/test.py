'''
3 2
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 0 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2

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

N, Q = map(int, sys.stdin.readline().split())
N_size = 2**N
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(N_size)]
Q = list(map(int, sys.stdin.readline().split()))

def pprint(arr):
    print('------------------')
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()

dir = [(0,1), (1,0), (-1,0), (0,-1)]

def Rotate(L_size):
    # 회전
    for x in range(0, N_size, L_size):
        for y in range(0, N_size, L_size):
            temp = [ice[x+i][y:y+L_size] for i in range(L_size)]
            
            for i in range(L_size):
                for j in range(L_size):
                    ice[x+i][y+j] = temp[L_size-1-j][i]

    # 인접한 칸 계산
    cnt = [[0] * N_size for _ in range(N_size)]
    for x in range(N_size):
        for y in range(N_size):
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < N_size and 0 <= ny < N_size and ice[nx][ny]:
                    cnt[x][y] += 1

    # 얼음 제거
    for x in range(N_size):
        for y in range(N_size):
            if cnt[x][y] < 3 and ice[x][y] :
                ice[x][y] -= 1

#(x,y)가 속한 덩어리의 크기
def dfs(x, y):
    ret = 1
    ice[x][y] = 0
    for d in dir:
        nx, ny = x+d[0], y+d[1]
        if 0 <= nx < N_size and 0 <= ny < N_size and ice[nx][ny] != 0:
            ret += dfs(nx, ny)
    return ret



for L in Q :
    Rotate(2 ** L)

print(sum(map(sum,ice)))

ans = 0
for x in range(N_size):
    for y in range(N_size):
        if ice[x][y]:
            ans = max(ans, dfs(x, y))
    

print(ans)
    
