class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            output[i] = product 
        return output 
