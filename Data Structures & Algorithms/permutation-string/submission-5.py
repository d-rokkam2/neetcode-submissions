class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        l = 0
        matches = {}
        
        for r in range(len(s2)):
            c = s2[r]
            matches[c] = matches.get(c, 0) + 1
            if (r - l + 1) > len(s1):
                leaving = s2[l]
                matches[leaving] -= 1
                if matches[leaving] == 0:
                    del matches[leaving]

                l += 1

            if matches == s1Count:
                return True


        return False






            

        