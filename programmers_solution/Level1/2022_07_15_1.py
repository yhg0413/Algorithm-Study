# 난이도 1
#  2019 카카오 블라인드 채용 실패율


# https://school.programmers.co.kr/learn/courses/30/lessons/42889
#다른사람 풀이
def solution_other(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

#내풀이

def solution(N, stages):
    answer = []
    person_count = len(stages)
    for n in range(N):
        if stages.count(n+1) > 0:
            print(n + 1, person_count)
            answer.append([(n+1),stages.count(n+1)/person_count])
            person_count -= stages.count(n+1)
        else:
            answer.append([n+1,0])
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [i[0] for i in answer]
    return answer

if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))