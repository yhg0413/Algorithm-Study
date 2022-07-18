
## 어떤 경우 안되는지 테스트케이스 생각중

def solution(n, lost, reserve):
    answer = 0

    for num in range(1,n+1):
        if num in lost:
            for r in reserve:
                if ((num - 1) <= r) and (r <= (num + 1)):
                    reserve.remove(r)
                    lost.remove(num)
                    answer += 1
                    break
        else:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(5,[2, 4],[3]))