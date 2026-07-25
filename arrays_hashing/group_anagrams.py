from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            sign = tuple(count)

            if sign not in groups:
                groups[sign] = []

            groups[sign].append(word)

        return list(groups.values())