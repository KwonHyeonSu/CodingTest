from audioop import reverse


def solution(citations):
    citations.sort(reverse = True)
    return max(list(map(min, enumerate(citations, start= 1)))))

    
c = [0,0,1,2,3]
solution(c)