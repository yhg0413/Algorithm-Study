# 곱하기 혹은 더하기
"""
- 각 자리가 숫자(0부터 9)로만 이러우진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요
단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽부터 순서대로 이러주진다고 가정합니다.

- 예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는((((0 + 2) * 9) * 8) * 4) = 576 입니다.
또한 만들어질 수 잇는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.
"""

"""
문제 조건

입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1<= S의 길이 <= 20)
출력 조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

문제 해결 아이디어
- 대부분의 경우 '+'보다는 'x'가 더 값을 크게 만든다
 -> 예를 들어 5+6 = 11 이고 5x6 = 30이다.
 다만 다 수중에서 하나라도 0 혹은 1인 경우, 곱하기보다 더하기를 수행하는 것이 효율적이다.
 따라서 두 수에 대하여 연사을 수행할 때, 두 수 중 하나라도 1 이하인 경우에는 더하며 두 수가 2 이상인 경우에는 곱한다.

"""

def sol(numbers):
    result = int(numbers[0])
    for number in numbers[1::]:
        if int(number) <= 1:
            result += int(number)
        else:
            result *= int(number)
    print(result)

sol('2345')


## 남의 코드
def sol2(data):
    result = int(data[0])
    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)