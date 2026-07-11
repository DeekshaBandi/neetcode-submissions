class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.squares(n)
            if n == 1:
                return True
        return False

    def squares(self, n: int) -> int:
        out = 0

        while n:
            num = n%10
            num = num ** 2
            out += num
            n = n // 10
        return out 