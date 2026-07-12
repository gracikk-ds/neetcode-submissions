class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res, sol = [], []

        def backtrack(idx: int, remaining: int) -> None:
            if not remaining:
                res.append(sol.copy())
                return 

            if idx == n or remaining < 0:
                return

            # if we do NOT pick candidates[idx] → skip ALL its duplicates too
            # to avoid [2, 2, 4, 5] -> [[2, 4, 5], [2, 4, 5]]
            next_idx = idx + 1
            while next_idx < n and candidates[next_idx] == candidates[idx]:
                next_idx += 1                  # step 2
            backtrack(next_idx, remaining)

            # pick value
            sol.append(candidates[idx])
            backtrack(idx + 1, remaining - candidates[idx])
            sol.pop()

        backtrack(0, target)
        return res