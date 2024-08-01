"""
아나그램이란 두 문자열이 알파벳의 나열 순서는 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 한다.

두 문자열을 입력사항으로 줄 때 아나그램일 경우 YES 아닐경우 NO를 출력하는 코드를 작성하시오.

2024-07-31
"""

# 내풀이 , Python 자체의 내장함수 사용법에 대해 학습해야할 필요성을 느낄 수 있었다.
def solution(a_word ,b_word) -> str:
    if len(a_word) != len(b_word):
        return "NO"

    a_dict = {}
    b_dict = {}

    for a ,b in zip(a_word ,b_word):
        print(a ,b)
        if a_dict.get(a):
            a_dict[a] += 1
        else:
            a_dict[a] = 1
        if b_dict.get(b):
            b_dict[b] += 1
        else:
            b_dict[b] = 1
    for key in a_dict.keys():
        if a_dict.get(key) != b_dict.get(key):
            return "NO"
    return "YES"

#강의 풀이
def solution2(a, b):
    str1 = dict()
    str2 = dict()
    for x in a:
        str1[x] = str1.get(x,0)+1
    for x in b:
        str2[x] = str2.get(x,0)+1

    for key in str1.keys():
        if key in str2.keys(): # 이 부분이 굳이 작성해야하는 코드인지 의문
            if str1[key] != str2[key]:
                print("NO")
                break
        else:
            print("NO")
            break
        # if str1.get(key) != str2.get(key): 대체 가능한 부분이지 않나
        #     return "NO"
    else:
        print("YES")

# 강의의 리팩토링 코드
def solution3(a,b):
    str_h = dict()
    for x in a:
        str_h[x] = str_h.get(x, 0) + 1
    for x in b:
        str_h[x] = str_h.get(x, 0) - 1

    for x in a:
        if str_h.get(x) > 0:
            print("NO")
            break
    else:
        print("YES")

# 강의의 리팩토링 코드 리스트 해시 버전
def solution4(a:str,b:str):
    str1 = [0] * 52
    str2 = [0] * 52
    for x in a:
        if x.isupper():
            str1[ord(x) - 65] += 1
        else:
            str1[ord(x) - 71] += 1
    for x in b:
        if x.isupper():
            str2[ord(x) - 65] += 1
        else:
            str2[ord(x) - 71] += 1
    for i in range(52):
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    print(solution("AbaAeCe" ,"baeeACA"))
    solution2("AbaAeCe" ,"baeeACA")
