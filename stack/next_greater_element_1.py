from typing import List

class Solution(object):
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        stack = []
        next_greater = {}

        for current in nums2:
            while stack and current > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = current

            stack.append(current)

        while stack:
            number = stack.pop()
            next_greater[number] = -1

        return [next_greater[number] for number in nums1]