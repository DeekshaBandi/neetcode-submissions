class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        
        left = 0
        right = len(height) - 1
        
        leftvalue = height[left]
        rightvalue = height[right]

        result = 0        
        
        while left < right:
            if leftvalue < rightvalue:
                left += 1 
                leftvalue = max(leftvalue, height[left])
                result += leftvalue - height[left]
            else: 
                right -= 1
                rightvalue = max(rightvalue, height[right])
                result += rightvalue - height[right]
        return result 

        
