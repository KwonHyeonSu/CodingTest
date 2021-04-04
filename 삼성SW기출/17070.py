
def dfs(x, y, z): #가로 0, 대각선 1, 아래 2
    global k
    
    if x == n-1 and y == n-1 :
        k += 1
    #아래쪽으로 갈 수 있는경우 -> 1, 2
    if z == 1 or z == 2:
        if y + 1 < n:
            if d[y+1][x] == 0:
                dfs(x,y+1,2)
    #오른쪽으로 갈 수 있는 경우 -> 0, 1
    if z == 0 or z == 1:
        if x + 1 < n:
            if d[y][x+1] == 0:

                dfs(x+1, y, 0)
    #대각선으로 갈 수 있는 경우 -> 0, 1, 2
    if z == 0 or z == 1 or z == 2:
        if x+1 < n and y+1 < n:
            if d[y][x+1] == 0 and d[y+1][x] == 0 and d[y+1][x+1] == 0:
                dfs(x+1,y+1, 1)


n = int(input())
d = [[*map(int,input().split())] for _ in range(n)]
k = 0
#처음 시작 => (1,0)
dfs(1, 0, 0) 
print(k)
