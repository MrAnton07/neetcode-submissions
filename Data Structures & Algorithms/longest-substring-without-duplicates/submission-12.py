from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_max = 0
        if (len(s) == 0):
            return 0

        l, r = 0, 0
        c_d = dict()

        while ( r < len(s) ):           
            while ( r < len(s) ) and ( s[r] not in c_d ):
                c_d[s[r]] = 1
                r+=1

            c_d.pop(s[l])
            cur_max = max(cur_max, r-l)
            l+=1
        return cur_max
