"""
최소힙 구현
"""
from collections import deque
import heapq as hq

# 강의 답안,
def solution(n_list:list,):
    hep = []
    for n in n_list:
        if n == -1:
            break
        if n == 0:
            if len(hep) == 0:
                print(-1)
            else:
                print(hq.heappop(hep))
        else:
            hq.heappush(hep, n)




