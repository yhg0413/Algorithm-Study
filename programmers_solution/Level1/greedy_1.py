# 큰 수 만들기
# 난이도 1
# 그리디

## 다른 사람 해석
def solution(number, k):
    answer = [number[0]]

    for num in number[1:]:
        while answer and answer[-1] < num and k > 0:
            # 누적된 값의 마지막 값보다 현재 숫자가 큰지 비교
            # 현재 숫자가 더 크고 뺄 횟수가 남은경우 pop(끝에서부터 제거)
            answer.pop()
            k -= 1
        answer.append(num)

    if k > 0  :# 횟수가 남은경우 횟수만큼 뒤에서부터 제거
        answer = answer[:-k]

    return "".join(answer)  # 리스트를 문자열로 반환