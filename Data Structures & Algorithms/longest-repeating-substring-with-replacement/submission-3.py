class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        out = 0
        for i in range(len(s)):
            count = {}
            freq = 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                freq = max(freq, count[s[j]])
                
                if (j - i + 1) - freq <= k:
                    out = max(out, j - i + 1)
        return out