# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        current = root

        while current or stack:
            while current: 
                # by traversing to very left you get the smallest val
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            # when you pop - you remove smallest value so increment
            n+=1
            # if n == k it means you found kth smallest
            if n == k:
                return current.val
            # if not traverse right subtress
            current = current.right
        
        