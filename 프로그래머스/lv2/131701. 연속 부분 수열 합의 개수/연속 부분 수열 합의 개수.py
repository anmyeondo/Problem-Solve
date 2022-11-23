def solution(elements):
    answer = set(elements)
    elements = elements + elements
    for term in range(2, (len(elements)//2)+1):
        for i in range(len(elements)):
            answer.add(sum(elements[i:(term+i)]))
    return len(answer)