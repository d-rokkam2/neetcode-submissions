class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:

            if char in "+-*/":
                a, b = int(stack.pop()), int(stack.pop())
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(b - a)
                elif char == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(char))

        return stack[0]
                


        