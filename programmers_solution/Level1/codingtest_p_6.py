# 같은 숫자는 싫어
# 난이도 1
# https://school.programmers.co.kr/learn/courses/30/lessons/12906


# 다른사람 코드
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 내코드
def solution(arr):
    answer = []
    for i,arr in enumerate(arr):
        if i == 0:
            answer.append(arr)
        else:
            if answer[-1] != arr:
                answer.append(arr)
    return answer