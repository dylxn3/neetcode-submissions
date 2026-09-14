# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
            
        q = collections.deque()
        q.append(root)

        while q:
            nodesatlvl = []

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    nodesatlvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if nodesatlvl:
                res.append(nodesatlvl)
        
        return res
        
            
            
