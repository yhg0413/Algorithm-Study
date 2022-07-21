#직사각형 별찍기
#난이도 1


a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*", end="")
    print("")

##################
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)