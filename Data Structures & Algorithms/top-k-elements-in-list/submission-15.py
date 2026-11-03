class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        for val in nums:
            counter[val] = counter.get(val, 0) + 1

        srted = sorted(counter.items(), key = lambda item : item[1])[-k:]

        return [i[0] for i in srted]

       


        