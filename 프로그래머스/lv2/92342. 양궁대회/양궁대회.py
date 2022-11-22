from collections import deque

def solution(n, info):
    answer = []
    board = [0 for _ in range(11)]
    idx = 0
    max_diff = -1

    q = deque()
    q.append([idx, board])

    while q:
        idx, board  = q.popleft()
        # index 벗어난 경우
        if 10 < idx or n < sum(board):
            continue
        
        # N 발을 다 쏜 경우
        if n == sum(board):
            apeach, ryan = 0, 0
            diff_score = 0
            # 값 비교
            for i in range(11):
                if 0 < (info[i] + board[i]):
                    if info[i] < board[i]:
                        diff_score += (10 - i)
                    else:
                        diff_score -= (10 - i)
            
            if 0 < diff_score:
                if max_diff < diff_score:
                    answer = [board]
                    max_diff = diff_score
                elif max_diff == diff_score:
                    answer.append(board)
                else:
                    continue

        else:
            # 안 쏜거
            q.append([idx+1, board])

            # 쏜거
            tmp1 = [i for i in board]
            tmp2 = [i for i in board]

            left = n-sum(board)

            # 남은거 끝에 쏜거
            tmp1[-1] = left
            q.append([idx+1, tmp1])

            # apeach 보다 잘 쏜거
            tmp2[idx] = info[idx]+1
            q.append([idx+1, tmp2])
    
    if answer:
        return answer[-1]
    else:
        return [-1]