from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        start = 0
        window_sum = 0
        for end in range(len(nums)):

            window_sum += nums[end]

            while window_sum >= target:
                min_len = min(min_len, end - start + 1)
                window_sum -= nums[start]
                start += 1

        return 0 if min_len == float("inf") else min_len