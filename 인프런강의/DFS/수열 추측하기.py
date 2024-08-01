"""
2024-08-01
가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 그리고 둘째 줄 부터 차례대로 파스칼의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다.
예를 들어 N이 4 이고 가장 윗 줄에 3 1 2 4가 있다고 했을 때, 다음과 같은 삼각형이 그려진다
3 1 2 4
 4 3 6
  7 9
   16
N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 잇는 숫자를 구하는 프로그램을 작성하시오.
단 답이 여러가지인 경우 사전순으로 가장 앞에 오는 것을 출력

입력
N = 가장 윗줄 까지의 수 1 <= N <= 10
F = 가장 밑에 잇는 줄의 수 1,000,000 이하

"""


# 내풀이
def DFS(l):
    if l > N:
        return
    if l == N:
        n = 0
        for i in range(0, N):
            if i == 0:
                n += p[i]
            elif i == N - 1:
                n += p[i]
            else:
                n += p[i] * (N - 1)
        if n == F:
            print(p)
        return
    else:
        for i in range(1, N + 1):
            if ch[i - 1] == 1:
                continue
            p[l] = i
            ch[i - 1] = 1
            DFS(l + 1)
            ch[i - 1] = 0


# 인강 풀이
def DFS2(L, sum):
    if L == N and sum == F:
        for x in p:
            print(x, end=' ')
    else:
        for i in range(1, N + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS2(L + 1, sum+(p[L] * b[L]))
                ch[i] = 0


if __name__ == '__main__':
    N = 4
    F = 16
    p = [0] * N
    ch = [0] * N
    b = [1] * N
    for i in range(1, N):
        b[i] = b[i-1] * (N-i) // i
    DFS(0)
    DFS2(0,0)
