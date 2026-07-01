# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        #height od the left and right subtree
        lh = self.maxHeight(root.left)
        rh = self.maxHeight(root.right)
        diameter = lh + rh

        #also calculate the dumater of the left adn right subtree and get the max value of both 
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max (self.maxHeight(root.left), self.maxHeight(root.right))