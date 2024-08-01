"""
1부터 N까지 번호가 적힌 구슬이 있고. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력하시오

입력설명
N : 최대 번호 3 <= N <= 10
M : 뽑을 횟수 2 <= M <= N

출력설명
모든 경우의 수 출력
마지막 총 경우의 수 출력
"""


def dfs(l):
    global cnt
    global result
    if l == m:
        print(result)
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            result[l] = i
            dfs(l + 1)


if __name__ == '__main__':
    m = 2
    n = 3
    cnt = 0
    result = [0] * m
    res = []
    dfs(0)
    print(res)
    print(cnt)

