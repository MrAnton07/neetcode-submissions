class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_nums_vals = dict()
        for num in nums:
            if (num not in in_nums_vals):
                in_nums_vals[num] = 1
            else:
                return True
        return False
