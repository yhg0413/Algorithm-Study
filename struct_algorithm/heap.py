class MaxHeap:
    def __init__(self):
        self.data = [None]

    def get_data(self):
        return self.data

    def insert(self, item):
        self.data.append(item)
        l = len(self.data) - 1
        p = l // 2
        while self.data[p] is not None:
            print(l, p)
            if self.data[p] < self.data[l]:
                self.data[p], self.data[l] = self.data[l], self.data[p]
                l = p
                p = p // 2
            else:
                break

    def remove(self):
        """
        원소의 개수가 n인 최대 힙에서 최대 원소 삭제
        -> 자식 노드들과의 대소 비교 최대 회수 : 2 X log_2n
        최악 복잡도 O(logn)의 삭제 연산

        :return:
        """
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.max_heapify(1)
        else:
            data = None
        return data

    def max_heapify(self, i):
        smallest = i
        left = i * 2
        right = (i * 2) + 1
        if (len(self.data) - 1 // 2) >= left and self.data[left] > self.data[smallest]:
            smallest = left
        if (len(self.data) - 1 // 2) >= right and self.data[right] > self.data[smallest]:
            smallest = right
        print(smallest)
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.max_heapify(smallest)
            # 현재 노듸 (i)와 최댓값 노드 (smallest)의 값 바꾸기
            # 재귀적으로 maxHeapify 호출


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(2)
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(6)
    max_heap.insert(1)
    print(max_heap.get_data())
    max_heap.remove()
    print(max_heap.get_data())
    max_heap.remove()
    print(max_heap.get_data())
    max_heap.remove()
    print(max_heap.get_data())
