# 음료수 얼려 먹기

"""
N X M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 잇는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때 얼름 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
"""

"""
입력 조건 : 첫 번째 줄에 얼음 틀의 세로 길이 N 과 가로 길이 M이 주어집니다. (1 <= N,M <= 1,000)
            두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어집니다.
            이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
            
출력 조건 : 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.
"""


def sol(N,M, iced_list):
    direction = [[0,1,],[0,-1],[1,0],[-1,0]]

    iced = [[False] * N] * M
    pos = [0,0]
    for i in N:
        for j in M:
            if iced_list[i][j] == 1:
                break
            if not iced[i][j]:
                while True:
                    for dir in direction:
                        p_x = i + dir[0]
                        p_y = j + dir[1]
                        if (p_x < 0 or p_x >= N) or (p_y < 0 or p_y >= M):
                            continue
                        elif iced_list[i][j] == 0:
                            iced[i][j] = True



n, m = 4,5

graph = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,0,0,0]]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y -1)
        dfs(x + 1, y)
        dfs(x , y + 1)
        return True
    return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)






