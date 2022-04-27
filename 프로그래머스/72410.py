#72410

import string


def solution(new_id):
    answer = new_id.lower()
    
    l = []
    for s in answer:
        if ('a' <= s <= 'z' or '0' <= s <= '9' or s == '-' or s == '_' or s =='.'):
            l.append(s)
    answer = ('').join(l)
    
    l.clear()
    prev = ''
    for i, v in enumerate(answer):
        if v == '.':
            if v != prev:
                l.append(v)
                
        else:
            l.append(v)
        prev = v

    if len(l) > 0:
        if l[0] == '.':
            del l[0]
            
    if len(l) > 0:
        if l[-1] == '.':
            del l[-1]        
    
    if len(l) == 0:
        l.append('a');

    answer = ('').join(l)
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
            
    if len(answer) <=2:
        s = answer[-1]
        while(len(answer)<3):
            answer += s
    print(answer)
    return answer

n = "...!@BaT#*..y.abcdefghijklm"
solution(n)