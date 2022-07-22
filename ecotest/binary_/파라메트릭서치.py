# 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
# -> 최적화 문제란 어떠한 함수의 값을 최대한 높이거나 최대한 낮추는 문제
# 일반적인 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용해 해결할 수 있다

# 떡볶이 떡 만들기
"""
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다.
오늘은 떡볶이 떡을 만드는 날입니다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이의 떡의 길이가
일정하지 않습니다. 대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춥니다.

절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단합니다. 높이가 H보다 긴 떡 H위의 부분이 잘릴 것이고
낮은 떡은 잘리지 않습니다

예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는
15, 14,10,15,cm가 될 것 입니다. 잘인 떡의 길이는 차례대로 4,0,0,2cm입니다 손님은 6cm만큼의 길이를 가져갑니다

손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 잇는 높이의 최댓값을 구하는
프로그램을 작성하세요
"""

def cut_dduck(dduck,m):
    dduck.sort(reverse = True)

    answer = 0
    h = dduck[0]

    for i in range(h,0,-1):
        cut_l = 0
        for dd in dduck:
            if dd > i:
                cut_l += dd - i
        if cut_l >= m:
            print(cut_l)
            answer = i
            break
    print(answer)

def sol2(n,m,du_list):
    start = 0
    end = max(du_list)

    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in du_list:
            if x > mid:
                total += x - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

if __name__ == '__main__':
    cut_dduck([19,14,10,17],6)
