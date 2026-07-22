class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        start = 0
        max_length = 0

        for end in range(len(s)):
            if s[end] in char_dict:
                start = max(char_dict[s[end]] + 1, start)
            
            char_dict[s[end]] = end

            max_length = max(max_length, end - start + 1)
        
        return max_length
