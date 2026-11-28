class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0 

        longest = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1

            last[ch] = right
            longest = max(longest, right - left + 1)

        return longest