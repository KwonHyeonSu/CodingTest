def solution(array, commands):
    answer = []
    for c in commands:
        ans = sorted(array[c[0]-1:c[1]])
        answer.append(ans[c[2]-1])
    return answer

a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(a, c)