"""
2024-07-31
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태울수가 없다.
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.

입력 사항
C = 최대 제한 무게
N = 강아지 마리 수
W = 강아지 무게

출력 제한 사한
첫번 째 줄에 가장 무거운 무게를 출력
"""


def DFS(L, sum, max_sum):
    """
    :param L: 현재 차수
    :param sum: 현재 차수까지 왔을 때의 부분 집합의 합
    :param max_sum: 현재 차수까지의 최대 집합의 합
    :return:
    """
    global result
    if sum + (total - max_sum) < result: # 만약 현재 차수까지의 합과 총 무게 - 최대 집합의 합이 현재 기록된 최대값보다 작다면 return
        return
    if sum > c: # 최대 가능한 무게값을 초과한 경우 return
        return
    if L == n and sum > result: # 최대 무게값을 초과하지 않고 기록한 경우들 중 가장 큰경우 result 갱신
        result = sum
    else:
        DFS(L + 1, sum + w[L], max_sum + w[L]) # 현재 값 포함 다음 차수 진행
        DFS(L + 1, sum, max_sum + w[L]) # 현재 값 제외 다음 차수 진행


if __name__ == '__main__':
    c = 259
    n = 5
    w = [81, 58, 42, 33, 61]
    result = -2147000000
    total = sum(w)
    DFS(0, 0, 0)
    print(result)
