"""
역수열 구하기
2024-07-29
"""

input_data = [5, 3, 4, 0, 2, 1, 1, 0]


# 내 풀이
def solution(n_len: int, n_list: list):
    answer_list = [0 for i in range(n_len)]
    for i, reverse_number in enumerate(n_list):  # 역수열 리스트를 전체 순회
        count = 0
        for j, answer in enumerate(answer_list):
            if answer == 0 and count == reverse_number:  # 현재 인덱스의 값이 빈자리고 앞에 존재하는 수의 수가 일치할 때
                answer_list[j] = i + 1
                break
            elif answer == 0:
                count += 1
    return answer_list


# 강의 영상 풀이
def solution2(n, l):
    seq = [0] * n
    for i in range(n):  # i가 정렬된 자리를 처리하는 것
        for j in range(n):
            if l[i] == 0 and seq[j] == 0:  # l[i] == 0 이라는 것은 빈 공간을 확보 했다는 것
                seq[j] = i + 1
                break
            elif seq[j] == 0:
                l[i] -= 1
    for x in seq:
        print(x, end=' ')


if __name__ == '__main__':
    solution(len(input_data), input_data)
    solution2(len(input_data), input_data)
