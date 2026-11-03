class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = []

        def backtrack(openN, closeN, curr):

            if openN == closeN == n:
                ret.append("".join(curr))

            if openN < n:
                curr.append('(')
                backtrack(openN + 1, closeN, curr)
                curr.pop()

            if closeN < openN:
                curr.append(')')
                backtrack(openN, closeN + 1, curr)
                curr.pop()

        backtrack(0, 0, [])
        return ret


        