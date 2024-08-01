from collections import deque

def solution(n:int,k:int):
    cnt = 0
    tmp = [i+1 for i in range(n)]
    people = deque(tmp)

    while len(people) > 1:
        cnt += 1
        print(people)
        if cnt == k:
            cnt = 0
            people.popleft()
        else:
            p = people.popleft()
            people.append(p)
    print(people)

if __name__ == '__main__':
    solution(8,3)