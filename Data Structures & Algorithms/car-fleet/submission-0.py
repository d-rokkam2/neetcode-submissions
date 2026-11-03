class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(pos, spe) for pos, spe in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        
        for pos, speed in pairs:
            stack.append((target - pos) / speed)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)

        