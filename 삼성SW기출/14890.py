# 14890 - 경사로

import sys

n, l = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

compare = []

for i in range(n):
    tmp = []
    compare.append(board[i])
    for j in range(n):
        tmp.append(board[j][i])
    compare.append(tmp)
        
re = 2*n
tilt = []
flag = 0
for test in compare:
    #print('test : ', test)
    for i in range(n-1):
        if flag == 0:
            if abs(test[i] - test[i+1]) > 1: # 차이가 2 이상일 때
                #print('차이가 2 이상 \n')
                re -= 1
                flag = 1
                break # 다음 줄로 넘어감
            elif test[i] < test[i+1] : # 오른쪽이 더 클 때
                for j in range(0, l):
                    if i-j < 0 or test[i-j] != test[i] or (i-j) in tilt: # 조건 불만족
                        re -= 1
                        #print(f'오른쪽이 큼 : {i}와 {i+1}, re : {re}\n')
                        flag = 1
                        break
                    else:
                        tilt.append((i-j))

            elif test[i] > test[i+1]: # 왼쪽이 더 클 때
                for j in range(0, l):
                    if i+j+1 >= n or test[i+j+1] != test[i+1] or (i+j+1) in tilt:
                        re -= 1
                        #print(f'왼쪽이 큼 : {i}와 {i+j+1}, re : {re}\n')
                        flag = 1
                        break
                    else:
                        tilt.append((i+j+1))
    flag = 0
    #print('tilt : ', tilt)
    tilt = []
print(re)



