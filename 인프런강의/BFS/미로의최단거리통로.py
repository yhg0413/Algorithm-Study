from collections import deque




# 내풀이
def solution(n,m):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    cnt = 0
    dq = deque()
    dq.append((0,0))

    ch = [[0] * n for _ in range(7)]
    m[0][0] = 1

    while dq:
        size = len(dq)
        for i in range(size):
            tmp = dq.popleft()
            if tmp[0] == 6 and tmp[1] == 6:
                return cnt
            for j in range(4):
                x = dx[j] + tmp[0]
                y = dy[j] + tmp[1]
                if ((0 > x) or (6 < x)) or ((0 > y) or (6 < y)):
                    continue
                if m[x][y] == 0 and ch[x][y] == 0:
                    print(x, y)
                    ch[x][y] = 1
                    dq.append((x,y))
        cnt += 1

def solution2(n,m):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    dq.append((0,0))
    dis = [[0] * 7 for _ in range(7)]
    m[0][0] = 1
    while dq:
        tmp = dq.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x <=6 and 0 <= y<= 6 and m[x][y] == 0:
                m[x][y] = 1
                dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                dq.append((x,y))
    if dis[6][6] == 0:
        print(-1)
    else:
        print(dis[6][6])

if __name__ == '__main__':
    m = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 0]
    ]
    cnt = solution(7,m)
    print(cnt)
    pass