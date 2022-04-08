from audioop import reverse


def solution(priorities, location):
    
    map = list(zip(priorities, [x for x in range(len(priorities))]))
    answer = []
    while map:
        val = map.pop(0)

        if len(map) > 0 and val[0] < max([x[0] for x in map]):
            map.append(val)
        else :
           answer.append(val[1]) 
        print(answer)
        
    return answer.index(location)+1

        
    


priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))