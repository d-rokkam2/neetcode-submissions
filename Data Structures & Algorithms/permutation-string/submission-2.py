from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        c1 = Counter(s1)
        need = len(c1)

        for i in range(len(s2)):
            matches = 0
            counter = {}
            for j in range(i, len(s2)):
                counter[s2[j]] = 1 + counter.get(s2[j], 0) 
                if c1.get(s2[j], 0) < counter[s2[j]]:
                    break
                if c1.get(s2[j], 0) == counter[s2[j]]:
                    matches += 1
                if matches == need:
                    return True

        return False
                

            

        










        

        