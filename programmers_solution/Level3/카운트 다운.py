"""
https://school.programmers.co.kr/learn/courses/30/lessons/131129?language=python3#
"""

"""
해당 문제를 풀 경우 다이나믹 프로그래밍으로 풀어야하는데 근야 조건문으로만 작성하려다가 실패헀다
답을 보고 해석 해보자
"""

# https://school.programmers.co.kr/questions/38683 우석우 님
import sys
limit_number = 300000
sys.setrecursionlimit(limit_number)
"""
파이썬 재귀함수의 경우 기본 재귀 함수의 깊이 제한이 1000으로 얕기때문에
해당 깊이 제한을 300000으로 늘려 풀 수 있게 만든다.
"""

sequence=[1,18,4,13,6,10,15,2,17,3,19,7,16,8,11,14,9,12,5,50,20]
"""
해당 문제에서의 싱글, 불의 경우을 sqquence에 저장
"""
cache={}
"""
재귀함수를 돌면서 경우의 수 별 target 별 던진횟수, 싱글 + 불 횟수
"""
def solution(target):

    def dp(n):
        if n==0:
            return (0,0) #횟수, 합
        if n in cache:
            # 이미 확인한 숫자의 경우 캐시에서 찾아서 반환
            return cache[n]
        arr=[]
        #싱글,불
        # 모든 경우의 수를 맞췄을 때(맞출 수 있는 경우)를 재귀적으로 확인
        for i in sequence:
            if i==50:
                if n-50>=0:
                    temp = dp(n-50)
                    arr.append((temp[0]+1,temp[1]+1))
            else:
                if n-i>=0:
                    temp = dp(n-i)
                    arr.append((temp[0]+1,temp[1]+1))
                if n-i*2>=0:
                    temp = dp(n-i*2)
                    arr.append((temp[0]+1,temp[1]))
                if n-i*3>=0:
                    temp = dp(n-i*3)
                    arr.append((temp[0]+1,temp[1]))

        arr.sort(key=lambda x:(x[0],-x[1]))
        # arr(list) 안의 tuple 값중 0번 인덱스는 낮은순 1번 인덱슨는 높은순으로 정렬
        cache[n]=arr[0]
        # 가장 0번 인덱스가 작고 1번 인덱스가 낮은 경우의 수를 cache에 저장 및 반환
        return cache[n]

    ans = dp(target)
    answer = [ans[0],ans[1]]
    return answer

"""
DFS BFS - 다이나믹 프로그래밍 관련 문제 및 알고리즘을 좀 더 공부하자.. 해당 알고리즘을 사용해야한다고는 생각했는데
머리속에서 그려지지가 않는다. 좀 더 풀어보기
"""