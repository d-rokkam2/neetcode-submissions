class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ret = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                pop_i, pop_t = stack.pop()
                ret[pop_i] = idx - pop_i

            stack.append((idx, temp))

        return ret







        