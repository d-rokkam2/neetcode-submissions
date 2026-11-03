class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        n = len(s)

        def is_palindrome(string, l, r):
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start, curr):

            if start >= n:
                res.append(curr.copy())
                return

            for end in range(start, n):
                if is_palindrome(s, start, end):
                    curr.append(s[start: end + 1])
                    backtrack(end + 1, curr)
                    curr.pop()


        backtrack(0, [])
        return res

        