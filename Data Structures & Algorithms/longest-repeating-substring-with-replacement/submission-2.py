class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        out = 0
        seen = set(s)
        
        for c in seen:
            count = l = 0
            for i in range(len(s)):
                if s[i] == c:
                    count += 1

                while (i - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                out = max(out, i - l + 1)
        return out