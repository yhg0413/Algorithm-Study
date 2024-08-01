"""
1부터 N까지의 번호가 적힌 구술이 있다. 이 중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하시오


"""



# 중복 처리되는 부분이 있어서 제거하는 로직이 있으면 좋을 것 같다.
def DFS(l,s):
    global res
    global cnt
    if l == m:
        cnt += 1
        print(res)
        return
    else:
        for i in range(s, n + 1):
            res[l] = i
            DFS(l+1,i+1)


if __name__ == '__main__':
    n = 10
    m = 5
    ch = [0] * n
    res = [0] * m
    cnt = 0
    DFS(0,1)
    print(cnt)