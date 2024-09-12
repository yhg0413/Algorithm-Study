"""
2024-08-12

일직선상 A와 B의 거리가 주어 질 때 A가 움직일 수 있는 경우를 -1, +1, +5의 경우로 움직일 수 있다고 가정하고
A가 B까지 도착할 때의 A가 움직인 회수를 구하는 문제

n = A의 좌표
m = B의 좌표

"""


from collections import deque


def solution(n,m):
    MAX = 10000
    ch = [0] * (MAX + 1)
    dis = [0] * (MAX + 1)
    ch[n] = 1
    dis[n] = 0
    dQ = deque()
    dQ.append(n)
    while dQ:
        now = dQ.popleft()
        if now == m:
            break
        for next in (now - 1, now + 1, now + 5):
            if 0 < next <= MAX:
                if ch[next] == 0:
                    dQ.append(next)
                    ch[next] = 1
                    dis[next] = dis[now] + 1
    print(dis[m])

if __name__ == '__main__':

    n, m = 5, 14
    solution(n,m)
    pass
