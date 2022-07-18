# 약수의 개수와 덧셈
# 난이도 1



#다른사람 코드
# 제곱의 약수는 홀수개
def solution_other(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


# 나의 코드

def solution(left, right):
    answer = 0

    for n in range(left,right+1):
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        answer += (-n) if count % 2 == 1 else n
    return answer

if __name__ == '__main__':
    solution(13,17)