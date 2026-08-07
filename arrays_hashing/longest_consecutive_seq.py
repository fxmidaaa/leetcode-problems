class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1

                max_streak = max(max_streak, curr_streak)

        return max_streak

