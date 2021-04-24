#15683 - 감시

# 1번으로 2,3,4,5를 조합할 수 있음

import sys
import copy
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

di = [0, [[0],[1],[2],[3]], [[0,2], [1,3]],\
     [[0,1], [1,2], [2,3], [3,0]], \
    [[0,1,2],[1,2,3], [2,3,0], [3,0,1]], [[0,1,2,3]]]

cctv_list = []

def pprint(arr):
    n = len(arr)
    print('------------')
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end = ' ')
        print()

for i in range(n):
    for j in range(m):
        if 1<=board[i][j] <=5:
            cctv_list.append((i,j,board[i][j]))

cnt = len(cctv_list)
count = 0
re_min = 99999


def dfs(MAP, count):
    global re_min
    if cnt == count:
        re = 0
        for i in range(n):
            for j in range(m):
                if MAP[i][j] == 0:
                    re += 1
        re_min = min(re_min, re)
        return

    y,x,num = cctv_list[count]
    for i in di[num]: #cctv 1개의 모든 경우의 수
        tmp = copy.deepcopy(MAP)
        for j in i:# cctv 1개의 1개 경우의 수
            ny, nx = y, x
            while True: #같은 방향으로 끝까지
                ny += dy[j]
                nx += dx[j]
                #print(ny, nx)
                if 0<=ny<n and 0<=nx<m and tmp[ny][nx] != 6 :
                    if tmp[ny][nx] == 0:                    
                        tmp[ny][nx] = '#'
                else:
                    break
            #pprint(tmp)
        dfs(tmp, count+1)
    
     
dfs(board, 0)



print(re_min)