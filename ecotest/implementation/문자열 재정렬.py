"""
알파벳 대문자와 숫자 (0 ~ 9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로
정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다.
"""


def sol(S : str):

    s_i = 0
    S = sorted(S)
    i = 0
    for s in S:
        if s >= '0' and s <= '9':
            i += 1
            s_i += int(s)
        else:
            break

    S = str(''.join(S[i::])) + str(s_i)

    return S

print(sol('K1KA5CB7'))

# 남의 코드

def sol2(S :str):
    result = []
    value = 0
    for x in S:
        if x.isalpha():
           result.append(x)
        else:
            value += int(x)

    result.sort()

    if value != 0:
        result.append(str(value))

    print(''.join(result))