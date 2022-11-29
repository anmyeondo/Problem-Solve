def f(x):
    if x%2 == 0:
        return x+1
    
    x = bin(x)[:1:-1] + '0'
    for i in range(len(x)):
        if x[i] == '0':
            x = x[:i-1] + '01' + x[i+1:]
            break
    return int(x[::-1], 2)

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(f(n))
    return answer
