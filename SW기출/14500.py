#14500

"""
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
"""

import sys
import copy

sys.setrecursionlimit(10**5)

n, m = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 상 하 좌 우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def pprint(arr):
    n = len(arr)
    print('-------------')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')

        print()

re_list = []
re = []
def dfs(board, y, x, count):
    
    if count == 4:
        #print('count 4!')
        pprint(board)
        
        return board[y][x]

    tmp_board = copy.deepcopy(board)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 0:
            count += 1
            tmp_board[y][x] = 0
            #print(type(dfs(tmp_board, ny, nx, count)), type(board[y][x]))
            tmp = dfs(tmp_board, ny, nx, count) + board[y][x]
            re.append(tmp)
        
        elif board[ny][nx] == 0:
            count += 1
            re.append(0)
            return 0
        return max(re)
a = []

for i in range(n):
    for j in range(m):
            print('i, j : ', i, j)
            a.append(dfs(board, i, j, 0))
            #board[i][j] = 0
print(a)