def solution(begin, target, words):
    if target not in words:
        return 0
    global minanswer

    words.insert(0, begin)
    minanswer = len(words)
    return min(DFS(begin, target, words, 0))

def comp(a, b):
    answer = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
    if answer == 1: return True
    else: return False


minanswer = 0

def DFS(begin, target, words, depth):

    answer = []
    global minanswer
    if minanswer < depth:
        return []

    if begin == target and minanswer > depth:
        minanswer = depth
        #print("found" + str(depth))
        return [depth]

    else:
        for compare_word in words:
            if comp(compare_word, begin) == 1:
                answer.extend(DFS(compare_word, target, words, depth+1))

        #print(answer)
        return answer



b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]



solution(b, t, w)