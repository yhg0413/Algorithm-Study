"""
n x m 크기의 금광이 있습니다. 금광은 1x1 크기의 칸으로 나누어져 있으며,
각 칸은 특정한 크기의 금이 들어 있습니다.

채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다.
맨 청음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
이후에 m - 1번에 걸쳐서 매번 오른쪽위 오른쪽 오른쪽 아래 3가지중 하나의 위치로
이동해야합니다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램
"""
"""
array[i][j] = 1행 j열에 존재하는 금의 양
dp[i][j] = i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
점화식은 다음 과 같다.

dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j-1], dp[i+1][j-1])

이때 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크해야한다.

편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 된다
    - 바로 DP 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍에 적용할 수 있다.
"""

### 틀림 모든 경우에서 가장 큰수를 찾아버림..
 
def sol(n, m, li):
    d = [0] * (m)

    d[0] = 0
    test = []
    for i in range(n):
        test.append(li[i][0])
    d[0] = max(test)

    print(d[0])
    for i in range(1, m):
        d[i] = d[i - 1]
        for j in range(n):
            if j - 1 >= 0:
                d[i] = max(d[i], li[j - 1][i] + d[i - 1])
            if j + 1 <= n - 1:
                d[i] = max(d[i], li[j + 1][i] + d[i - 1])
            d[i] = max(d[i], li[j][i] + d[i - 1])
        print(d[i])

    print(d[m - 1])


def sol2(n, m, li):
    dp = li
    index = 0

    for j in range(1, m):
        for i in range(n):
            print(j,i)
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)


if __name__ == '__main__':
    # li = [
    #     [1, 3, 3, 2],
    #     [2, 1, 4, 1],
    #     [0, 6, 4, 7]
    # ]
    li = [
        [1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]
    ]
    # sol(4,4,li)
    sol2(4, 4, li)
