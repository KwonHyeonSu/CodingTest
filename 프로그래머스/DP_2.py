def solution(triangle):
    answer = 0
    triangle = [[0] + t + [0] for t in triangle]

    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    print(triangle)
    

t = [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5]]
print(solution(t))