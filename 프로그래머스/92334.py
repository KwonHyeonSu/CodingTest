from collections import defaultdict

def solution(id_list, report, k):
    reporting = defaultdict(list)
    reported = defaultdict(int)

    report = list(set(report))

    for i in id_list:
        reporting[i] = []

    for r in report:
        a, b = r.split()
        reporting[a].append(b)
        reported[b] += 1

    stopped = [x[0] for x in reported.items() if x[1] >= k]

    #print(stopped)
    #print(reporting)

    re = []

    for i in reporting.items():
        cnt = 0
        for j in i[1]:
            if j in stopped:
                cnt += 1
        re.append(cnt)
    #print(re)
    return re




i = ["muzi", "frodo", "apeach", "neo"]
r = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(i, r, k)