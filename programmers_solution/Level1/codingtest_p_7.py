# 없는 숫자 더하기
# 난이도 1
# https://school.programmers.co.kr/learn/courses/30/lessons/86051

# 다른사람 풀이
def solution(numbers):
    return 45 - sum(numbers)


# 내풀이
def solution(numbers):
    answer = 0
    for number in range(10):
        if number in numbers:
            continue
        else:
            answer += number
    return answer