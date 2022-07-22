#이진 탐색

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target,mid+1, end)


def binary_search_(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

# 파이썬 이진 탐색 라이브러리
"""
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오르쪽 인덱스를 반환
"""

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x)) # result = 2 -> 인덱스 번호
print(bisect_right(a,x)) # result = 4 -> 인덱스 번호

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

#값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))

