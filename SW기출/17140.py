#17140-이차원배열과 연산

import sys
import collections
import copy

sys.setrecursionlimit(10**5)

r, c, k = map(int, sys.stdin.readline().split())
r -= 1
c -= 1
board = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]


def pprint(arr):
    print('-------------')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end = ' ')
        print()

def R():
    global board, count
    re = []
    for i in range(len(board)):
        counter = collections.Counter(board[i])
        
        keys = list(counter.keys())
        values = list(counter.values())
        
        for a, b in enumerate(keys):
            if b == 0:
                keys.pop(a)
                values.pop(a)
        l = len(keys)
        #print('key : ', keys)
        #print('values : ', values)
        

        # 값 정렬
        for j in range(l-1):
            for k in range(j+1, l):
                if keys[j] > keys[k]:
                    values[j], values[k] = values[k], values[j]
                    keys[j], keys[k] = keys[k], keys[j]

        # 개수 정렬
        for j in range(l-1):
            for k in range(j+1, l):
                if values[j] > values[k]:
                    values[j], values[k] = values[k], values[j]
                    keys[j], keys[k] = keys[k], keys[j]

        tmp = []
        for j in range(l):
            if len(tmp) <= 100:
                tmp.append(keys[j])
                tmp.append(values[j])
            else:
                break
                #print('100초과!')
        #print('tmp ' ,tmp)
        re.append(tmp)
    
    #print(re)

    # 0 채우기
    m = 0
    for i in range(len(re)):
        m = max(len(re[i]), m)
    
    gap = 0
    for i in range(len(re)):
        if len(re[i]) < m:
            gap = m - len(re[i])
        for j in range(gap):
            re[i].append(0)
        gap = 0
    board = copy.deepcopy(re)

def transform():
    re = []
    for i in range(len(board[0])):
        tmp = []
        for j in range(len(board)):
            tmp.append(board[j][i])
        re.append(tmp)
    return re

def C():
    global board
    board = transform()
    R()
    board = transform()

count = 0
while True:
    
    if r<len(board) and c < len(board[0]) and board[r][c] == k:
        print(count)
        break
    #print(f'{len(board)} , {len(board[0])}')
    if len(board) < len(board[0]): #열이 길다
        C()
        #print('c')
    else:
        R()
        #print('r')

    if count == 100 and board[r][c] != k:
        print('-1')
        break
    #pprint(board)
    #print(count)
    count += 1