class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashMap = set()

        for number in nums:
            if number in hashMap:
                return True
            else:
                hashMap.add(number)

        return False

        