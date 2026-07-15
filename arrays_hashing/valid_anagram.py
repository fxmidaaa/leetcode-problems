class Solution:
    def isAnagram(self, s, t):

        char_counter = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            char_counter[s[i]] = char_counter.get(s[i], 0) + 1
            char_counter[t[i]] = char_counter.get(t[i], 0) - 1

        for count in char_counter.values():
            if count != 0:
                return False

        return True