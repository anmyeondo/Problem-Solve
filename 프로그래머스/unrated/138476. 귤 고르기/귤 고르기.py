from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    
    for _, v in sorted(c.items(), key=lambda item: -item[1]):
        if k <= v:
            answer += 1
            break
        else:
            answer += 1
            k -= v
    return answer