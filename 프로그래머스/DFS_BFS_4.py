from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)


    for key, value in tickets:
        routes[key].append(value)

    for key in routes.keys():
        routes[key].sort(reverse = True)
    print(routes)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        print(tmp + "\t-->\t", end = "")
        if not routes[tmp]:
            print("no")
            answer.append(stack.pop())
            
        else:
            stack.append(routes[tmp].pop())
            print("yes, stack : ", end = "")
            print(stack)
    print(answer)


t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(t))