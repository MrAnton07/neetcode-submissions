from collections import deque
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bag_of_nums = dict()
        for num in nums:
            if (num in bag_of_nums): 
                bag_of_nums[num] -= 1 
            else:
                bag_of_nums[num] = -1

        flag = 0
        heap = [(v, key) for key, v in bag_of_nums.items()]
        heapq.heapify(heap)
        out = []
        # print(heap)
        for i in range(k, 0, -1):
            # print(heap[i])
            _, num = heapq.heappop(heap)
            out.append(num)
        return out  