class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        out = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            out = max(out, r - left + 1)
        return out