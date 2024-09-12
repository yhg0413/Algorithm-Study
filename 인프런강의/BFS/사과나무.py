from collections import deque

def solution(n,a):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    ch = [[0] * n for _ in range(n)]
    sum = 0
    dq = deque()
    ch[n//2][n//2] = 1
    sum += a[n//2][n//2]
    L = 0
    dq.append((n//2,n//2))
    while True:
        if L == n // 2:
            break
        size = len(dq)
        for i in range(size):
            tmp = dq.popleft()
            for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]
                if ch[x][y] == 0:
                    sum += a[x][y]
                    ch[x][y] = 1
                    dq.append((x,y))
        L += 1

    print(sum)

if __name__ == '__main__':
    a = [
        [1,2,3,4,5],
        [2,2,3,4,5],
        [3,2,3,4,5],
        [4,2,3,4,5],
        [5,2,3,4,5]
    ]
    solution(5,a)
