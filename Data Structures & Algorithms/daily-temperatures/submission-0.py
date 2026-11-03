class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = []

        for i in range(n):
            diff = 0
            for j in range(i, n):
                if temperatures[i] < temperatures[j]:
                    diff = j - i
                    break

            result.append(diff)
        
        return result