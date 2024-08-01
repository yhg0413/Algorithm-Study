"""
재귀함수를 이용한 이진수 출력

10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용해서 출력할 것.
"""


# 강의 풀이
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x % 2, end='')




# 내풀이 , 필요 없는 조건들이 포함 된것으로 확인됐다. 더 최적화할 수 있도록 생각해보자
def solution(n: int):
    global result
    div_n = n // 2
    if div_n > 0:
        if n % 2 == 1:
            result = "1" + result
            solution(div_n)
        else:
            result = "0" + result
            solution(div_n)
    elif n == 1:
        result = "1" + result
    else:
        return


if __name__ == '__main__':
    result = ""
    solution(11)
    print(result)
    DFS(11)
