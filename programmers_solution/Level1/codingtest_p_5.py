# 카카오 채용연계형 인턴십 숫자 문자열과 영단어
# 난이도 1
#https://school.programmers.co.kr/learn/courses/30/lessons/81301


# 다른사람 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution_outer(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)



####################

def solution(s):
    number_s = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, number in enumerate(number_s):
        if number in s:
            s = s.replace(number, f'{i}')

    answer = int(s)
    return answer


if __name__ == '__main__':
    solution("one4seveneight")