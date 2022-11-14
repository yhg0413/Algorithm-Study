"""
2022-11-14
다리를 지나는 트럭
문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length,
다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다.
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.
입출력 예
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
출처

※ 공지 - 2020년 4월 06일 테스트케이스가 추가되었습니다.

"""

# 내가 푼 답
from collections import deque

class Truck:
    def __init__(self, weight):
        self.b_count = 0
        self.weight = weight

    def get_b_count(self):
        return self.b_count

    def get_weight(self):
        return self.weight

    def move_bridge(self):
        self.b_count += 1

    def __str__(self):
        return [self.weight,self.b_count]

def solution(bridge_length, weight, truck_weights):
    waiting_trucks = deque([Truck(weight) for weight in truck_weights])
    bridge_on_trucks = deque()
    time = 0
    while waiting_trucks or bridge_on_trucks:
        time += 1
        if bridge_on_trucks:
            if bridge_on_trucks[0].get_b_count() >= bridge_length:
                bridge_on_trucks.popleft()
        if len(bridge_on_trucks) < bridge_length and waiting_trucks:
            if (sum([truck.get_weight() for truck in bridge_on_trucks]) + waiting_trucks[0].get_weight()) <= weight:
                bridge_on_trucks.append(waiting_trucks.popleft())
                print(sum([truck.get_weight() for truck in bridge_on_trucks]))

        for truck in list(bridge_on_trucks):
            if truck.get_b_count() < bridge_length:
                truck.move_bridge()

        print(time,[w.__str__() for w in waiting_trucks]," // " , [b.__str__() for b in bridge_on_trucks])
        if not bridge_on_trucks and not waiting_trucks:
            break

    print(time)


# 남이 푼 답

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution_other(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()
if __name__ == '__main__':
    solution(100,100,[10,10,10,10,10,10,10,10,10,10])
