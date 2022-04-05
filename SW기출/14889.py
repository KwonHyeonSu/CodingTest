# 14889

import sys
from itertools import combinations

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

team = [i for i in range(n)]
team_list = list(combinations(team, n//2))

minval = 10**5
for i in range(len(team_list)//2):
    
    team = team_list[i]
    score_a = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            score_a += board[member][k]
    
    team = team_list[-i-1]
    score_b = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            score_b += board[member][k]
    
    minval = min(minval, abs(score_a - score_b))

print(minval)