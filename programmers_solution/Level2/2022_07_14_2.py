# 카카오 개발자 겨울 인턴십 튜플
# 난이도 2
# 문제 이해 실패. 해결 진행 중.


if __name__ == '__main__':
    test = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    start = 0

    temp = ""
    temp_list = []
    answer = list()
    for test in test[1:-1]:
        if test == '{':
            start = 1
            continue
        elif test == '}':
            start = 0
            for i,temp_li in enumerate(temp_list):
                C = temp.split() if len(temp.split()) >= len(temp_li) else temp_li
                D = temp_li if len(temp.split()) >= len(temp_li) else temp.split()
                print('C:',C , "D:",D)
                m_s = list(set(D) - set(C))
                print('m_s', m_s)
                if m_s == []:
                    temp_list[i] = temp_li
                else:
                    continue
            temp_list.append(temp.split(','))
            temp = ""
            continue
        if start == 1:
            temp += test


    print(temp_list)


