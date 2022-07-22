from collections import deque

# 미로 탈출

"""
동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리 괴물이 있어 이를 피해 탈춣해야한다.
동빈이의 위치는 (1,1) 이며 미로의 출구는 (N, M)의 위치에 존재하고 한번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분을 0으로 없는 부분을 1로 표시할고 미로는 반드시 탈출 할 수있는 형태로 제시된다
이때 동빈이가 탈출하기 위해서 움직여야 하는 최소 칸의 개수를 구하시오 칸을 셀때는 시작칸과 ㅁ마지막칸을 포함한다
"""

n, m = 5, 6

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    print(graph)
    return graph[n - 1][m - 1]


print(bfs(0, 0))
