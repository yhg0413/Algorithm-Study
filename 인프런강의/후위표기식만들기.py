"""
2024-07-31
"""

def solution(n:str):
    answer:list = []
    stack = []
    operator = {
        "-":0,
        "+":0,
        "*":1,
        "/":1,
        "(":2,
        ")":2
    }
    for s in n:
        if s.isnumeric():
            answer.append(int(s))
        else:
            if stack:
                while stack:
                    if operator[stack[-1]] == "(" and s != ")":
                        stack.append(s)
                        break
                    elif s == ")":
                        while stack:
                            if operator[stack[-1]] == "(":
                                stack.pop()
                                break
                            answer.append(stack.pop())
                    if operator[stack[-1]] >= operator[s]:
                        if operator[stack[-1]] != "(":
                            answer.append(stack.pop())
                        else:
                            stack.pop()

                    else:
                        stack.append(s)
                        break
            else:
                stack.append(s)

    print(answer)

def solution2(n:str):
    stack = []
    res = ''
    for x in n:
        if x.isdecimal():
            res += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()
    print(res)

if __name__ == '__main__':
    solution("3+5*2/(7-2)")
    solution2("3+5*2/(7-2)")