# 20055 - 컨베이어 벨트 위의 로봇

import sys

n, k = map(int, sys.stdin.readline().split())

belt = list(map(int, sys.stdin.readline().split()))

robot_list = []
flag = 0
re = 0

def rotate(belt):
    tmp = belt[-1]
    for i in range((2*n)-1, 0, -1):
        belt[i] = belt[i-1]
    belt[0] = tmp
    i = 0
    while i < len(robot_list):
        robot_list[i] += 1
        if robot_list[i] > n-1:
            robot_list.remove(robot_list[i])
            i-=1
        i += 1
    return belt

def move(belt):
    global robot_list
    i = 0
    while i < len(robot_list):
        if robot_list[i] >= n-1: # 로봇이 내려가는 위치일 때
            robot_list.remove(robot_list[i])
            i -= 1
        
        elif (robot_list[i] + 1 not in robot_list) and belt[robot_list[i]+1] > 0: # 앞에 로봇이 없을 때 / 앞에 내구도 1 이상
            robot_list[i] += 1 # 앞으로 한 칸 이동
            belt[robot_list[i]] -= 1 # 내구도 1 감소
        i += 1
         
    return belt

while flag == 0:
    re += 1
    # 벨트 한칸 회전
    belt = rotate(belt)
    belt = move(belt)
    if belt[0] > 0 and (0 not in robot_list):
        robot_list.append(0)
        belt[0] -= 1 #내구도 감소
    if belt.count(0) >= k:
        flag = 1

print(re)
    
    