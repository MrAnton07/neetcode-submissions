class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # k* (Разбить строку на буквы - O(n) + отсортировать эти буквы O(n) + сделать dict из соответствий "если слово имеет hash p - то dict[p].append(s))
        def counting_sort(s):
                counts = [0]*26 #26 букв
                thr = ord('a')
                for c in s:
                    counts[ord(c) - thr] += 1
                
                chars = []
                for i in range(26):
                    chars += ( chr(thr + i) * counts[i] )
                return "".join(chars)

        strs_d = dict()

        for s in strs:
            h_s = counting_sort(s)
            if h_s in strs_d:
                strs_d[h_s].append(s)
            else:
                strs_d[h_s] = [s]
        
        out = []
        for k, v in strs_d.items():
            out.append(v)
        return out            
            
            
                    