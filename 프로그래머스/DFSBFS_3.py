


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [False]*(len(words))

    answer = bfs(begin, target, words, visited)

    return answer

def bfs(begin, target, words, visited):
    






b = "hit"
t = "cog"
words = ["hot", "dot", "dog", "lot", "log"]

print(solution(b, t, words))