class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""
        ret = ""

        for wrd in strs:
            ret += str(len(wrd)) + '#' + wrd

        return ret

    def decode(self, s: str) -> List[str]:
        
        i = 0
        ret = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            wrd = s[j + 1: j + 1 + length]
            ret.append(wrd)

            i = j + 1 + length

        return ret



        
