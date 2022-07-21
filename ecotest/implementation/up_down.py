"""
여행가 A는 N x N 크기의 정사각형 공간 위에 서있습니다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져있습니다.
가장 왼쪽 위 자표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다. 여행가 A는 상,하,좌,우 방향으로
이동할 수 있으며, 시작 좌표는 항상 (1,1) 입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여있습니다.

계획세에는 하나의 줄에 띄어싀기를 기준으로하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀있습니다
이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다. 예를 들어 (1,1) 위치에서
"""

"""
입력 조건 : 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
            둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다 (1 <= 이동 횟수 <= 100)
출력 조건: 첫째 줄에 여행가 A가 최적적으로 도착할 지점의 좌표(X, Y)를 공백을 기준으로 구분하여 출력합니다.
"""

"""
문제 해결 아이디어
"""

def sol(n,move : list):
    dir = {
        "L": (0,-1),
        "R": (0,+1),
        "U": (-1,0),
        "D": (+1,0)
    }

    curr = [1,1]
    for m in move:
        if (m == 'L' or m == 'R') and 1 < (curr[1] + dir[m][1]) <= n:
            curr[0] += dir[m][0]
            curr[1] += dir[m][1]
        elif (m == 'U' or m == 'D') and 1 < (curr[0] + dir[m][0]) <= n:
            curr[0] += dir[m][0]
            curr[1] += dir[m][1]
        else:
            continue
        print(curr)


    print(curr)


sol(5,['R','R','R','U','D','D'])


def sol2(n, plans):
    x, y = 1, 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    move_types = ['L','R','U','D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

    return x, y

