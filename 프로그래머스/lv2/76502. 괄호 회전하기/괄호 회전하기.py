from collections import deque
def checker(s):
    stack = deque()
    
    for c in s:
        if c in ['[', '(', '{']:
            stack.append(c)
        else:
            if not stack:
                return 0

            if c == ')' and stack[-1] == '(':
                stack.pop()
                
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            
            else:
                return 0
    
    if not stack:
        return 1
    else:
        return 0
    
def solution(s):
    answer = 0
    tmp = ''.join(s)
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        answer += checker(tmp)
    
    return answer