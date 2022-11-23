from collections import deque

def solution(order):
    answer = 0

    q = deque([i for i in range(1, max(order)+1)])
    s = deque()
    
    for n in order:
        # print(n,q,s)
        
        while (q and q[0] != n):
            if s and s[-1] == n:
                break

            s.append(q.popleft())
                
        if q and q[0] == n:
            answer += 1
            q.popleft()

        elif s and s[-1] == n:
            answer += 1
            s.pop()
        else:
            break
            
    return answer
