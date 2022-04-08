from ast import operator
import heapq

def solution(operations):    
    answer = []
    for o in operations:
        if o.startswith("I"):
            #print("1", o.split()[1])
            answer.append(int(o.split()[1]))
        elif o.startswith("D 1") and len(answer) > 0:
            #print("2", o.split()[1])
            answer.remove(int(max(answer)))
        elif o.startswith("D -1") and len(answer) > 0:
            #print("빼기", o.split()[1], min(answer))
            answer.remove(int(min(answer)))
    
    
    answer = list(map(int, answer))
    if answer == []:
        answer = [0,0]
    answer = [max(answer), min(answer)]
    #print(answer)
    
    return answer

o = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
solution(o)