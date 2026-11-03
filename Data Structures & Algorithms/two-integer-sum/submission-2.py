class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for key, idx in enumerate(nums):

            complement = target - idx

            if complement in hashMap:

                return [hashMap[complement], key ]

            hashMap[idx] = key

        