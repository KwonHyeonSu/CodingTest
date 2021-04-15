"""
5
100 200 300 400 200
300 243 432 334 555
999 111 0 999 333
888 777 222 333 900
100 200 300 400 500

=>7501

"""

import sys
n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
ans = 0
def pprint(arr):
    n = len(arr)
    print('---------------')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()

left_move = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
down_move = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,'a',10,0],[0,0,5,0,0]]
right_move = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,'a',5],[0,1,7,10,0],[0,0,2,0,0]]
up_move = [[0,0,5,0,0],[0,10,'a',10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]


def spread(x, y, move, board, out):

    temp = 0
    nx, ny = x-2, y-2

    for i in range(5):
        for j in range(5):
            if move[i][j] != 'a' and move[i][j] != 0:
                if 0 <= i+nx < n and 0 <= j+ny < n:
                    board[i+nx][j+ny] += board[x][y]*move[i][j]//100
                else:
                    out += board[x][y]*move[i][j]//100
                temp += board[x][y]*move[i][j]//100
            elif move[i][j] == 'a':
                remain = (i,j)
    if 0<=remain[0]+nx<n and 0<=remain[1]+ny<n:
        board[remain[0]+nx][remain[1]+ny] += board[x][y]-temp
    else:
        out += board[x][y]-temp
    board[x][y] = 0

    return board, out
    


#left, down, right, up
d = [(0,-1), (1,0), (0,1), (-1,0)]

x, y = n//2, n//2
times = 1
flag = 0

while flag != 1:
    for i in range(4):
        dx, dy = d[i]
        for j in range(times):
            x, y = x+dx, y+dy
            # left
            if i == 0:
                board, ans = spread(x, y, left_move, board, ans)
                
            elif i == 1:
            # down
                board, ans = spread(x, y, down_move, board, ans)

            elif i == 2:
            # right
                board, ans = spread(x, y, right_move, board, ans)

            elif i == 3:

            # up
                board, ans = spread(x, y, up_move, board, ans)

            if (x,y) == (0,0):
                flag = 1
                break
            

        if i == 1 or i == 3:
            times += 1

        if flag == 1:
            print(ans)
            break
