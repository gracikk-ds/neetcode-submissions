class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer: int = 0
        right_pointer: int = len(numbers) - 1

        while left_pointer < right_pointer:
            result = numbers[left_pointer] + numbers[right_pointer]
            if result == target:
                return [left_pointer + 1, right_pointer + 1]
            if result < target:
                left_pointer += 1
            else:
                right_pointer -= 1
            
