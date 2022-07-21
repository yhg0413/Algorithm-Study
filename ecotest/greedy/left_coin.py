#<문제> 거스름 돈 : 시간 복잡도 분석


if __name__ == '__main__':

    n = 1260
    count = 0

    array = [500, 100, 50, 10]

    for coin in array:
        count += n // coin
        n %= coin

    print(count)


"""
화폐의 종류가 K라고 할 때, 소스코드의 시간복잡도는 O(K) 이다.

이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받는다.

"""