
#size () - 현재 큐에 들어 있는 데이터의 원소의 수를 구함
#isEmpty() - 현재 큐가 비어 잇는지를 판단
#enqueue(x) - 데이터 원소 x를 큐에 추가
#dequeue() - 큐의 맨 앞에 저장된 데이터 우너소를 제거 또는 반환
#peek() - 큐의 맨 앞에 저장된 덷이터 원소를 반환

class ArrayQueue:
    # 빈 큐를 초기화
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.data)

    def enqueue(self,item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]