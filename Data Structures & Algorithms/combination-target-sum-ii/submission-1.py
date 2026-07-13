class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res, sol = [], []

        def backtrack(idx: int, remaining: int) -> None:
            if remaining == 0:
                res.append(sol[:])
                return

            if idx >= n or remaining < 0:
                return

            # do not choose the element 
            # [1, 2, 2, 3] -> [[1, 2, 3], [1, 3, 2]]
            next_idx = idx + 1
            while next_idx < n and candidates[idx] == candidates[next_idx]:
                next_idx += 1
            backtrack(next_idx, remaining)

            # choose the element
            sol.append(candidates[idx])
            backtrack(idx + 1, remaining - candidates[idx])
            sol.pop()

        backtrack(0, target)
        return res