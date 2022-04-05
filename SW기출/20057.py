# 마법사 상어와 토네이도

'''
5
0 0 0 0 0
0 0 0 0 0
0 10 0 0 0
0 0 0 0 0
0 0 0 0 0

=>10

5
0 0 0 0 0
0 0 0 0 0
0 100 0 0 0
0 0 0 0 0
0 0 0 0 0

=>85

5
100 200 300 400 200
300 243 432 334 555
999 111 0 999 333
888 777 222 333 900
100 200 300 400 500

=>7501
'''

import sys

N = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
out_sand = 0

def pprint(arr):
    print('----------------------')
    for i in range(N):
        for j in range(N):
            print(A[i][j], end = ' ')
        print()

finger = [N//2, N//2]
#up, down, right, left
direction = [(-1,0), (1,0), (0,1), (0,-1)]

def Push_sand(dir, sand, x, y):
    global maps, out_sand, N
    first_sand = sand
    move_left =[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01),
              (-1,-1,0.1),(1,-1,0.1),(0,-2,0.05)]
    move_right=[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),
              (-1,1,0.1),(1,1,0.1),(0,2,0.05)]
    move_up = [(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),
               (-2,0,0.05),(0,-2,0.02),(0,2,0.02)]
    move_down = [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),
                 (1,-1,0.1),(1,1,0.1),(2,0,0.05)]
    move_list = [move_up,move_down,move_right,move_left]
    last_move = [(-1,0,1), (1,0,1), (0,1,1), (0,-1,1)]
    for i in move_list[dir]:
        temp_x = x+i[0]
        temp_y = y+i[1]
        temp_sand = int(first_sand*i[2])
        sand -= temp_sand
        if temp_x < 0 or temp_y < 0 or temp_x >= N or temp_y >= N:
            out_sand += temp_sand
            continue
        maps[temp_x][temp_y] += temp_sand

    last_x = x+last_move[dir][0]
    last_y = y+last_move[dir][1]
    if last_x >= N or last_x < 0 or last_y >= N or last_y < 0:
        out_sand += sand
    else:
        maps[last_x][last_y] += sand
    


for idx in range(N-1):
    if(idx % 2 == 0):
        #left
        for _ in range(idx+1):
            finger[1] += direction[3][1]
            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]] = 0
            Push_sand(3, temp, finger[0], finger[1])
        
        #down
        for _ in range(idx+1):
            finger[0] += direction[1][0]
            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]] = 0
            Push_sand(1, temp, finger[0], finger[1])
            #Push_sand
    else:
        #right
        for _ in range(idx + 1):
            finger[1] += direction[2][1]
            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]] = 0
            Push_sand(2, temp, finger[0], finger[1])
        #up
        for _ in range(idx + 1):
            finger[0] += direction[0][0]
            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]] = 0
            Push_sand(0, temp, finger[0], finger[1])

for _ in range(N):
    finger[1] += direction[3][1]
    temp = maps[finger[0]][finger[1]]
    maps[finger[0]][finger[1]] = 0
    Push_sand(3,temp,finger[0],finger[1])

print(out_sand)
