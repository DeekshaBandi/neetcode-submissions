class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare = ''
        for c in s:
            if c.isalnum():
                compare += c.lower()
        return compare == compare[::-1]