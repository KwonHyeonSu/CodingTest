
def solution(tickets):
    answer = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visited = [False] * len(tickets)
            answer.append(DFS(tickets, i, visited, []))

    answer.sort()
    answer[0].insert(0, "ICN")

    return answer[0]

def check(a):
    for i in a:
        if i == False:
            return False
    return True

def DFS(tickets, i, visited, result):

    visited[i] = True

    result.append(tickets[i][1])

    if check(visited) == True:
        #print("end, result : " , end = "")
        #print(result)
        return result

    for j in range(len(tickets)):
        if visited[j] == False and tickets[i][1] == tickets[j][0]:
            result = DFS(tickets, j, visited, result)
            return result





t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(t))