class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                currTemp, currIndex = stack.pop()
                result[currIndex] = i - currIndex

            stack.append([temperatures[i], i])

        return result

        