def binary(s):
    zero = 0
    one = 0
    
    for bit in s:
        if bit == '0':
            zero += 1
        else:
            one += 1
    
    return [zero, bin(one)[2:]]

def solution(s):
    answer = [0, 0]
    
    while s != "1":
        zero, s = binary(s)
        answer[0] += 1
        answer[1] += zero
        
    return answer