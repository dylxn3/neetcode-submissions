# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        while q: 
            length = len(q)   
            rightSide = 0
            for _ in range(length):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    rightSide = node.val
                
            if rightSide: 
                res.append(rightSide)

        
        return res