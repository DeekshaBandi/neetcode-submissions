class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        output = 0

        for num in nums:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length +=1 
                output = max(output, length)
        return output 