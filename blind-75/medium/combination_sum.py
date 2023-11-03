'''
desc: find unique combos of candidates (duplicates ok) that sum to target

soln: recurse each i-th value, then recurse each i + 1th value after searching through ith combinations
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, curr, total):

            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i]) # testing all combos of ith value
            curr.pop()
            dfs(i + 1, curr, total) # recursing each i + 1th value

        
        dfs(0, [], 0)

        return res