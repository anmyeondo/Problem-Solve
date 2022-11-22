def get_divisor(n):
    result = [n]
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            result.append(i)
            result.append(n//i)
    
    return result

def solution(arrayA, arrayB):
    answer = 0
    
    candidate = []
    min_A = min(arrayA)
    min_B = min(arrayB)
    
    candidate = list(sorted(get_divisor(min_A) + get_divisor(min_B), reverse=True))
    print(candidate)
    for c in candidate:
        flag_a = 1
        flag_b = 1
        
        for i in range(len(arrayA)):
            if not(arrayA[i]%c == 0 and arrayB[i]%c != 0):
                flag_a = 0
                break
        
        for i in range(len(arrayA)):
            if not(arrayB[i]%c == 0 and arrayA[i]%c != 0):
                flag_b = 0
                break
        
        if flag_a or flag_b:
            answer = c
            break

    return answer