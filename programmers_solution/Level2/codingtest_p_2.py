# 기능 개발 난이도 2
# https://school.programmers.co.kr/learn/courses/30/lessons/42586\

###### 내풀이
def solution(progresses, speeds):
    answer = []
    pro_list = list()

    for pro in progresses:
        pro_list.append([pro,False])

    while 1:
        count = 0
        for i, pro in enumerate(pro_list):
            if pro[0] >= 100 and pro[1] is False:
                if i == 0 or pro_list[i-1][1] == True:
                    pro[1] = True
                    count += 1
            else:
                pro_list[i][0] += speeds[i]
        if count != 0:
            answer.append(count)
        if sum(answer) == len(progresses):
            break
    return answer


### 다른사람 풀이
def solution_other(progresses, speeds):
    """
    소스 해석 : -((p-100)//s) 이 구간은 (p-100)//s로 진행할경우 숫자가 버림이 발생되어 정확한
    값을 구하기 힘들어짐 -((p-100)//s)사용하여 -를 나누게되면 음수에서의 버림은 절댓값이 커지기 때문에
    다시한번 -를 하여 값을 구하였음
    ex )  3//4   -> 1
        -(-3//4) -> 2
    """
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

if __name__ == '__main__':
    # progresses = [95, 90, 99, 99, 80, 99]
    # speeds = [1, 1, 1, 1, 1, 1]
    # print(solution(progresses,speeds))

    print(-4//3)