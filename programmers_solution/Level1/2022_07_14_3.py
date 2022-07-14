# [카카오 인턴] 키패드 누르기
# 난이도 1
# 통과
#남이 푼것
def solution_other(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

# 내가 푼 것
def solution(numbers, hand):
    answer = ''
    pos_L = [3,1]
    pos_R = [3,3]

    for number in numbers:
        div_num,mod_num  = divmod(number,3)
        if (mod_num % 3) == 1:
            pos_L = [div_num,mod_num]
            answer += 'L'
        elif (mod_num % 3) == 2 or number == 0:
            if number == 0:
                div_num = 3
                mod_num = 2
            sum_l = abs(pos_L[0] - div_num) + abs(pos_L[1] - mod_num)
            sum_r = abs(pos_R[0] - div_num) + abs(pos_R[1] - mod_num)
            print(sum_l,sum_r)
            if sum_l > sum_r:
                pos_R = [div_num, mod_num]
                answer += 'R'
            elif sum_r > sum_l:
                pos_L = [div_num, mod_num]
                answer += 'L'
            else:
                if hand == 'right':
                    pos_R = [div_num, mod_num]
                    answer += 'R'
                else:
                    pos_L = [div_num, mod_num]
                    answer += 'L'
        else:
            pos_R = [div_num-1,3]
            answer += 'R'
        print(number,pos_L, pos_R,answer)


    return answer

if __name__ == '__main__':
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))