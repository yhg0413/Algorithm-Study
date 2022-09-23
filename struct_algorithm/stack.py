from double_linked_lists import Node
from double_linked_lists import DoublyLinkedList


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data


"""
중위 표기법을 따르는 수식 S 가 인자로 주어질 때, 이 수식을 후위 표기법을 따르는 수식으로 변환하여 반환하는 함수 solution() 을 완성하세요.
"""
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for s in S:
        pre = prec.get(s)
        if pre:
            if opStack.isEmpty() or s == '(':
                opStack.push(s)
            else:
                peek = opStack.peek()
                if (peek == '(') or (prec[peek] < pre):
                    opStack.push(s)
                else:
                    while not opStack.isEmpty() and (prec.get(opStack.peek()) >= pre):
                        answer += opStack.pop()
                    opStack.push(s)
        else:
            if s == ')':
                while 1:
                    temp = opStack.pop()
                    if temp == '(':
                        break
                    answer += temp
            else:
                answer += s
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer

def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while 1:
                temp = opStack.pop()
                if temp == '(':
                    break
                postfixList.append(temp)
        else:
            while not opStack.isEmpty() and prec.get(opStack.peek()) >= prec.get(token):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        elif token == '*':
            a = valStack.pop()
            b = valStack.pop()
            valStack.push(b * a)
        elif token == '/':
            a = valStack.pop()
            b = valStack.pop()
            valStack.push(b / a)
        elif token == '+':
            a = valStack.pop()
            b = valStack.pop()
            valStack.push(b + a)
        elif token == '-':
            a = valStack.pop()
            b = valStack.pop()
            valStack.push(b - a)
        print(valStack.peek())

    return valStack.pop()

def sol(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val



##### 스택의 응용 후위 표기 수식 계산