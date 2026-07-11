class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        final = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        final = [1] + digits
        return final
