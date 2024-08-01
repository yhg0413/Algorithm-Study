"""
다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환해주려면 어떻게 줘야하나는가

각 단위의 동전은 무한정 쓸 수 있다.

입력
N : 동전의 종류 개수 1 <= N <= 12
k : 동전의 종류
M : 거슬러줘야할 금액 1 <= M <= 500
"""



# 내풀이
def DFS(l, cnt, r_sum): # l이나 cnt나 같은 변수였다. 굳이 선언할 필요없는 cnt였다
    global result
    if cnt > result: #cnt 즉 거슬러 준 동저의 개수가 이전에 가능한 동전의 개수보다 큰 경우 탈출
        return
    else:
        if r_sum == m: # 동전의 합이 거슬러 줄 돈과 같고
            if cnt < result: # 동전의 개수가 더 적다면 result 갱신 and문으로 하는 것보다 케이스 단축
                result = cnt
            return
        elif r_sum > m:
            return
        else:
            cnt += 1
            for i in range(n):
                DFS(l + 1, cnt, r_sum + k[i])

# 강의 풀이
def DFS2(L, sum):
    global res
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS2(L+1, sum+k[i])


if __name__ == '__main__':
    result = 10000000
    res = 21400000000
    # n = 3
    # k = [1, 2, 5]
    # m = 15

    n = 5
    k = [1, 5, 7,11,15]
    m = 39
    DFS(0, 0, 0)
    print(result)
