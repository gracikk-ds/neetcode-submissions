class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(nlogn)
        n = len(nums)
        sol, res = [], []

        def backtrack(idx: int) -> None:
            if idx == n:
                res.append(sol[:])
                return

            # we can skip the number
            next_idx = idx + 1
            while next_idx < n and nums[next_idx] == nums[idx]:
                next_idx += 1
            backtrack(next_idx)

            sol.append(nums[idx])
            backtrack(idx + 1)
            sol.pop()

        backtrack(0)
        return res
        
