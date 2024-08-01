"""
2024-07-29
숫자하나를 입력 받고, 해당 숫자의 자리수들 중 m개의 숫자를 제거하여
가장 큰수를 만드는 것. (단숫자의 순서는 유지)
ex n = 5276823 이고 m이 3이라면
7823이 가장 큰수
"""
from collections import deque


# 내 풀이
# 필요없는 앞에서 부터 빼는 동작 이용 스택 자료구조로 하는게 훨씬 효율적이였음
def solution(n: int, m: int):
    string_n = str(n)
    n_list = deque([])
    for s in string_n:
        tmp = s
        if not n_list:
            n_list.append(tmp)
        else:
            while m > 0 and len(n_list) >= 1:
                if n_list[0] < tmp and m > (len(n_list) - 1):
                    n_list.popleft()
                    m -= 1
                    continue
                if n_list[-1] < tmp:
                    n_list.pop()
                    m -= 1
                    continue
                break
            n_list.append(tmp)
    for i in range(m):
        n_list.pop()

    print(int(''.join(n_list)))


def solution2(n, m):
    stack = []
    for x in n:
        while stack and m > 0 and stack[-1] < x:
            stack.pop()
            m -= 1
        stack.append(x)
    if m != 0: # 슬라이싱으로 컷
        stack = stack[:-m]
    print(stack)

if __name__ == '__main__':
    solution(5276823, 3)
    solution(9977252641, 5)
