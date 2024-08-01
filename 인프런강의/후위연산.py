"""
2024-07-31
"""

def solution(n:str):
    stack = []
    for s in n:
        if s.isdecimal():
            stack.append(int(s))

        else:
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                if s == "+":
                    stack.append(b + a)
                elif s == "-":
                    stack.append(b - a)
                elif s == "/":
                    stack.append(b / a)
                elif s == "*":
                    stack.append(b * a)
    return stack[0]


if __name__ == '__main__':
    solution("352+*9-")