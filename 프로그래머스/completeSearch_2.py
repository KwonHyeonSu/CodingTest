import itertools

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per = []
    
    for i in range(1, len(numbers) + 1):
        per += list(itertools.permutations(nums, i))
    new = [int(("").join(p)) for p in per]
    
    for n in new:
        if n<2:
            continue
        check = True
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                check = False
                break
        if check:
            answer.append(n)
            
    return len(set(answer))
    
    
numbers = "011"
print(solution(numbers))
