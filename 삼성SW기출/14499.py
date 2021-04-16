import sys

n, m, x, y, k = [*map(int, sys.stdin.readline().split())]

board = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

order = list(map(int, sys.stdin.readline().split()))

def pprint(arr):
    n = len(arr)
    print('------------')
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end = ' ')
        print()

dice = [0,0,0,0,0,0,0]

# 1-동쪽/ 2-서쪽 / 3 - 북쪽 / 4 - 남쪽
def change(d):
    if d == 1: #동쪽
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif d == 2:
        dice[4], dice[1], dice[6], dice[3] = dice[1], dice[3], dice[4], dice[6]
    elif d == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif d == 4:
        dice[5], dice[1], dice[6], dice[2] = dice[1], dice[2], dice[5], dice[6]

# 동 서 북 남
dx = [0,0,-1,1]
dy = [1,-1,0,0]
re = []
def func(d):
    global x, y
    nx, ny = x + dx[d-1], y + dy[d-1]
    if 0<=nx<n and 0<=ny<m:
        change(d)
        x, y = nx, ny
        if board[nx][ny] == 0:
            board[nx][ny] = dice[6]
        else:
            dice[6] = board[nx][ny]
            board[nx][ny] = 0
        re.append(dice[1])

    


for _ in range(k):
    func(order[_])
for i in range(len(re)):
    print(re[i])
    


        