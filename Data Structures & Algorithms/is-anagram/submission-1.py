class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        def make_dict(s: str):
            characters_dict = dict()
            for c in s:
                if (c not in characters_dict):
                    characters_dict[c] = 1
                else:
                    characters_dict[c] += 1
            return characters_dict

        s_dict = make_dict(s)
        t_dict = make_dict(t)
        
        for k, v in s_dict.items():
            if (k not in t_dict):
                return False
            if (t_dict[k] != v):
                return False
        return True