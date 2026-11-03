class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        count = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
                count += 1
            elif char == ')' and count > 0:
                stack.append(char)
                count -= 1
            elif char != ')':
                stack.append(char)
            continue

        res = []
        for c in reversed(stack):
            if c == '(' and count > 0:
                count -= 1
                continue
            res.append(c)

        return "".join(res[::-1])

            
                

        