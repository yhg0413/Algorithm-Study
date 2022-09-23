"""

문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
입출력 예
n	result
15	4
"""


def solution(n):
    answer = 1

    i = 1
    while i <= n // 2:
        temp = 0
        for j in range(i, n):
            temp += j
            if temp > n:
                break
            if temp == n:
                answer += 1
        i += 1

    return answer

def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])