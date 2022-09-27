
"""
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	return
118372	873211
"""

# 내풀이
# sort 사용 안하고 풀기/
def solution(n):
    int_list = []
    answer = 0
    while n:
        int_list.append(n%10)
        if len(int_list) >= 2:
            for i in range(len(int_list)-1,0,-1):
                if int_list[i-1] < int_list[i]:
                    temp = int_list[i]
                    int_list[i] = int_list[i-1]
                    int_list[i-1] = temp
                else:
                    break
        n = n//10
    for i,int_ in enumerate(int_list):
        answer += int_ * (10**(len(int_list)-(i+1)))

    return answer


# 남의 풀이
def solution2(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))