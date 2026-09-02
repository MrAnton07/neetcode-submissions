class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        def make_hasharr(nums: List[int]):
            i = 0
            hasharr = dict()
            for num in nums:
                if num not in hasharr:
                    hasharr[num] = [i]
                else:
                    hasharr[num].append(i)
                i+=1
            return hasharr

        hasharr = make_hasharr(nums)
        for i in range(len(nums)):
            needed_val = target - nums[i]
            if (needed_val in hasharr):
                for k in hasharr[needed_val]:
                    if k != i:
                        return [min(i, k), max(i, k)]
        