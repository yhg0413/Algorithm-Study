# 가장 큰 수
# Level2
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


def solution(numbers):
    for i,number in enumerate(numbers):
        numbers[i] = str(number)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))



"""
문제 미해결로 다른 사람 코드 뜯어보기

numbers = list(map(str, numbers))
-> numbers 원소들은 현재 int형 모드 str 형으로 변경하여 리스트에 집어 넣는다

numbers.sort(key = lambda x: x*3, reverse=True)
list.sort()와 sorted()는 모두 비교하기 전에 각 리스트 요소에 대해 호출할 함수를 지정하는 key 매개 변수를 가지고 있습니다.

x * 3 -> 문자열에 3을 곱해주면 해당문자열을 3개 나열하는 것과 같으니

'333', '303030', '343434', '555', '999'를 key로 넣어주면.
정렬을 하면 303030 -> 333 -> 343434 -> 555 -> 999가 됨

reverse=True로 해서 거꾸로 정렬된 결과가 리턴.

numbers = ['9', '5', '34', '3', '30']

return str(int(''.join(numbers)))

python에서 join 함수는 배열을 특정 문자로 구분하여 문자열로 변환해주는 함수이다.

근데 왜 string을 int로 변환하고 다시 string으로 변환해서 리턴하는지 이해가 안됐는데

그렇게 join만 사용하면 0일 때가 문제다.

[0,0,0,0] 을 input으로 넣는다면 '0000'이 리턴되므로 int로 변환해서 '0'으로 바꿔야 한다.

그리고 오버플로우 방지를 위해 다시 str으로 변환해야 하는 것!!!!

"""