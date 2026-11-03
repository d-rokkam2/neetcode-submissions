class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = []
        for word in strs:
            curr = str(len(word)) + '#' + word
            res.append(curr)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []

        while i < len(s):

            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            string = s[j + 1: j + length + 1]
            res.append(string)

            i = j + length + 1

        return res


            

        

