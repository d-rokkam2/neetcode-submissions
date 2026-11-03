class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        ret = []
        letter_map = {
            "2":'abc',
            "3":'def',
            "4":'ghi',
            "5":'jkl',
            "6":'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def backtrack(i, curr):

            if len(curr) == len(digits):
                ret.append(curr)
                return

            for char in letter_map[digits[i]]:
                backtrack(i + 1, curr + char)

        
        if digits:
            backtrack(0, "")

        return ret
        