#난이도 1 로또 최대 최소 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484
## 다른 사람 코드
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# 내코드

def solution_me(lottos, win_nums):
    result = 0
    cases = 0
    win = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1,
    }

    for lotto in lottos:
        if lotto in win_nums:
            result += 1
        elif lotto == 0:
            cases += 1
    answer = [win[result + cases], win[result]]

    return answer