from itertools import permutations

def solution(k, dungeons):
    answer = -1
    dungeons = permutations(dungeons, len(dungeons))
    
    for dungeon in dungeons:
        energy = k
        tmp = 0
        for require, use in dungeon:
            if require <= energy:
                energy -= use
                tmp += 1
            else:
                break
        answer = max(answer, tmp)
    
    
    return answer