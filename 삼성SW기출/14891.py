#14891 - 톱니바퀴

#n = 0
#s = 1

# 1 : 시계
# -1 : 반시계

# 왼쪽의 i2, 오른쪽 i[6] 

import sys
import copy

saw = [sys.stdin.readline() for i in range(4)]
k = int(sys.stdin.readline())

k_board = [list(map(int, sys.stdin.readline().split())) for i in range(k)]

#print(saw, k, k_board)

def rotate(saw, d): # d방향
    temp_list = []
    if d == 1: #시계방향
        #print('시계방향 회전')
        for i in range(7):
            temp_list.append(saw[i])
        if saw[-1] == '\n':
            temp_list.insert(0,saw[-2])
        else : temp_list.insert(0, saw[-1])

    elif d == -1:
        #print('반시계방향 회전')
        for i in range(7):
            temp_list.append(saw[i+1])
        temp_list.append(saw[0])
    #print('변환 후 : ', temp_list)
    return temp_list



def opposite(d):
    if d == 1: return -1
    else : return 1

after_saw = copy.deepcopy(saw)

def simulate(n, d): # n번째 톱니, d 방향
    after_saw[n] = rotate(saw[n], d)

    #오른쪽 방향
    r = n
    d_r = d
    while r < 3:
        if saw[r][2] != saw[r+1][6]: #극이 다를 경우
            d_r = opposite(d_r)
            after_saw[r+1] = rotate(saw[r+1], d_r)
            #print(f'{r} : {after_saw}')
        else : break
        r += 1
    
    #왼쪽 방향
    l = n
    d_l = d
    while l > 0:
        if saw[l][6] != saw[l-1][2]: #극이 다를경우
            d_l = opposite(d_l)
            after_saw[l-1] = rotate(saw[l-1], d_l)
            #print(f'{l} : {after_saw}')

        else : break
        l-=1

    



for rot in k_board:
    rot[0] -= 1
    simulate(rot[0], rot[1])
    saw = copy.deepcopy(after_saw)
    #print(f'after_saw : {saw},\n, rot : {rot}\n\n')

re = 0
for i in range(4):
    if after_saw[i][0] == '1':
        re += 2**i
print(re)
