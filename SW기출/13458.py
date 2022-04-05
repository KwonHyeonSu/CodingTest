# 13458 - 시험 감독

import sys

n = int(sys.stdin.readline()) #시험장 갯수
a = [*map(int, sys.stdin.readline().split())]
b, c = [*map(int, sys.stdin.readline().split())] #b = 총감독관, c = 부감독관

re = 0

for i in range(n):
    ans = 1
    if (a[i]-b) > 0:
        ans += (a[i]-b) // c
        if (a[i]-b) % c > 0 : ans += 1
    re += ans
    print(ans)

print(re)