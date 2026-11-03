class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_string = [i.lower() for i in s if i.isalnum()]

        return filtered_string == filtered_string[::-1]
        