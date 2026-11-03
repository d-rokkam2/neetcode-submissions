class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1

        # sorting hashmap
        newMap = sorted(hashMap.items(), key = lambda item:item[1], reverse = True)[:k]

        return [number[0] for number in newMap]

        