#LinkedList 구현하기. 테스트

class Node:
    def __init__(self, item):
        self.data = item
        self.next =None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos): # 특정 순서 원소 뽑기
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self): #전체 내용 뽑기
        answer = []
        if self.nodeCount == 0:
            return []

        curr = self.head
        answer.append(curr.data)

        while curr.next:
            curr = curr.next
            answer.append(curr.data)

        # 다른 사람 풀이
        # l = []
        # node = self.head
        # while node != None:
        #     l.append(node.data)
        #     node = node.next
        # return l


        return answer
