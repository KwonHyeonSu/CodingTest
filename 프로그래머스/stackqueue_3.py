
def solution(bridge_length, weight, truck_weights):
    
    crossing = []
    passed = []
    time = 0
    while len(crossing) > 0 or truck_weights:
        for i in crossing:
            i[1] += 1
        for i in crossing:
            if i[1] == bridge_length:
                passed.append(crossing.pop(0)[0])

        
        
        if len(truck_weights) > 0 and truck_weights[0]+sum([x[0] for x in crossing]) <= weight:
            crossing.append([truck_weights.pop(0), 0])
        
        time += 1
        #print(time, "\t", passed, "\t", crossing, "\t", truck_weights)

        
    return time


bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]	

print(solution(bridge_length, weight, truck_weights))