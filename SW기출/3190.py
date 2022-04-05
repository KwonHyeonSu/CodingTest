#3190 - 뱀

from collections import deque
import sys

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    if c == 'L': #왼쪽 회전
        d = (d - 1) % 4
    else:
        d = (d+1) % 4
    return d


# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def start():
    direction = 1 # 초기 방향(우)
    time = 1
    x, y = 0, 0
    visited = deque([[x, y]])
    arr[x][y] = 2
    while True:
        x, y = x + dx[direction], y + dy[direction]
        if 0 <= y < N and 0 <= x < N and arr[x][y] != 2:
            if not arr[x][y] == 1 : #사과가 없는 경우
                temp_x, temp_y = visited.popleft()
                arr[temp_x][temp_y] = 0 # 꼬리 제거
            arr[x][y] = 2
            visited.append([x, y])
            if time in times.keys(): 
                direction = change(direction, times[time])
            time += 1
        else: #몸에 부딪 / 벽에 부딪
            return time




if __name__ == "__main__":

    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    arr = [[0]*N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        arr[a-1][b-1] = 1
    L = int(sys.stdin.readline())
    times = {}
    for i in range(L):
        X, C = sys.stdin.readline().split()
        times[int(X)] = C
    print(start())