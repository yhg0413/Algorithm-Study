

if __name__ == '__main__':
    # n = int(input())
    # li = []
    # for i in range(n):
    #     li.append(list(map(int, input().split())))
    #
    # for i in range(n):
    #     answer = li[i][0] + li[i][1]
    #     print(f"Case #{i + 1}: {answer}")

    """
    n = int(input())

    li = []
    
    for i in range(n):
        li.append(list(map(int,input().split())))
    백준 2차원 배열 입력받기
    """
    A, I = map(int, input().split())

    answer = (A * I) - (A + 1)

    print(answer)