array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #i부터 출발 1까지 1씩 감소
        if array[j] < array[j -1]: # 한칸씩 왼쪽으로 이동
            array[j], array[j -1] = array [j - 1], array[j]
        else: #자기보다 작은 데이터를 만나면 그자리에서 스톱
            break

print(array)