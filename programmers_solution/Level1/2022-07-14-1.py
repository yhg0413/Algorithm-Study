# 음양 더하기 난이도 1

# 다른사람 풀이
def solution_other(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))


# 내풀이
def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute

    return answer