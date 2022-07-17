#완전탐색 최소 직사각형
#난이도 1
#https://school.programmers.co.kr/learn/courses/30/lessons/86491


#남의 코드
solution_other2 = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)

def solution_other(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

#내코드
def solution(sizes):
    test = []
    for i in sizes:
        test.append([i[1],i[0]] if i[0] < i[1] else [i[0],i[1]])

    width = max([i[0] for i in test])
    height = max([i[1] for i in test])

    print(width,height)

    return width*height


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))