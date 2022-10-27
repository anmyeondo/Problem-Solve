def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    
    return True

def solution(n, k):
    answer = 0
    
    tmp = ''

    while 0 < n:
        r = n%k
        n = n//k
        tmp = str(r) + tmp

    nums = list(map(lambda x: int(x) if x != '' else 0, tmp.split('0')))
    
    for num in nums:
        if is_prime(num):
            answer += 1

    return answer