from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        curr_sum = 0

        for num in nums:
            curr_sum += num

        return expected_sum - curr_sum