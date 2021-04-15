# 12100

import sys
import copy

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def pprint(arr):
    print('--------------')
    N = len(arr)
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()

def rotate(n, b):
    new_list = copy.deepcopy(b)
    for i in range(n):
        for j in range(n):
            new_list[j][n-1-i] = b[i][j]
    return new_list

def convert(n, b):
    new_list = [i for i in b if i!=0]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i!=0]
    return new_list + [0]*(n-len(new_list))

def dfs(n, b, count):
    result = max([max(i) for i in b])
    if count == 0:
        return result

    for _ in range(4):
        c = [convert(n, i) for i in b]
        result = max(result, dfs(n, c, count-1))
        b = rotate(n, b)
    return result

print(dfs(n, board, 5))