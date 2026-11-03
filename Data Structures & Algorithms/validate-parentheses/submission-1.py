class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hashMap = {'}':'{', ')':'(', ']':'['}

        for char in s:
            if char in hashMap:
                if stack and hashMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) 

        return True if len(stack) == 0 else False



        
        