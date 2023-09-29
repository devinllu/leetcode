# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
description: find if subRoot is a sub-tree of root

easy once you have the helper function same_tree, then just need to regularly iterate through 
every node of root, using helper function to find sub_tree
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(r1, r2):

            if not r1 and not r2:
                return True
            
            if r1 and r2 and r1.val == r2.val:
                return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)
            return False

        
        if not root:
            return False
        
        if root and sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)