# 1이 될 때까지:
"""
-어떠한 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

- 예를 들어 N이 17, K가 4라고 가정하자. 이때 1번의 과정을 수행하면 N은 16이 되고 이후에
2번 과정을 두번 수행하면 N은 1이된다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다.
이는 N을 1로 만드는 최소 횟수이다.

- N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성하세요

입력 조건 : 첫째 줄에 N(1 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백을 기준으로 하여 각각 자연수로 주어진다.

출력 조건 : 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력한다.
"""

"""
문제 해결 아이디어
- 주어진 N에 대하여 최대한 많이 나누기를 수행하면 된다.
- N의 값을 줄일 때 2이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 많이 줄이기 때문.

정당선 분석
- 가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수있는가?
 -> N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있다.
 -> 다시 말해 K가 2 이상이면 K로 나누는것이 1로 빼는것보다 항상 빠르게 줄일 수 있다
  -> 또한 N은 항상 1에 도달한다.(최적의 해 성립)
"""


## 나의 풀이
n = 100
k = 5

def sol(n, k):
    count = 0
    while n != 1:
        if n % k == 0:
            n = n // k
        else:
            n -= 1
        count += 1
        print(n)

    print(count)
sol(n, k)
## 남의 풀이

def sol2(n,k):
    result = 0
    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
        target = (n // k) * k
        result += (n - target) # 1일 빼는 횟수를 한번에 계산 반복문 도는 횟수를 줄임
        n = target
        # N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        # K로 나누기
        result += 1
        n //= k
    result += (n-1)
    print(result)

sol2(n,k)