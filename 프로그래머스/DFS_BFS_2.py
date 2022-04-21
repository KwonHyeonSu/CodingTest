
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for com in range(len(computers)):
        if visited[com] == False:
            #print(visited)      
            DFS(n, computers, com, visited)  
            answer += 1
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    
    for connect in range(len(computers)):
        if com != connect and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)   

n = 3
c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, c))