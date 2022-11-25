from collections import deque

def dfs(start, edges, n):
    visited = [False for _ in range(n+1)]
    s = deque()
    s.append(start)
    
    n = 0
    while s:
        v = s.pop()
        visited[v] = True
        n += 1
        
        for edge in edges[v]:
            if not visited[edge]:
                s.append(edge)
        
    return n

def solution(n, wires):
    answer = float('inf')
    
    e = [set() for _ in range(n+1)]
    
    for v1, v2 in wires:
        e[v1].add(v2)
        e[v2].add(v1)
    
    for v1, v2 in wires:
        e[v1].remove(v2)
        e[v2].remove(v1)
        
        answer = min(answer, abs(dfs(v1, e, n)-dfs(v2, e, n)))
        
        e[v1].add(v2)
        e[v2].add(v1)
        
    return answer