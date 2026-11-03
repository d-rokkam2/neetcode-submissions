from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = defaultdict(int)

        for n in nums:
            hmap[n] += 1

        freq = sorted(hmap.items(), key = lambda 
        item:item[1], reverse = True)[:k]

        return [number[0] for number in freq]


        