from collections import Counter

def solution(want, number, discount):
    answer = 0
    goal = {}
    
    # 가격 매칭
    for i in range(len(want)):
        goal[want[i]] = number[i]
    
    for i in range(len(discount)):
        product = Counter(discount[i:min(i+10, len(discount))])
        flag = 1
        for key in goal.keys():
            if (key not in product) or (product[key] < goal[key]):
                flag = 0
                break
        
        if flag:
            answer += 1
            
    return answer