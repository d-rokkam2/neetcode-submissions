from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        c1 = Counter(s1)
        c2 = Counter()

        left = 0
        

        for right, letter in enumerate(s2):
            c2[letter] += 1
            if right - left + 1 > len(s1):
                
                leaving = s2[left]
                c2[leaving] -= 1
                if c2[leaving] == 0:
                    del c2[leaving]

                left += 1
            if c1 == c2:
                return True


        return False



            

        










        

        