from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def CHEEEEECK(s, k):
            l, r = 0, 0
            char_d = defaultdict(int)
            char_d[s[0]] = 0
            pivot_c = s[0]
            cur_max = 1
            if len(s) == 1:
                return 1

            while r < len(s):

                if ((sum(char_d.values()) - char_d[pivot_c] <= k)):
                    char_d[s[r]] += 1
                    r += 1
                else:
                    char_d[s[l]] -= 1
                    l += 1
                if (sum(char_d.values()) - char_d[pivot_c] > k):
                    cur_max = max(cur_max, sum(char_d.values())-1 )
                else:
                    cur_max = max(cur_max, sum(char_d.values()))
                pivot_c = max(char_d, key=char_d.get) # 'A' or 'B' or 'C' or ...

                    
            return cur_max
        a = CHEEEEECK(s, k)
        s = s[::-1]
        b = CHEEEEECK(s, k)
        return max(a, b)