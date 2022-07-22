"""
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
이때 이 수열에서 x가 등장하는 횟수를 계산하세요. 예를 들어 수열 {1,1,2,2,2,2,3}이 있을때 x =2 라면 현재 수열에서
2인 원소가 4개이므로 4를 출력합니다

단 이문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다.
"""

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index

array = [1,2,2,2,2,3]
x = 2

count = count_by_range(array,x,x)

if count == 0:
    print(-1)
else:
    print(count)