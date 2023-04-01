# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traverse through a tree

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # def helper(root, lst):
        #     if not root:
        #         return lst
            
        #     lst.append(root.val)

        #     helper(root.left, lst)
        #     helper(root.right, lst)

        # lst_p = helper(p, [])
        # lst_q = helper(q, [])

        # if lst_p == lst_q:
        #     return True

        # return False
        
