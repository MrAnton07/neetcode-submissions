class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = []
        for s in strs:
            l = len(s)
            encode_str+= f"{l}#{s}"
        encode_str = "".join(encode_str)
        print(encode_str)
        return encode_str

    def decode(self, s: str) -> List[str]:
        out = []
        if len(s) == 0:
            return out
        num = s[0]
        i = 0
        while i < len(s):
            j = s.find("#", i)
            shift = int(s[i:j])
            out.append(s[j+1:j+shift+1])
            i = j+shift+1
            # print(s[i])
            
        return out               
