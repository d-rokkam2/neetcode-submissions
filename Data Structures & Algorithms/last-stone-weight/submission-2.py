import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            curr = first - second

            if curr:
                heapq.heappush(stones, -curr)

        return -stones[-1] if stones else 0