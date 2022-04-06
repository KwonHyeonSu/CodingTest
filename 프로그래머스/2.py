from collections import defaultdict

def solution(n, results):
    answer = 0

    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for winner, loser in results:
        win_graph[winner].add(loser)
        lose_graph[loser].add(winner)
    
    for i in range(1, n+1):
        #i에게 진 사람은 i를 이긴 사람에게도 진 것
        for loser in win_graph[i]:
            lose_graph[loser].update(lose_graph[i])
        for winner in lose_graph[i]:
            win_graph[winner].update(win_graph[i])
            
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1
    

    
    return answer




n = 5
results = [[4,3], [4,2], [3,2], [1,2], [2,5]]
print(solution(n, results))