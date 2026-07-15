class Solution(object):
    def sortedSquares(self, nums):
        result = []

        left, right = 0, len(nums) - 1

        while left <= right:
            if pow(nums[left], 2) > pow(nums[right], 2):
                result.append(pow(nums[left], 2))
                left += 1
            else:
                result.append(pow(nums[right], 2))
                right -= 1
        return result[::-1]