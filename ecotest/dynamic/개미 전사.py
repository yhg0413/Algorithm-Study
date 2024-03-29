"""
개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 합니다.
메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있습니다.

각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 에정입니다.
이때 메뚜기 정창별들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있습니다.

따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진
식량창고를 약탕해야 합니다.

예를 들어 식량창고 4개가 존재한다고 가정하자
[1,3,1,5]
-> 이때 개미 전사는 두번째 식량창고와 네 번째 식량창고를 선택했을 때 최댓값인 총 8개의 식량을
빼앗을 수 있습니다. 개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 원합니다.

개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하세요
"""

"""
입력 조건 : 식량창고의 개수 N (3 <= N <= 100)
            둘째 줄에 공백을 기준으로 각 식량창고에 저장된 식량의 개수 K (0 <= K <= 1,000) 
"""
"""
문제 해설
ai = i번째 식량창고까지의 최적의 해 (얻을 수 있는 식량의 최댓값)
ki = i번째 식량창고에 있는 식량의 양
점화식은 다음 과 같다
max(a(i-1), a(i-2) + Ri)

한 칸 이상 떨어진 식량 창고는 항상 털 수 있으므로(i - 3)번째 이하는 고려할 필요가 없습니다
"""

k = [1,3,1,5]

n = len(k)
d = [0] * (n + 1)
d[1] = 1
d[2] = 3


for i in range(2, n):
    print(i)
    d[i] = max(d[i-1],d[i-2] + k[i])

print(d[n-1])


d = [0] * 100
d[0] = k[0]
d[1] = max(k[0],k[1])

for i in range(2, n-1):
    d[i] = max(d[i -1], d[i - 2] + k[i])

print(d[n-1])
