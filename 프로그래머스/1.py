def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [0 for _ in range(n)]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    while queue:
        i = queue.pop(0)
        
        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distance[j] = distance[i] + 1
    distance.sort(reverse=True)
    answer = distance.count(distance[0])
    return answer

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6

print(solution(n, vertex))