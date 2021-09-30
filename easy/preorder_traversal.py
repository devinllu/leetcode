# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tmp(self, root, lst):
        if root:
            lst.append(root.val)
            
            self.tmp(root.left, lst)
            self.tmp(root.right, lst)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
            
        self.tmp(root, lst)
        
        return lst
    