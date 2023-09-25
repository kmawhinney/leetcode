class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                # Add new candidate to comb
                comb.append(candidates[i])
                # With new comb, check all new possibilities
                backtrack(remain - candidates[i], comb, i)
                # Go back after checking all possibilities
                comb.pop()
            
        backtrack(target, [], 0)

        return result
