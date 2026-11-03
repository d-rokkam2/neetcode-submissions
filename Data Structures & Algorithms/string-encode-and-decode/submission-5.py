class Solution:

    def encode(self, strs: List[str]) -> str:
         
        res = ""
        ret = []
        for word in strs:
            curr = str(len(word)) + '#' + word 
            ret.append(curr)

        return res.join(ret)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            string = s[j + 1: j + 1 + length]
            res.append(string)

            i = j + length + 1

        return res



            