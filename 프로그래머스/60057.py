from itertools import combinations

def solution(s):
    
    for i in range(1, len(s)//2):
        p = list(combinations(s, 2))
        print(p)

s = "ab"
solution(s)