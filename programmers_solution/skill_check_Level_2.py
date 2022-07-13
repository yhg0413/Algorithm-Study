from itertools import permutations

## 첫번째 도전
def solution_Q1(s):
    str_list = s.split(" ")
    int_list = list()
    for st in str_list:
        int_list.append(int(st))
    answer = f'{min(int_list)} {max(int_list)}'
    return answer


# def permutations(iterable, r=None):
#     # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
#     # permutations(range(3)) --> 012 021 102 120 201 210
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))
#     cycles = list(range(n, n-r, -1))
#     yield tuple(pool[i] for i in indices[:r])
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i+1:] + indices[i:i+1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return

def solution_Q2(number, k):
    str_list = list(number)
    answer = []
    cases = 0

    sort_list = list(map(''.join,permutations(number, k)))

    min_index = min(sort_list)
    max_index = max(sort_list)
    print(int(min_index),int(max_index))


    return answer


## 두번쨰 도전

#https://school.programmers.co.kr/learn/courses/30/lessons/70129/solution_groups?language=python3
def sol2_outer(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

def sol2(s):
    c_a = s.count('0')
    x = s.replace('0', '')
    i = 0
    while 1:
        i+=1
        c = len(x)
        bin_s = str(bin(int(c))).replace('0b', '')
        if bin_s == '1':
            answer = [i,c_a]
            return answer
        else:
            c_a += bin_s.count('0')
            x = bin_s.replace('0', '')

if __name__ == '__main__':
    pass



