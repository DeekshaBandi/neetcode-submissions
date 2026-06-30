# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #emply queue
        q = deque()
        # if the root is empty append the queue with the root
        if root:
            q.append(root)
        # initialize the num of levels to 0 
        level = 0

        while q: #loop until q is empty
            #for the values in one level
            for i in range(len(q)):
                node = q.popleft() #remove the first node

                #enqueue the children --> become the next levels 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #after one iteration, go to the next level 
            level += 1
        return level