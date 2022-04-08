import collections
import functools

def solution(clothes):
    cnt = collections.Counter(kind for name, kind in clothes)
    return functools.reduce(lambda x, y : x*(y+1), cnt.values(), 1)-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))