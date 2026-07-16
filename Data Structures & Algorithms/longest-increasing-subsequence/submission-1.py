class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}  # key: (i, prev) -> best length from here

        def dfs(i, prev):  # prev = index of last picked element, -1 if none
            if i == n:
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            # skip nums[i]
            best = dfs(i + 1, prev)

            # pick nums[i], if valid
            if prev == -1 or nums[i] > nums[prev]:
                best = max(best, 1 + dfs(i + 1, i))

            memo[(i, prev)] = best
            return best

        return dfs(0, -1)