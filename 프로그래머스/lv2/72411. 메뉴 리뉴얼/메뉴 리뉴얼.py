from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    cnts = [ Counter() for _ in range(len(course)) ]
    
    for i in range(len(course)):
        for order in orders:
            cm = combinations(order, course[i])
            tmp = Counter(list(map(''.join, map(sorted, cm))))
            cnts[i] += tmp
    
    for cnt in cnts:
        max_ = 0
        for c in cnt.most_common():
            if 1 < c[1] and max_ <= c[1]:
                max_ = c[1]
                answer.append(''.join(c[0]))
    return list(sorted(answer))