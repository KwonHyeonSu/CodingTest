#16236 - 아기상어

import sys

n = int(sys.stdin.readline())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

baby = 2

# 상 좌 우 하
direction = [(-1,0), (0,-1), (0,1), (1,0)]
fish_list = []
def pprint(arr):
    n = len(arr)
    print('-----------')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()

fish = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            y, x = i, j
        elif 1<=arr[i][j]<=6:
            fish_list.append((i,j,arr[i][j]))
            fish += 1

time = 0
def dfs(y, x):
    global time
    

    for d in direction:
        dy, dx = y + d[0] , x + d[1]
        if 0<=dy<n and 0<=dx<n: #ny, nx 범위 지정
            #지나갈 수 있는 경우
            if board[dy][dx] <= baby:
                #먹는 경우
                if board[dy][dx] != baby and board[dy][dx] != 0:
                    fish += 1
                
                




    time += 1





        