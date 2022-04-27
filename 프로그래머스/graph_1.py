from collections import deque


def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visit[1] = 1
    q = deque([1])
    
    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visit[next]:
                visit[next] = visit[x] + 1
                q.append(next)
    
    cnt = visit.count(max(visit))
    
    return cnt if cnt > 0 else 1    

n = 6
v = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n, v))