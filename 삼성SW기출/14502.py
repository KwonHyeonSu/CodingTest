"""
4 6
0 0 1 0 0 0
0 2 1 0 0 0
0 0 1 0 0 2
1 1 1 0 0 2

"""

import sys
import copy

sys.setrecursionlimit(10**8)

n, m = [*map(int, sys.stdin.readline().split())]

board = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

def pprint(arr):
    n = len(arr)
    print('------------')
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end = ' ')
        print()

# 상 하 좌 우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def spread(board, y, x):
    re = 0
    for _ in range(4):
        ny = y + dy[_]
        nx = x + dx[_]
        if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 0:
            board[ny][nx] = 2
            board = spread(board, ny, nx)
    return board

visited = []

def simulate(board):
    zero_list = []
    virus_list = []
    max_ = 0

    # 0의 좌표를 모두 찾는다.
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                zero_list.append((i,j))

    # 바이러스 좌표 리스트 만듬
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus_list.append((i,j))

    # 임시 보드를 만들어서
    l = len(zero_list)
    
    for a in range(l-2):
        for b in range(a+1, l-1):
            for c in range(b+1, l):
                tmp_board = copy.deepcopy(board)
                _a, _b, _c = zero_list[a], zero_list[b], zero_list[c] # 벽 3개를 세울 수 있는 모든 경우의 수
                #print(_a, _b, _c)x
                tmp_board[_a[0]][_a[1]] = 1
                tmp_board[_b[0]][_b[1]] = 1
                tmp_board[_c[0]][_c[1]] = 1

                #pprint(tmp_board)

                #초기 바이러스 개수만큼 돌림
                for i in range(len(virus_list)):
                    tmp_board = spread(tmp_board, virus_list[i][0], virus_list[i][1])
                
                re = 0
                re = sum([tmp_board[i].count(0) for i in range(n)])

                max_ = max(max_, re)
                        
                #print('re : ', re)

                tmp_board[_a[0]][_a[1]] = 0
                tmp_board[_b[0]][_b[1]] = 0
                tmp_board[_c[0]][_c[1]] = 0
    return max_

print(simulate(board))


