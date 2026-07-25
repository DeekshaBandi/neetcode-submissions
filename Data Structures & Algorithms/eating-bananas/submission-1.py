class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            i = (left + right) // 2

            time = 0
            for p in piles:
                time += (p + i - 1) // i
            if time <= h:
                res = i
                right = i - 1
            else:
                left = i + 1
        return res