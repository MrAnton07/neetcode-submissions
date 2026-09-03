from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums_set = set(nums)
        nums_dict = dict()
        tmp = 0
        for num in nums_set:
            i = 0
            if (num-1 in nums_set):
                continue
            while True:
                if (num+i in nums_set):
                    i+=1
                else:
                    tmp = max(tmp, i)
                    break
        return tmp