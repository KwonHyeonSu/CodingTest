#14888 - 연산자 끼워넣기

'''
어려웠던 점
-7 // 6 을 하면 -2가 출력이 된다.

나누기를 할 땐 항상 조심히!

순열과 조합을 쓸 땐 itertools 라이브러리를 쓰자!
itertools.permutations(para)

'''
"""
3
1 1 1
0 1 0 1

2
-7 6
0 0 0 1
"""
import sys
import itertools

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
operator = ['+'] * op[0] + ['-'] * op[1] + ['*'] * op[2] + ['/'] * op[3]
op_list = list(itertools.permutations(operator))

def calc(val1, val2, op):
    #print('val1 : ', val1, 'val2 : ', val2, 'op : ', op)
    re = 0
    if op == '+':
        re = val1+val2
    
    elif op == '-':
        re = val1-val2

    elif op == '*':
        re = val1*val2
    
    elif op == '/':
        if val1 < 0:
            re = -((-val1) // val2)
        else :
            re = val1//val2

    if re < min_value or re > max_value:
        re = None

    #print('re : ', re)
    return re


min_value = -(10 ** 9)
max_value = (10 ** 9)

def func():
    global min_value, max_value
    ans = []
    for i in range(len(op_list)):
        tmp_ans = calc(arr[0], arr[1], op_list[i][0])
        for j in range(1, n-1):
            tmp_ans = calc(tmp_ans, arr[j+1], op_list[i][j])
            #print(tmp_ans)
        ans.append(tmp_ans)
    print(max(ans), min(ans), sep='\n')

#print(func())
func()
