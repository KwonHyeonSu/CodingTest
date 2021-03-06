from functools import reduce

def solution(jobs):
    
    start = 0
    answer = 0
    length = len(jobs)
    
    jobs = sorted(jobs, key = lambda x : x[1])
    
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
        # print("break", start, answer, jobs)
        if i == len(jobs) -1:
            start += 1
    return answer // length
    
    
    
j = [[0, 3], [1, 9], [2, 6]]

print(solution(j))