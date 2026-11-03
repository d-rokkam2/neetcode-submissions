from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

        frequencies = sorted(counter.items(), key = lambda item:item[1], reverse = True)[:k]


        return [number[0] for number in frequencies]


        