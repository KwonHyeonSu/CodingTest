# 17822 - 원판 돌리기

import sys

'''
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1

4 6 3
1 2 3 4 5 6
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9
2 1 4
3 0 1
2 1 2

'''

n, m, t = map(int,sys.stdin.readline().split()) 

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]



# n : 원판의 갯수
# m : 원판마다 정수의 갯수
# t : 회전 수
def pprint(arr):
    n = len(arr)
    print('-------------')
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end = ' ')
        print()

def rotate(rot, d):
    tmp_rot = []
    if d == 0: # 시계방향
        tmp_rot.append(rot[-1])
        for i in range(m-1):
            tmp_rot.append(rot[i])

    else: #반시계
        for i in range(1,m):
            tmp_rot.append(rot[i])
        tmp_rot.append(rot[0])
    return tmp_rot


re = 0
flag = 0 #인접한 수 있는가?
l = []
for _ in range(t):
    re = 0
    #회전 수행
    x, d, k = map(int, sys.stdin.readline().split())
    for i in range(n):
        if (i+1) % x == 0: #Xi의 배수일 때
            for _ in range(k): #k 번 회전
                board[i] = rotate(board[i], d)

    #인접한 수 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == board[i][(j+1)%m] and board[i][j] != 'x':
                flag = 1
                l.append([i, j])
                l.append([i, (j+1)%m])


    for i in range(m):
        for j in range(n-1):
            if board[j][i] == board[j+1][i] and board[j][i] != 'x':
                flag = 1
                l.append([j, i])
                l.append([j+1, i])
                

    for c in l:
        board[c[0]][c[1]] = 'x'
    l = []
    tmp = 0
    if flag == 0:
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'x':
                    re += board[i][j]
                else :
                    tmp += 1
        if re != 0:
            re = re/((n*m)-tmp)
        
        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    if board[i][j] != 'x' and board[i][j] > re:
                        board[i][j] -= 1
                    elif board[i][j] != 'x' and board[i][j] < re:
                        board[i][j] += 1
    #pprint(board)
    flag = 0

re = 0
for i in range(n):
    for j in range(m):
        if board[i][j] != 'x':
            re += board[i][j]
print(re)

