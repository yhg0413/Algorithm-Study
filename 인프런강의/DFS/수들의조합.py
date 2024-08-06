"""
2024-08-05
N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수는 몇개가 있는지 출력하는 프로그램을 작성하시오
예들 들어 5개의 숫자 2 4 5 8 12가 주어지고 , 3개를 뽑은 조합의 합이 6의 배수인 조합을 찾으면
4+8+12 2+4+12로 2가지가 있다.
"""



# 내풀이
def DFS(l,s,local_sum):
    global m
    global cnt
    if l == k:
        if local_sum % 6 == 0:
            cnt += 1
        return
    else:
        for i in range(s,n):
            if ch[i] == 1:
                return
            ch[i] = 1
            DFS(l+1, s+1,local_sum + m[i])
            ch[i] = 0


# 인강 풀이 중복제거가 따로 필요없었다.
def DFS2(l,s,local_sum):
    global m
    global cnt
    if l == k:
        if local_sum % 6 == 0:
            cnt += 1
        return
    else:
        for i in range(s,n):
            DFS(l+1, i+1,local_sum + m[i])

if __name__ == '__main__':
    n = 5
    k = 3
    m = [2, 4, 5, 8, 12]
    ch = [0] * n
    cnt = 0
    DFS(0,0,0)
    print(cnt)