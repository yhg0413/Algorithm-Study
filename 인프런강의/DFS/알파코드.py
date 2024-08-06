"""
2024-08-06
"""


def DFS(l, p):
    global cnt
    if l == n:
        cnt += 1
        for j in range(p):
            print(chr(64+res[j]), end='')
        print()
    else:
        for i in range(1, 27):
            if code[l] == i:
                res[p] = i
                DFS(l + 1, p + 1)
            elif i >= 10 and code[l] == i // 10 and code[l + 1] == i % 10:
                res[p] = i
                DFS(l + 2, p + 1)


if __name__ == '__main__':
    code = [2, 5, 1, 1, 4]
    n = len(code)
    code.insert(n,-1)

    res = [0] * (n + 3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
