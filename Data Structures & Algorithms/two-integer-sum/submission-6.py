class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for idx, num in enumerate(nums):
            array.append([num, idx])


        array.sort(key=lambda x: x[0])  # time: O(nlogn) space: O(1)

        idx_start = 0
        idx_end = len(array) - 1

        while idx_start < idx_end:
            current_sum = array[idx_start][0] + array[idx_end][0]
            if current_sum == target:
                return [
                    min(array[idx_start][1], array[idx_end][1]),
                    max(array[idx_start][1], array[idx_end][1]),
                    ]
            
            if current_sum > target:
                idx_end -= 1
                continue
            
            if current_sum < target:
                idx_start += 1
                continue
        return []



                    
