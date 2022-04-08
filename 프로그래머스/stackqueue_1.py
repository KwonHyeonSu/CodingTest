from collections import Counter

def findX(x, y):
    v = (100-x) / y
    if v % 1 != 0:
        return int(v)+1
    return int(v) 


def solution(progresses, speeds):
    answer = []
    
    for i, v in enumerate(progresses):
        val = findX(v, speeds[i])
        if len(answer) > 0 and val < answer[-1] :
            answer.append(answer[-1])
        else : answer.append(val)

    return list(Counter(answer).values())

progresses = [93, 30, 55]

speeds = [1, 30, 5]
solution(progresses, speeds)