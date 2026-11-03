class Solution:
    def isValid(self, s: str) -> bool:

        hMap = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for char in s:

            if char in hMap:
                if stack and stack[-1] == hMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

        