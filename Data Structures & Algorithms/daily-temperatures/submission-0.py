class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            found = False
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    result.append(j - i)
                    found = True
                    break
            if not found:
                result.append(0)
        return result
        

