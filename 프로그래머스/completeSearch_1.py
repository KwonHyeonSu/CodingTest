def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    re = [[1,0], [2,0], [3,0]]
    for i, v in enumerate(answers):
        #print(i, v)
        if v == one[(i % len(one))]:
            re[0][1] += 1
        if v == two[(i % len(two))]:
            re[1][1] += 1
        if v == three[(i % len(three))]:
            re[2][1] += 1
    max = 0
    for i in re:
        if max < i[1]:
            max = i[1]
    return[x[0] for x in re if x[1] == max]
a = [1,2,3,4,5]
solution(a)