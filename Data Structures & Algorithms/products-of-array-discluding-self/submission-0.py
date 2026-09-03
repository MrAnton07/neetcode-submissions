class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def make_prefix(nums: List[int]) -> List[int]:
            #Делает префиксный массив по умножению с паддингом 1 1 в начале и конце
            pref = [1]
            for num in nums:
                pref.append(num*pref[-1])
            pref.append(1)
            return pref

        nums_l = make_prefix(nums)
        nums_r = make_prefix(nums[::-1])[::-1]

        out = []
        for i in range(1, len(nums_l)-1):
            out.append(nums_l[i-1] * nums_r[i+1])
        return out
