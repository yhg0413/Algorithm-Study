"""
2024-07-29
"""
# 내풀이
def solution(n: str):
    stack = []
    last = ""
    answer = 0
    for s in n:
        if s == "(":
            stack.append(s)
        elif s == ")":
            stack.pop()
            if last == "(":
                print(stack)
                print(len(stack))
                answer += len(stack)
            else:
                answer += 1
        last = s
    print(answer)
    return answer

# 강의 풀이 코드 동일

if __name__ == '__main__':
    solution("()(((()())(())()))(())")
