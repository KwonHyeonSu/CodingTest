#14503 - 로봇청소기

import sys
n, m = list(map(int, sys.stdin.readline().split()))
r, c, d = list(map(int, sys.stdin.readline().split()))
if d == 1:
    d = 3
elif d == 3:
    d = 1
board = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
# 0-북 / 1-서 / 2-남 / 3-동
#북동남서 -< 북서남동
direction = [(-1,0), (0,-1), (1,0), (0,1)]
def full(r, c):
    for i in range(4):
        nr = r + direction[i][0]
        nc = c + direction[i][1]
        if board[nr][nc] == 0:
            return False
    return True

flag = 0
def clean():
    global r, c, d, board, flag
    board[r][c] = 2
    count = 0
    #print(r, c , '에 청소하였습니다., dir : ', d)
    #pprint(board)
    while flag != 1:
        a = (d+1)%4
        nr = r + direction[a][0]
        nc = c + direction[a][1]
        if 0<=nr<n and 0<=nc<m:
            if board[nr][nc] == 0: # 왼쪽에 청소할 공간 존재
                r, c, d = nr, nc, a # 회전
                board[r][c] = 2 #청소
                #count = 0
                #print(r, c , '에 청소하였습니다. dir : ', d)
                #pprint(board)
            
            elif full(r,c) == True:
                k = (d+2)%4
                nr, nc = r + direction[k][0], c + direction[k][1]
                if board[nr][nc] == 1:
                    #print('end')
                    flag = 1
                else:
                    #print('후진')
                    r, c = nr, nc #후진
                
            elif board[nr][nc] != 0: #회전만
                d = a
                #count += 1
                #print("회전! , dir : ", d)

    return sum(board[i].count(2) for i in range(n))

def pprint(arr):
    n = len(arr)
    print('------------')
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                print('\033[95m' + str(arr[i][j]) + '\033[0m', end = ' ')
            else :
                print(arr[i][j], end = ' ')
        print()

print(clean())