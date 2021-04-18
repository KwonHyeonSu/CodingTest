#14501 - 퇴사
'''
2
3 10
1 20

5
3 50
1 1
3 3
2 2
1 1
'''

import sys
t = []
p = []
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

re_list = [0]*n

def func():
    global re_list
    tmp_list = re_list[:]        
    # 뒤에서 부터 탐색
    for i in range(n-1,-1,-1):

        # 상담 할 수 있을 때
        if board[i][0] < n-i+1:

            print('print', i+1, board[i][0])
            for k in range(board[i][0]):
                tmp_list[k+i] = 0
                
            tmp_list[i] = board[i][1]
            print('tmp : ', tmp_list)
            
            if sum(re_list) < sum(tmp_list) :
                re_list = tmp_list[:]
                print('re_listed!')
                
            print('re_list : ', re_list)
            tmp_list = re_list[:]

        else:
            print('else : ', board[i][0])
            pass

        


for i in range(n):
    t.append(board[i][0])
    p.append(board[i][1])

func()
print(sum(re_list))