def solution(cards):
    answer = 0
    
    visited = [False for _ in range(len(cards))]
    groups = []
    
    for i in range(len(cards)):
        if visited[i]:
            continue
        
        j = i
        group = 0
        while not visited[j]:
            visited[j] = True
            group += 1

            j = cards[j]-1
        groups.append(group)
        
    groups.sort()
    
    if len(groups) <= 1:
        answer = 0
    else:
        answer = groups[-1] * groups[-2]
        
    return answer