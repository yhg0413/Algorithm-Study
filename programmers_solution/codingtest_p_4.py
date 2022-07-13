# 두개 뽑아서 더하기 난이도 1
# https://school.programmers.co.kr/learn/courses/30/lessons/68644

# 다른사람 풀이
def solution_outer(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

# 내풀이
from itertools import permutations

def solution(numbers):
    answer = []
    per_list = list(permutations(numbers, 2))
    for per in per_list:
        if per[0] + per[1] in answer:
            continue
        else:
            answer.append(per[0] + per[1])
    answer.sort()
    return answer