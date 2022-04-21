def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for com in range(n):
        if visited[com] == False:
            DFS(computers, visited, com, n)
            answer += 1
    
    return answer

def DFS(computers, visited, com, n):
    visited[com] = True
    for connected in range(n):
        if connected != com and computers[com][connected] == 1:
            if visited[connected] == False:
                DFS(computers, visited, connected, n)
    

c = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

print(solution(n, c))