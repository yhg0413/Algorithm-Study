"""
중복 순열 구하기에서 중복의 경우 제외
"""

def DFS(l):
    global cnt
    global result
    if l == m:
        print(result)
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            if ch[i] == 1:
                continue
            result[l] = i
            ch[i] = 1
            DFS(l + 1)
            ch[i] = 0
    pass

if __name__ == '__main__':
    cnt = 0
    m = 2
    n = 3
    result = [0] * m
    ch = [0] * (n + 1)
    DFS(0)
    print(cnt)