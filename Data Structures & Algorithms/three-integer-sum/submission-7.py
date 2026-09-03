class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = list()
        for t in range(len(nums)):
            l, r = 0, len(nums)-1
            while (r > l):
                if l == t:
                    l+=1
                if r == t:
                    r-=1
                if ( (nums[l]+nums[r]) > -1*nums[t] ):
                    r-=1
                elif ( (nums[l]+nums[r]) < -1*nums[t] ):
                    l+=1
                else:
                    if (r <= l):
                        break
                    vvv = [nums[l], nums[r], nums[t]]
                    vvv.sort()
                    if (vvv not in out):
                        out.append(vvv)
                        print(l, r, t)
                    l+=1
                    r-=1

        return out