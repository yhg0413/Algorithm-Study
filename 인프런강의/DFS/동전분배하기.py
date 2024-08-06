"""
N개의 동전을 A,B,C 에게 나누어 줄 예정
세명에게 동전을 적절히 나누어주어, 세명이 받은 각각의 총액을 계산해,
총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 분배하라.
단 세사람의 총액은 서로 달라야한다.

N = 동전의 개수
coins = 동전의 금액
"""


def DFS(l):
    global  total_sum
    if l == n:
        cha = max(k) - min(k) # 최고값에 최저값 차감
        if cha < total_sum:
            tmp = set() # 중복 제거
            for x in k:
                tmp.add(x)
            if len(tmp) == 3: # 제거된 중복이 있을 경우 개수가 달라짐.
                print(k)
                total_sum = cha
        return
    else:
        for i in range(len(k)):
            k[i] += coins[l]
            DFS(l+1)
            k[i] -= coins[l]


if __name__ == '__main__':
    n = 7
    k = [0] * 3
    total_sum = 20000000000000
    coins = [8,9,11,12,23,15,17]
    DFS(0)
    print(total_sum)
