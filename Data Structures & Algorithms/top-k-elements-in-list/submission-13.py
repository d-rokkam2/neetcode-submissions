from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for elem in nums:
            freq[elem] += 1

        ret = sorted(freq.items(), key = lambda item:item[1], reverse = True)[:k]

        return [i[0] for i in ret]

        