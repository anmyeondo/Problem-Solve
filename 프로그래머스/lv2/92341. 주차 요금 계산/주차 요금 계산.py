import math
END_TIME = 1439

def solution(fees, records):
    answer = []
    dic = {}
    
    for record in records:
        time, num, state = record.split()
        
        if state == 'IN':
            h, m = time.split(':')
            time = int(h)*60 + int(m)
            
            if num in dic:
                dic[num]['time'] = time
                dic[num]['state'] = 'IN'
            else:
                dic[num] = {
                    'time': time,
                    'use': 0,
                    'state': ''
                }
        else:
            post_time = dic[num]['time']
            h, m = time.split(':')
            time = int(h)*60 + int(m)
            
            use = time - post_time
            dic[num]['use'] += use
            dic[num]['state'] = 'OUT'
    
    for k in sorted(dic.keys()):
        
        if dic[k]['state'] == 'OUT':
            if dic[k]['use'] <= fees[0]:
                fee = fees[1]
            else:
                fee = fees[1] + math.ceil((dic[k]['use'] - fees[0])/fees[2])*fees[3]
        else:
            dic[k]['use'] += END_TIME - dic[k]['time']
            if dic[k]['use'] <= fees[0]:
                fee = fees[1]
            else:
                fee = fees[1] + math.ceil((dic[k]['use'] - fees[0])/fees[2])*fees[3]
        
        answer.append(fee)
            
    return answer