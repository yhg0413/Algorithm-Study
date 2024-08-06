"""
현금 출납기에 K가지의 동전이 각각 n1,n2,... nk개 씩 들어있다고 할 때
T원을 동전으로 바꿔줄 수 있는 방법의 가지수를 출력하시오
"""



# 내풀이
def DFS(n,local_t):
    global cnt
    if cnt_tmp[n] > coins[n][1]:
        return
    if local_t >= t:
        if local_t == t:
            cnt += 1
        return
    else:
        for i in range(n,k):
            cnt_tmp[i] += 1
            DFS(i,local_t+coins[i][0])
            cnt_tmp[i] -= 1

def DFS2(l, sum):
    global cnt
    if sum > t:
        return
    if l == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(cn[l] + 1): # 반복문 횟수를 처음부터 동전의 개수만큼으로 처리하여 나의 풀이처럼 카운팅하는 로직 제거
            DFS(l+1, sum+(cv[l]*i))


if __name__ == '__main__':
    t = 20
    k = 3
    cnt = 0
    coins = [[5,3], [10,2], [1,5]]
    cnt_tmp = [0] * k
    DFS(0,0)

    cv = [5,10,1]
    cn = [3,2,5]


