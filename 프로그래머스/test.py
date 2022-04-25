def solution(seoul):
    for s in seoul:
        if "Kim" in s:
            return "김서방은 " + str(seoul.index(s)) + "에 있다"

solution(["Jane", "Kim"])