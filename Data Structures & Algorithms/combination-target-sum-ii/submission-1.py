class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, curr, total):
            if total == target:
                ret.append(curr.copy())
                return

            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                if total + candidates[idx] > target:
                    break
                
                curr.append(candidates[idx])
                backtrack(idx + 1, curr, total + candidates[idx])
                curr.pop()
                
        backtrack(0, [], 0)
        return ret